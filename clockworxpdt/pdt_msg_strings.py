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
#
# ----------------------------------------------------------
# Authors: Alan Odom (Clockmender), Rune Morling (ermo)
#  Copyright © 2019
# ----------------------------------------------------------
#
# English Version
#
# If you edit this file do not change any of the PDT_ format, just the Text Value in "'s
# Do not delete any of the PDT_ lines
#
# Menu Labels
#
PDT_LAB_ABS           = "Absolute"    # "Global"
PDT_LAB_DEL           = "Delta"       # "Relative"
PDT_LAB_DIR           = "Direction"   # "Polar"
PDT_LAB_NOR           = "Normal"      # "Perpendicular"
PDT_LAB_ARCCENTRE     = "Arc Centre"
PDT_LAB_PLANE         = "Plane"
PDT_LAB_MODE          = "Mode"
PDT_LAB_OPERATION     = "Operation"
PDT_LAB_PERCENT       = "Percent"
PDT_LAB_INTERSECT     = "Intersect"   # "Convergance"
PDT_LAB_ORDER         = "Order"
PDT_LAB_FLIPANGLE     = "Flip Angle"
PDT_LAB_FLIPPERCENT   = "Flip %"
PDT_LAB_ALLACTIVE     = "All/Active"
PDT_LAB_VARIABLES     = "Coordinates/Delta Offsets & Other Variables"
PDT_LAB_XVALUE        = "X"
PDT_LAB_DISVALUE      = "Distance"
PDT_LAB_YVALUE        = "Y"
PDT_LAB_ANGLEVALUE    = "Angle"
PDT_LAB_ZVALUE        = "Z"
PDT_LAB_PERCENTS      = "%"
PDT_LAB_TOOLS         = "Tools"
PDT_LAB_JOIN2VERTS    = "Join 2 Verts"
PDT_LAB_ORIGINCURSOR  = "Origin To Cursor"
PDT_LAB_AD2D          = "Set A/D 2D"
PDT_LAB_AD3D          = "Set A/D 3D"
PDT_LAB_TAPERAXES     = ""            # Intentionally left blank
PDT_LAB_TAPER         = "Taper"
PDT_LAB_INTERSETALL   = "Intersect All"
PDT_LAB_BISECT        = "Bisect"
PDT_LAB_EDGETOEFACE   = "Edge-Face"
PDT_LAB_FILLET        = "Fillet"
PDT_LAB_SEGMENTS      = "Segments"
PDT_LAB_USEVERTS      = "Use Verts"
PDT_LAB_RADIUS        = "Radius"
PDT_LAB_PROFILE       = "Profile"
PDT_LAB_PIVOTSIZE     = ""            # Intentionally left blank
PDT_LAB_PIVOTWIDTH    = ""            # Intentionally left blank
PDT_LAB_PIVOTALPHA    = ""            # Intentionally left blank
PDT_LAB_PIVOTLOC      = ""            # Intentionally left blank
PDT_LAB_PIVOTLOCH     = "Pivot Point Location"
#
# Error Message
#
PDT_ERR_NO_ACT_OBJ    = "No Active Object - Please Select an Object"
PDT_ERR_NO_ACT_VERT   = "No Active Vertex - Select One Vertex Individually"
PDT_ERR_NO_SEL_GEOM   = "No Geometry/Objects Selected"
PDT_ERR_NO_ACT_VERTS  = "No Selected Geometry - Please Select some Geometry"
PDT_ERR_NON_VALID     = "is Not a Valid Option for Command:"
PDT_ERR_VERT_MODE     = "Work in Vertex Mode for this Function"

PDT_ERR_SEL_1_VERTI   = "Select at least 1 Vertex Individually (Currently selected:"
PDT_ERR_SEL_1_VERT    = "Select at least 1 Vertex (Currently selected:"
PDT_ERR_SEL_2_VERTI   = "Select at least 2 Vertices Individually (Currently selected:"
PDT_ERR_SEL_2_VERTIO  = "Select Exactly 2 Vertices Individually (Currently selected:"
PDT_ERR_SEL_2_VERTS   = "Select Exactly 2 Vertices (Currently selected:"
PDT_ERR_SEL_3_VERTS   = "Select Exactly 3 Vertices (Currently selected:"
PDT_ERR_SEL_3_VERTIO  = "Select Exactly 3 Vertices Individually (Currently selected:"
PDT_ERR_SEL_2_V_1_E   = "Select 2 Vertices Individually, or 1 Edge (Currently selected:"
PDT_ERR_SEL_4_VERTS   = "Select 4 Vertices Individually, or 2 Edges (Currently selected:"

PDT_ERR_SEL_1_EDGE    = "Select at only 1 Edge (Currently selected:"
PDT_ERR_SEL_1_EDGEM   = "Select at least 1 Edge (Currently selected:"

PDT_ERR_SEL_1_OBJ     = "Select Exactly 1 Object (Currently selected:"
PDT_ERR_SEL_2_OBJS    = "Select Exactly 2 Objects (Currently selected:"
PDT_ERR_SEL_3_OBJS    = "Select Exactly 3 Objects (Currently selected:"
PDT_ERR_SEL_4_OBJS    = "Select Exactly 4 Objects (Currently selected:"

