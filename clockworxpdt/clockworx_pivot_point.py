# ***** BEGIN GPL LICENSE BLOCK *****
#
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.	See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ***** END GPL LICENCE BLOCK *****

# ----------------------------------------------------------
# Author: Alan Odom (Clockmender)
# ----------------------------------------------------------
# useful code: bpy.ops.view3d.snap_cursor_to_selected()

import bpy
import bgl
import blf
import gpu
import bmesh
from gpu_extras.batch import batch_for_shader
from bpy.types import Operator, Panel, PropertyGroup, SpaceView3D
from mathutils import Vector, Matrix
from math import pi
from .pdt_functions import viewCoords, viewCoordsI

# Shader for displaying the Pivot Point as Graphics.
#
shader = gpu.shader.from_builtin('3D_UNIFORM_COLOR') if not bpy.app.background else None

# Draw function, requires a set of coodinates, the draw type LINES, POINTS or TRIS
# then the colour in the form RGBA and the context.
#
def draw_3d(coords, type, rgba, context):
    scene = context.scene
    batch = batch_for_shader(shader, type, {"pos": coords})

    try:
        if coords is not None:
            #bgl.glEnable(bgl.GL_LINE_SMOOTH)
            bgl.glEnable(bgl.GL_BLEND)
            shader.bind()
            shader.uniform_float("color", rgba)
            batch.draw(shader)
    except:
        pass

# Create the coodinate sets to pass to the Draw Function.
#
def draw_callback_3d(self, context):
    scene = context.scene
    w = context.region.width
    x = scene.pdt_pivotloc.x
    y = scene.pdt_pivotloc.y
    z = scene.pdt_pivotloc.z
    # Scale it from view
    areas = [a for a in context.screen.areas if a.type == 'VIEW_3D']
    if len(areas) > 0:
        sf = abs(areas[0].spaces.active.region_3d.window_matrix.decompose()[2][1])
    a = w/sf/10000 * scene.pdt_pivotsize
    b = a * 0.65
    c = a * 0.05 + (scene.pdt_pivotwidth * a * 0.02)
    o = c / 3

    # X Axis
    coords = [(x,y,z), (x+b,y-o,z), (x+b,y+o,z), (x+a,y,z), (x+b,y+c,z), (x+b,y-c,z)]
    colour = (1.0, 0.0, 0.0, scene.pdt_pivotalpha)
    draw_3d(coords, 'TRIS', colour, context)
    coords = [(x,y,z),(x+a,y,z)]
    draw_3d(coords, 'LINES', colour, context)
    # Y Axis
    coords = [(x,y,z), (x-o,y+b,z), (x+o,y+b,z), (x,y+a,z), (x+c,y+b,z), (x-c,y+b,z)]
    colour = (0.0, 1.0, 0.0, scene.pdt_pivotalpha)
    draw_3d(coords, 'TRIS', colour, context)
    coords = [(x,y,z),(x,y+a,z)]
    draw_3d(coords, 'LINES', colour, context)
    # Z Axis
    coords = [(x,y,z), (x-o,y,z+b), (x+o,y,z+b), (x,y,z+a), (x+c,y,z+b), (x-c,y,z+b)]
    colour = (0.2, 0.5, 1.0, scene.pdt_pivotalpha)
    draw_3d(coords, 'TRIS', colour, context)
    coords = [(x,y,z),(x,y,z+a)]
    draw_3d(coords, 'LINES', colour, context)
    # Centre
    coords = [(x,y,z)]
    colour = (1.0, 1.0, 0.0, scene.pdt_pivotalpha)
    draw_3d(coords, 'POINTS', colour, context)

# Run the Pivot Point draw routines unless ] is pressed.
#
class PDT_OT_ModalDrawOperator(bpy.types.Operator):
    """Show/Hide Pivot Point"""
    bl_idname = "pdt.modaldraw"
    bl_label = "PDT Modal Draw"

    _handle = None  # keep function handler

    # ----------------------------------
    # Enable gl drawing adding handler
    # ----------------------------------
    @staticmethod
    def handle_add(self, context):
        if PDT_OT_ModalDrawOperator._handle is None:
            PDT_OT_ModalDrawOperator._handle = SpaceView3D.draw_handler_add(draw_callback_3d, (self, context),
                                                                        'WINDOW',
                                                                        'POST_VIEW')
            context.window_manager.pdt_run_opengl = True

    # ------------------------------------
    # Disable gl drawing removing handler
    # ------------------------------------
    #
    @staticmethod
    def handle_remove(self, context):
        if PDT_OT_ModalDrawOperator._handle is not None:
            SpaceView3D.draw_handler_remove(PDT_OT_ModalDrawOperator._handle, 'WINDOW')
        PDT_OT_ModalDrawOperator._handle = None
        context.window_manager.pdt_run_opengl = False

    # ------------------------------
    # Execute button action
    # ------------------------------
    def execute(self, context):
        if context.area.type == 'VIEW_3D':
            if context.window_manager.pdt_run_opengl is False:
                self.handle_add(self, context)
                context.area.tag_redraw()
            else:
                self.handle_remove(self, context)
                context.area.tag_redraw()

            return {'FINISHED'}
        else:
            self.report({'WARNING'},
                        "View3D not found, cannot run operator")

        return {'CANCELLED'}


# Rotate Object Geometry by Menu Value in View Orientation about the Pivot Point.
#
class PDT_OT_ViewPlaneRotate(bpy.types.Operator):
    """Rotate Selected Vertices about Pivot Point in View Plane"""
    bl_idname = "pdt.viewplanerot"
    bl_label = "PDT View Rotate"

    def execute(self,context):
        scene = context.scene
        obj = bpy.context.view_layer.objects.active
        if obj == None:
            self.report({'ERROR'},
                    "Select 1 Object")
            return {"FINISHED"}
        if obj.mode != 'EDIT':
            self.report({'ERROR'},
                    "Only in Works on Vertices in Edit Mode")
            return {"FINISHED"}
        bm = bmesh.from_edit_mesh(obj.data)
        v1 = Vector((0,0,0))
        v2 = viewCoords(0,0,1)
        axis = (v2 - v1).normalized()
        rot = Matrix.Rotation((scene.pdt_pivotang*pi/180), 4, axis)
        verts = verts=[v for v in bm.verts if v.select]
        bmesh.ops.rotate(bm, cent=scene.pdt_pivotloc-obj.matrix_world.decompose()[0], matrix=rot, verts=verts)
        bmesh.update_edit_mesh(obj.data)
        return {"FINISHED"}

# Scalee Object Geometry by Menu Values in Global Orientation about the Pivot Point.
#
class PDT_OT_ViewPlaneScale(bpy.types.Operator):
    """Scale Selected Vertices about Pivot Point"""
    bl_idname = "pdt.viewscale"
    bl_label = "PDT View Scale"

    def execute(self,context):
        scene = context.scene
        obj = bpy.context.view_layer.objects.active
        if obj == None:
            self.report({'ERROR'},
                    "Select 1 Object")
            return {"FINISHED"}
        if obj.mode != 'EDIT':
            self.report({'ERROR'},
                    "Only in Works on Vertices in Edit Mode")
            return {"FINISHED"}
        bm = bmesh.from_edit_mesh(obj.data)
        verts = verts=[v for v in bm.verts if v.select]
        for v in verts:
            dx = (scene.pdt_pivotloc.x - obj.matrix_world.decompose()[0].x - v.co.x) * (1-scene.pdt_pivotscale.x)
            dy = (scene.pdt_pivotloc.y - obj.matrix_world.decompose()[0].y - v.co.y) * (1-scene.pdt_pivotscale.y)
            dz = (scene.pdt_pivotloc.z - obj.matrix_world.decompose()[0].z - v.co.z) * (1-scene.pdt_pivotscale.z)
            dv = Vector((dx,dy,dz))
            v.co = v.co + dv
        bmesh.update_edit_mesh(obj.data)
        return {"FINISHED"}

# Move the Pivot Point to the Cursor Location.
#
class PDT_OT_PivotToCursor(bpy.types.Operator):
    """Set The Pivot Point ot Curor Location"""
    bl_idname = "pdt.pivotcursor"
    bl_label = "PDT Pivot To Cursor"

    def execute(self,context):
        scene = context.scene
        scene.pdt_pivotloc = scene.cursor.location
        return {"FINISHED"}

# Move the Cursor to the Pivot Point Location.
#
class PDT_OT_CursorToPivot(bpy.types.Operator):
    """Set The Curor Location at Pivot Point"""
    bl_idname = "pdt.cursorpivot"
    bl_label = "PDT Cursor To Pivot"

    def execute(self,context):
        scene = context.scene
        scene.cursor.location = scene.pdt_pivotloc
        return {"FINISHED"}

# Move the Pivot Point to the Selected Vertex Location.
#
class PDT_OT_PivotSelected(bpy.types.Operator):
    """Set Pivot Point to Selected Geometry"""
    bl_idname = "pdt.pivotselected"
    bl_label = "PDT Pivot to Selected"

    def execute(self,context):
        scene = context.scene
        obj = bpy.context.view_layer.objects.active
        if obj == None:
            self.report({'ERROR'},
                    "Select 1 Object")
            return {"FINISHED"}
        obj_loc = obj.matrix_world.decompose()[0]
        if obj.mode != 'EDIT':
            self.report({'ERROR'},
                    "Only in Works on Vertices in Edit Mode")
            return {"FINISHED"}
        bm = bmesh.from_edit_mesh(obj.data)
        verts = verts=[v for v in bm.verts if v.select]
        if len(verts) > 0:
            old_cursor_loc = scene.cursor.location.copy()
            bpy.ops.view3d.snap_cursor_to_selected()
            scene.pdt_pivotloc = scene.cursor.location
            scene.cursor.location = old_cursor_loc
            return {"FINISHED"}
        else:
            self.report({'ERROR'},
                    "Nothing Selected!")
            return {"FINISHED"}