PDT_ERR_FACE_SEL      = "You have a Face Selected, this would have ruined the Topology"

PDT_ERR_INT_LINES     = "Implied Lines Do Not Intersect in"
PDT_ERR_INT_NO_ALL    = "Active Vertex was not Closest to Intersection and All/Act was not Selected"
PDT_ERR_STRIGHT_LINE  = "Selected Points all lie in a Straight Line"
PDT_ERR_CONNECTED     = "Vertices are already Connected"
PDT_ERR_EDIT_MODE     = "Only Works in EDIT Mode (Current mode:"
PDT_ERR_EDOB_MODE     = "Only Works in EDIT, or OBJECT Modes (Current mode:"
PDT_ERR_TAPER_ANG     = "Angle must be in Range -80 to +80 (Currently set to:"
PDT_ERR_TAPER_SEL     = "Select at Least 2 Vertices Individually - Active is Rotation Point (Currently selected:"
PDT_ERR_NO3DVIEW      = "View3D not found, cannot run operator"
PDT_ERR_SCALEZERO     = "Scale Distance is 0"

PDT_ERR_CHARS_NUM     = "Bad Command Format, not enough Characters"
PDT_ERR_BADFLETTER    = "Bad Operator (1st Letter); C D E F G N M P S or V only"
PDT_ERR_BADSLETTER    = "Bad Mode (2nd Letter); A D I or P only (+ X Y & Z for Maths) (+ V & G for Fillet)"
PDT_ERR_BADMATHS      = "Not a Valid Mathematical Expression!"
PDT_ERR_BADCOORDL     = "X Y & Z Not permitted in anything other than Maths Operations"
PDT_ERR_BAD1VALS      = "Bad Command - 1 Value needed"
PDT_ERR_BAD2VALS      = "Bad Command - 2 Values needed"
PDT_ERR_BAD3VALS      = "Bad Command - 3 Coords needed"
PDT_ERR_ADDVEDIT      = "Only Add New Vertices in Edit Mode"
PDT_ERR_SPLITEDIT     = "Only Split Edges in Edit Mode"
PDT_ERR_EXTEDIT       = "Only Extrude Vertices in Edit Mode"
PDT_ERR_DUPEDIT       = "Only Duplicate Geometry in Edit Mode"
PDT_ERR_FILEDIT       = "Only Fillet Geometry in Edit Mode"
PDT_ERR_NOCOMMAS      = "No commas allowed in Maths Command"

PDT_ERR_2CPNPE        = "Select 2 Co-Planar Non-Parallel Edges"
PDT_ERR_NCEDGES       = "Edges must be Co-Planar Non-Parallel Edges, Selected Edges aren't"
PDT_ERR_1EDGE1FACE    = "Select 1 face and 1 Detached Edge"
PDT_ERR_NOINT         = "No Intersection Found, see the Info Panel for Details"

# Info messages
#
PDT_INF_OBJ_MOVED     = "Active Object Moved to Intersection, "

# Descriptions
#
PDT_DES_XDELTA        = "X Coord Delta"
PDT_DES_YDELTA        = "Y Coord Delta"
PDT_DES_ZDELTA        = "Z Coord Delta"
PDT_DES_OFFDIS        = "Offset Distance"
PDT_DES_OFFANG        = "Offset Angle"
PDT_DES_OFFPER        = "Offset Percentage"
PDT_DES_WORPLANE      = "Choose Working Plane"
PDT_DES_MOVESEL       = "Select Move Mode"
PDT_DES_OPMODE        = "Select Operation Mode"
PDT_DES_ROTMOVAX      = "Rotational Axis - Movement Axis"
PDT_DES_FLIPANG       = "Flip Angle 180 degrees"
PDT_DES_FLIPPER       = "Flip Percent to 100 - %"
PDT_DES_TRIM          = "Trim/Extend only Active Vertex, or All"
PDT_DES_LIBOBS        = "Objects in Library"
PDT_DES_LIBCOLS       = "Collections in Library"
PDT_DES_LIBMATS       = "Materials in Library"
PDT_DES_LIBMODE       = "Library Mode"
PDT_DES_LIBSER        = "Enter A Search String (Contained)"
PDT_DES_OBORDER       = "Object Order to Lines"
PDT_DES_VALIDLET      = "Valid 1st letters; C D E G N P S V, Valid 2nd letters: A D I P"
PDT_DES_PPLOC         = "Location of PivotPoint"
PDT_DES_PPSCALEFAC    = "Scale Factors"
PDT_DES_PPSIZE        = "Pivot Size Factor"
PDT_DES_PPWIDTH       = "Pivot Line Width in Pixels"
PDT_DES_PPTRANS       = "Pivot Point Transparency"
PDT_DES_PIVOTDIS      = "Input Distance to Compare with Sytem Distance to set Scales"
PDT_DES_FILLETRAD     = "Fillet Radius"
PDT_DES_FILLETSEG     = "Number of Fillet Segments"
PDT_DES_FILLETPROF    = "Fillet Profile"
PDT_DES_FILLETVERTS   = "Use Vertices, or Edges, Set to False for Extruded Geometry"