# Move the Pivot Point to the Selected Object Origin.
#
class PDT_OT_PivotOrigin(bpy.types.Operator):
    """Set Pivot Point at Object Origin"""
    bl_idname = "pdt.pivotorigin"
    bl_label = "PDT Pivot to Object Origin"

    def execute(self,context):
        scene = context.scene
        obj = bpy.context.view_layer.objects.active
        if obj == None:
            self.report({'ERROR'},
                    "Select 1 Object")
            return {"FINISHED"}
        obj_loc = obj.matrix_world.decompose()[0]
        scene.pdt_pivotloc = obj_loc
        return {"FINISHED"}

# Write the Pivot Point Location to a Custom Property of the Object.
#
class PDT_OT_PivotWrite(bpy.types.Operator):
    """Write Pivot Point Location to Object"""
    bl_idname = "pdt.pivotwrite"
    bl_label = "PDT Write PP to Object?"

    @classmethod
    def poll(cls, context):
        return True

    def execute(self,context):
        scene = context.scene
        obj = bpy.context.view_layer.objects.active
        if obj == None:
            self.report({'ERROR'},
                    "Select 1 Object")
            return {"FINISHED"}
        obj['PDT_PP_LOC'] = scene.pdt_pivotloc
        return {"FINISHED"}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def draw(self, context):
        row = self.layout
        row.label(text="Are You Sure About This?")

# Set the Pivot Point Location to the value stored in the Selected Object.
#
class PDT_OT_PivotRead(bpy.types.Operator):
    """Read Pivot Point Location from Object"""
    bl_idname = "pdt.pivotread"
    bl_label = "PDT Read PP"

    def execute(self,context):
        scene = context.scene
        obj = bpy.context.view_layer.objects.active
        if obj == None:
            self.report({'ERROR'},
                    "Select 1 Object")
            return {"FINISHED"}
        if obj['PDT_PP_LOC'] is not None:
            scene.pdt_pivotloc = obj['PDT_PP_LOC']
            return {"FINISHED"}
        else:
            self.report({'ERROR'},
                    "Custom Property PDT_PP_LOC for this object not found, have you Written it yet?")
            return {"FINISHED"}

# Create the Panel Menu.
#
class PDT_PT_Panel2(Panel):
    bl_idname = "PDT_PT_panel2"
    bl_label = "PDT Pivot Point"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category= 'PDT'

    def draw(self, context):
        scene = context.scene
        layout = self.layout
        row = layout.row()
        split = row.split(factor=0.4, align=True)
        if context.window_manager.pdt_run_opengl is False:
            icon = 'PLAY'
            txt = 'Show'
        else:
            icon = "PAUSE"
            txt = 'Hide'
        split.operator("pdt.modaldraw", icon=icon, text=txt)
        split.prop(scene, 'pdt_pivotsize', text = "")
        split.prop(scene, 'pdt_pivotwidth', text = "")
        split.prop(scene, 'pdt_pivotalpha', text = "")
        row = layout.row()
        row.label(text='Pivot Point Location')
        row = layout.row()
        row.prop(scene, 'pdt_pivotloc', text = "")
        row = layout.row()
        col = row.column()
        col.operator("pdt.pivotselected", icon='EMPTY_AXIS', text="Selection")
        col = row.column()
        col.operator("pdt.pivotcursor", icon='EMPTY_AXIS', text="Cursor")
        col = row.column()
        col.operator("pdt.pivotorigin", icon='EMPTY_AXIS', text="Origin")
        row = layout.row()
        col = row.column()
        col.operator("pdt.viewplanerot", icon='EMPTY_AXIS', text="Rotate")
        col = row.column()
        col.prop(scene, 'pdt_pivotang', text = "Angle")
        row = layout.row()
        col = row.column()
        col.operator("pdt.viewscale", icon='EMPTY_AXIS', text="Scale")
        col = row.column()
        col.operator("pdt.cursorpivot", icon='EMPTY_AXIS', text="Cursor To Pivot")
        row = layout.row()
        row.label(text='Pivot Point Scale Factors')
        row = layout.row()
        row.prop(scene, 'pdt_pivotscale', text = "")
        row = layout.row()
        col = row.column()
        col.operator("pdt.pivotwrite", icon='FILE_TICK', text="PP Write")
        col = row.column()
        col.operator("pdt.pivotread", icon='FILE', text="PP Read")