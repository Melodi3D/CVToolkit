""" CV Toolkit by Melodi Clark 2026 """
# ----------------------------
# Joint Functions
# ----------------------------
import maya.cmds as cmds
import maya.mel as mel
from maya import OpenMayaUI as omui
from shiboken6 import wrapInstance
from PySide6 import QtUiTools, QtCore, QtGui, QtWidgets
from functools import partial
import sys
import os


# ----------------------------
# Joint Functions
# ----------------------------

# functions for joint selection
def joint_selection():
    '''
    Selects joints if available
    '''
    import maya.cmds as cmds

    joints = cmds.ls(type="joint")

    if joints:
        cmds.select(joints)

    else:
        raise RuntimeError("There are no joints in this scene")

def create_center_joints():
    '''
    Creates joints at the center of object
    '''
    selection = cmds.ls(selection=True)

    new_joint = cmds.joint()

    cmds.parent(new_joint, world=True)


def mirror_joints():
    '''
    Mirrors joints in the current maya scene
    '''

    joint_selection = cmds.ls(selection=True)

    if joint_selection:
        cmds.mirrorJoint(
            joint_selection[0],
            mirrorYZ=True,
            mirrorBehavior=True
        )

    else:
        raise RuntimeError("Select joints to mirror")

def orient_joints_X():
    '''
    Orients joints on the X axis
    '''
    joint_selection = cmds.ls(selection=True)

    if joint_selection:
        for joint in joint_selection:
                current_value = cmds.getAttr(joint + ".jointOrientX")

                cmds.setAttr(
                    joint + ".jointOrientX",
                    current_value + 90
                )

        else:
            raise RuntimeError("Select joints to orient on X")


def orient_joints_Y():
    '''
    Orients joints on the Y axis
    '''
    joint_selection = cmds.ls(selection=True)

    if joint_selection:
        for joint in joint_selection:
            current_value = cmds.getAttr(joint + ".jointOrientY")

            cmds.setAttr(
                joint + ".jointOrientY",
                current_value + 90
            )

        else:
            raise RuntimeError("Select joints to orient on Y")

def orient_joints_Z():
    '''
    Orients joints on the Z axis
    '''
    joint_selection = cmds.ls(selection=True)

    if joint_selection:
        for joint in joint_selection:
            current_value = cmds.getAttr(joint + ".jointOrientZ")

            cmds.setAttr(
                joint + ".jointOrientZ",
                current_value + 90
            )

        else:
            raise RuntimeError("Select joints to orient on Z")

def lock_selection_translate_joints():
    '''
    Locks the translate of selected joints
    '''
    joints_selection = cmds.ls(type="joint")

    if joints_selection:
        joints = cmds.listRelatives(joints_selection, parent=True, fullPath=True)

        cmds.select(joints)

        for joint in joints:
            cmds.setAttr(joint + ".translateX", lock=True)
            cmds.setAttr(joint + ".translateY", lock=True)
            cmds.setAttr(joint + ".translateZ", lock=True)
    else:
        raise RuntimeError("Select joints to lock translate")

def lock_selection_rotate_joints():
    '''
    Locks the rotate of selected joints
    '''
    joints_selection = cmds.ls(type="joint")

    if joints_selection:
        joints = cmds.listRelatives(joints_selection, parent=True, fullPath=True)

        cmds.select(joints)

        for joint in joints:
            cmds.setAttr(joint + ".rotateX", lock=True)
            cmds.setAttr(joint + ".rotateY", lock=True)
            cmds.setAttr(joint + ".rotateZ", lock=True)
    else:
        raise RuntimeError("Select joints to lock scale")

def lock_selection_scale_joints():
    '''
    Locks the scale of selected joints
    '''
    joints_selection = cmds.ls(type="joint")

    if joints_selection:
        joints = cmds.listRelatives(joints_selection, parent=True, fullPath=True)

        cmds.select(joints)

        for joint in joints:
            cmds.setAttr(joint + ".scaleX", lock=True)
            cmds.setAttr(joint + ".scaleY", lock=True)
            cmds.setAttr(joint + ".scaleZ", lock=True)
    else:
        raise RuntimeError("Select joints to lock scale")

def lock_selection_visibility_joints():
    '''
    Locks the visibility of selected joints
    '''
    joints_selection = cmds.ls(type="joint")

    if joints_selection:
        joints = cmds.listRelatives(joints_selection, parent=True, fullPath=True)

        cmds.select(joints)

        for joint in joints:
            cmds.setAttr(joint + ".visibility", lock=True)
    else:
        raise RuntimeError("Select joints to lock visibility")


# ----------------------------
# Control Curves Functions
# ----------------------------
# cv presets for data extraction and curve reconstruction
cv_presets = {
    "preset_1": {},
    "preset_2": {
        "degree_data": 3,
        "cv_data": [
            [0.9071069692308772, -3.500040399211375e-17, 0.03247718293832558],
            [0.9417003841069793, -9.253679210110099e-33, -0.2933462251216245],
            [0.7122571376994776, 4.798237340988473e-17, -0.7836116248912246],
            [6.785732323110912e-17, 6.785732323110912e-17, -1.1081941875543877],
            [-0.7836116248912245, 4.798237340988472e-17, -0.7836116248912244],
            [-1.1081941875543881, 3.517735619006027e-33, -5.74489823752483e-17],
            [-0.7836116248912245, -4.7982373409884725e-17, 0.7836116248912245],
            [-0.10865429778605067, -6.660964775652119e-17, 1.0204277517293527],
            [0.24563708169559312, -5.68677343467475e-17, 0.9049357520267468]
        ],
        "form_data": 0,
        "knot_data": [
            8.0, 8.0, 8.0,
            9.0, 10.0, 11.0,
            12.0, 13.0,
            14.0, 14.0, 14.0
        ]
    },
    "preset_3": {},
    "preset_4": {},
    "preset_5": {},
    "preset_6": {},
    "preset_7": {
        "degree_data": 3,
        "cv_data": [
            [0.7836116248912245, 4.798237340988473e-17, -0.7836116248912246],
            [6.785732323110912e-17, 6.785732323110912e-17, -1.1081941875543877],
            [-0.7836116248912245, 4.798237340988472e-17, -0.7836116248912244],
            [-1.1081941875543881, 3.517735619006027e-33, -5.74489823752483e-17],
            [-0.7836116248912245, -4.7982373409884725e-17, 0.7836116248912245],
            [-1.1100856969603225e-16, -6.785732323110917e-17, 1.1081941875543884],
            [0.7836116248912245, -4.798237340988472e-17, 0.7836116248912244],
            [1.1081941875543881, -9.253679210110099e-33, 1.511240500779959e-16]
        ],
        "form_data": 2,
        "knot_data": [-2.0, -1.0, 0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
    },
    "preset_8": {},
    "preset_9": {},
    "preset_10": {},
    "preset_11": {},
    "preset_12": {},
    "preset_13": {},
    "preset_14": {},
    "preset_15": {},
    "preset_16": {},
    "preset_17": {},
    "preset_18": {},
    "preset_19": {},
    "preset_20": {},
    "preset_21": {},
    "preset_22": {},
    "preset_23": [
        {
            "degree_data": 1,
            "cv_data": [
                [-0.6877673961630678, 0.6918693855892112, 0.0],
                [-1.2163493331736928, 0.6918693855892112, 0.0],
                [-1.2163493331736928, 0.0, 0.0],
                [-1.0016129139007903, 0.0, 0.0],
                [-1.0016129139007903, 0.2826939123058683, 0.0],
                [-0.7335427740424286, 0.2826939123058683, 0.0],
                [-0.7335427740424286, 0.4223880819107849, 0.0],
                [-1.0016129139007903, 0.4223880819107849, 0.0],
                [-1.0016129139007903, 0.5432057500779164, 0.0],
                [-0.6877673961630678, 0.5432057500779164, 0.0]
            ],
            "form_data": 2,
            "knot_data": [
                0.0, 1.0, 2.0, 3.0, 4.0,
                5.0, 6.0, 7.0, 8.0, 9.0,
                10.0
            ]
        },

        {
            "degree_data": 1,
            "cv_data": [
                [0.7689378968119427, 0.6918693855892112, 0.0],
                [0.5551390065442845, 0.6918693855892112, 0.0],
                [0.5551390065442845, 0.0, 0.0],
                [0.7689378968119427, 0.0, 0.0],
                [0.7689378968119427, 0.16882572064243154, 0.0],
                [0.8793942052785444, 0.28453034902496066, 0.0],
                [1.0252647268989445, 0.0, 0.0],
                [1.288540724779276, 0.0, 0.0],
                [1.0247427139204173, 0.43071968721236314, 0.0],
                [1.27721293915859, 0.6918693855892112, 0.0],
                [0.9928757453343491, 0.6918693855892112, 0.0],
                [0.7689378968119427, 0.43041039192291963, 0.0]
            ],
            "form_data": 2,
            "knot_data": [
                0.0, 1.0, 2.0, 3.0, 4.0,
                5.0, 6.0, 7.0, 8.0, 9.0,
                10.0, 11.0, 12.0
            ]
        },

        {
            "degree_data": 1,
            "cv_data": [
                [0.4187904123994821, 0.6918693855892112, 0.0],
                [0.22670965373147878, 0.6918693855892112, 0.0],
                [0.22670965373147878, 0.561135095621458, 0.0],
                [0.4187904123994821, 0.561135095621458, 0.0]
            ],
            "form_data": 2,
            "knot_data": [
                0.0, 1.0, 2.0, 3.0, 4.0
            ]
        },

        {
            "degree_data": 1,
            "cv_data": [
                [0.4187904123994821, 0.501199855732928, 0.0],
                [0.22670965373147878, 0.501199855732928, 0.0],
                [0.22670965373147878, 0.0, 0.0],
                [0.4187904123994821, 0.0, 0.0]
            ],
            "form_data": 2,
            "knot_data": [
                0.0, 1.0, 2.0, 3.0, 4.0
            ]
        },

        {
            "degree_data": 1,
            "cv_data": [
                [-0.357988426628139, 0.6918693855892112, 0.0],
                [-0.5717873168957974, 0.6918693855892112, 0.0],
                [-0.5717873168957974, 0.0, 0.0],
                [-0.357988426628139, 0.0, 0.0],
                [-0.357988426628139, 0.16882572064243154, 0.0],
                [-0.2475321181615373, 0.28453034902496066, 0.0],
                [-0.10166172652444883, 0.0, 0.0],
                [0.16161440133919425, 0.0, 0.0],
                [-0.10218373950297588, 0.43071968721236314, 0.0],
                [0.15028648573519665, 0.6918693855892112, 0.0],
                [-0.13405057810573284, 0.6918693855892112, 0.0],
                [-0.357988426628139, 0.43041039192291963, 0.0]
            ],
            "form_data": 2,
            "knot_data": [
                0.0, 1.0, 2.0, 3.0, 4.0,
                5.0, 6.0, 7.0, 8.0, 9.0,
                10.0, 11.0, 12.0
            ]
        }
    ],
    "preset_24": {},
    "preset_25": {},
    "preset_26": {},
    "preset_27": {},
    "preset_28": {},
}

def curve_data_extraction():

    # -------------------------
    # Select curve
    # -------------------------

    selected_objects = cmds.ls(selection=True)

    if not selected_objects:
        cmds.error("Please select a NURBS curve.")

    selected_curve = selected_objects[0]


    # -------------------------
    # Get all curve shapes
    # -------------------------

    curve_shapes = cmds.listRelatives(
        selected_curve,
        shapes=True,
        type="nurbsCurve"
    )

    if not curve_shapes:
        cmds.error(
            "Selected object does not contain a NURBS curve shape."
        )


    # -------------------------
    # Stores all shape data
    # -------------------------

    curve_preset = []


    # -------------------------
    # Extract every curve shape
    # -------------------------

    for shape in curve_shapes:

        # Degree
        curve_degree = cmds.getAttr(
            shape + ".degree"
        )

        # Form
        curve_form = cmds.getAttr(
            shape + ".form"
        )


        # -------------------------
        # CV positions
        # -------------------------

        curve_points = []

        curve_cvs = cmds.ls(
            shape + ".cv[*]",
            flatten=True
        )

        for cv in curve_cvs:

            cv_position = cmds.xform(
                cv,
                query=True,
                translation=True,
                objectSpace=True
            )

            curve_points.append(
                cv_position
            )


        # -------------------------
        # Knot vector
        # -------------------------

        curve_info = cmds.createNode(
            "curveInfo"
        )

        cmds.connectAttr(
            shape + ".worldSpace[0]",
            curve_info + ".inputCurve",
            force=True
        )

        curve_knots = cmds.getAttr(
            curve_info + ".knots[*]"
        )

        cmds.delete(
            curve_info
        )

        curve_knots = list(
            curve_knots
        )


        # -------------------------
        # Store shape
        # -------------------------

        shape_data = {
            "degree_data": curve_degree,
            "cv_data": curve_points,
            "form_data": curve_form,
            "knot_data": curve_knots
        }

        curve_preset.append(
            shape_data
        )


    # -------------------------
    # Return all shapes
    # -------------------------

    return curve_preset


def curve_data_reconstruction(preset):

    # -------------------------
    # Store rebuilt curves
    # -------------------------

    rebuilt_curves = []


    # -------------------------
    # Rebuild every shape
    # -------------------------

    for shape_data in preset:

        degree = shape_data["degree_data"]
        points = shape_data["cv_data"]
        preset_form = shape_data["form_data"]
        knots = shape_data["knot_data"]


        # -------------------------
        # Periodic curve
        # -------------------------

        if preset_form == 2:

            periodic_points = (
                points + points[:degree]
            )

            required_knot_count = (
                len(periodic_points)
                + degree
                - 1
            )

            periodic_knots = list(
                range(required_knot_count)
            )

            rebuilt_curve = cmds.curve(
                point=periodic_points,
                degree=degree,
                knot=periodic_knots,
                periodic=True
            )


        # -------------------------
        # Open / closed curve
        # -------------------------

        else:

            rebuilt_curve = cmds.curve(
                point=points,
                degree=degree,
                knot=knots
            )


        rebuilt_curves.append(
            rebuilt_curve
        )


    # -------------------------
    # Combine all curve shapes
    # under one transform
    # -------------------------

    main_curve = rebuilt_curves[0]

    for extra_curve in rebuilt_curves[1:]:

        extra_shapes = cmds.listRelatives(
            extra_curve,
            shapes=True,
            fullPath=True
        )

        for shape in extra_shapes:

            cmds.parent(
                shape,
                main_curve,
                shape=True,
                relative=True
            )

        cmds.delete(
            extra_curve
        )


    print(
        "Rebuilt multi-shape curve:",
        main_curve
    )

    return main_curve

def curve_selection():
    '''
    Selects curves, makes sure curves are selected
    '''
    curves_selection = cmds.ls(type="nurbsCurve")

    if curves_selection:
        curves = cmds.listRelatives(curves_selection, parent=True, fullPath=True)

        cmds.select(curves)

    else:
        cmds.warning("There are no curves in this scene")


def mirror_curves():
    '''
    Mirrors curves in the current maya scene
    '''
    curve_selection = cmds.ls(selection=True)

    if curve_selection:
        duplicated_curve = cmds.duplicate(curve_selection)

        temporary_group = cmds.group(duplicated_curve[0], world=True)

        cmds.setAttr(temporary_group + ".scaleX", -1)

        mirrored_curves = cmds.ungroup(temporary_group)

        cmds.makeIdentity(mirrored_curves, apply=True, scale=True)

    else:
        raise RuntimeError("Select curves to mirror")

def lock_selection_translate_curves():
    curves_selection = cmds.ls(type="nurbsCurve")

    if curves_selection:
        curves = cmds.listRelatives(curves_selection, parent=True, fullPath=True)

        cmds.select(curves)

        for curve in curves:
            cmds.setAttr(curve + ".translateX", lock=True)
            cmds.setAttr(curve + ".translateY", lock=True)
            cmds.setAttr(curve + ".translateZ", lock=True)
    else:
        raise RuntimeError("Select curves to lock translate")

def lock_selection_rotate_curves():
    curves_selection = cmds.ls(type="nurbsCurve")

    if curves_selection:
        curves = cmds.listRelatives(curves_selection, parent=True, fullPath=True)

        cmds.select(curves)

        for curve in curves:
            cmds.setAttr(curve + ".rotateX", lock=True)
            cmds.setAttr(curve + ".rotateY", lock=True)
            cmds.setAttr(curve + ".rotateZ", lock=True)
    else:
        raise RuntimeError("Select curves to lock rotate")

def lock_selection_scale_curves():
    curves_selection = cmds.ls(type="nurbsCurve")

    if curves_selection:
        curves = cmds.listRelatives(curves_selection, parent=True, fullPath=True)

        cmds.select(curves)

        for curve in curves:
            cmds.setAttr(curve + ".scaleX", lock=True)
            cmds.setAttr(curve + ".scaleY", lock=True)
            cmds.setAttr(curve + ".scaleZ", lock=True)
    else:
        raise RuntimeError("Select curves to lock scale")

def lock_selection_visibility_curves():
    curves_selection = cmds.ls(type="nurbsCurve")

    if curves_selection:
        curves = cmds.listRelatives(curves_selection, parent=True, fullPath=True)

        cmds.select(curves)

        for curve in curves:
            cmds.setAttr(curve + ".visibility", lock=True)
    else:
        raise RuntimeError("Select curves to lock visibility")

# ----------------------------
# Landmark Functions
# ----------------------------

# color presets
red = (1.0, 0.0, 0.0)
orange = (1.0, 0.5, 0.0)
yellow = (1.0, 1.0, 0.0)
green = (0.0, 1.0, 0.0)
blue = (0.0, 0.0, 1.0)
magenta = (1.0, 0.0, 1.0)
cyan = (0.0, 1.0, 1.0)
pink = (1.0, 0.4, 0.7)

# landmark presets
landmark_presets = {
    "preset_1": {},
    "preset_2": {},
    "preset_3": {},
    "preset_4": {},
    "preset_5": {},
    "preset_6": {},
    "preset_7": {},
    "preset_8": {},
}


# function for confirming faces are selected
def faces_confirm():
    '''
    Confirms if faces are selected
    '''
    cmds.confirmDialog(
        title="CV Toolkit",
        message="Please select at least one polygon face.",
        button=["OK"]
    )

# function for creating landmarks
def create_landmark(colors):
    '''
    Creates colored landmarks
    '''
    # user selects faces
    selection = cmds.ls(sl=True, flatten=True)

    # filters the selection to polygon faces
    faces = cmds.filterExpand(sm=34)

    # error handling due to no selection
    if not selection:
        raise RuntimeError("Error: Nothing is selected")

    # error handling due to no faces in selection
    if not faces:
        faces_confirm()
        raise RuntimeError("Error: No faces selected")

    # error handling due to wrong colors
    for color in colors:
        if color < 0.0 or color > 1.0:
            raise RuntimeError(
                "Error: Colors should be between 0.0 and 1.0"
            )

    # creates landmark shader as a shader node, with lambert material
    landmark_shader = cmds.shadingNode(
        "lambert",
        asShader=True
    )

    # selects faces
    cmds.select(faces)

    # assigns shader to the selected faces
    cmds.hyperShade(assign=landmark_shader)

    # sets the colors for the landmark shader to RGB values
    cmds.setAttr(
        f"{landmark_shader}.color",
        colors[0],
        colors[1],
        colors[2],
        type="double3"
    )

# ----------------------------
# Misc Functions
# ----------------------------
def snap_tool():
    '''
    Snaps objects to each other
    '''
    object_selection = cmds.ls(selection=True)

    if len(object_selection) < 2:
        raise RuntimeError("Select two objects to snap")

    cmds.matchTransform(object_selection[0], object_selection[1])
# ----------------------------
# ----------------------------
# Presets
# ----------------------------


# ----------------------------
# UI Development
# ----------------------------
class CVToolkit(QtWidgets.QWidget):
    """Creates CV Toolkit window."""

    window = None

    def __init__(self, parent=None):
        """Initialize class."""

        super().__init__(parent)

        self.setWindowFlags(QtCore.Qt.Window)

        # Robust pathing to handle Maya Script Editor memory vs normal loading
        try:
            self.widgetPath = os.path.dirname(
                os.path.abspath(__file__)
            )

            if not self.widgetPath:
                raise NameError

        except (NameError, AttributeError):

            self.widgetPath = (
                r"C:\Users\melme\OneDrive - Rutgers University\Desktop\CVToolkit"
            )

        self.iconsPath = os.path.join(
            self.widgetPath,
            "icons"
        )

        # Debug helper log messages in Maya history
        print(
            f"// CVToolkit Directory: {self.widgetPath}"
        )

        print(
            f"// Loading Icons From Folder: {self.iconsPath}"
        )

        # Load UI file dynamically
        self.widget = QtUiTools.QUiLoader().load(
            os.path.join(
                self.widgetPath,
                "CVToolkit.ui"
            )
        )

        self.widget.setParent(self)

        # Set initial window size
        self.resize(700, 950)

        # Locate core UI widgets
        self.btn_close = self.widget.findChild(
            QtWidgets.QPushButton,
            "btn_close"
        )

        self.btn_circle = self.widget.findChild(
            QtWidgets.QToolButton,
            "btn_circle"
        )

        # Assign functionality to buttons
        if self.btn_close:
            self.btn_close.clicked.connect(
                self.close
            )

        if self.btn_circle:
            self.btn_circle.clicked.connect(
                load_preset_7
            )

        # Maps custom curve buttons to PNG files
        self.button_icon_map = {
            "btn_CVlogo": "CVtoolKitlogo.png",
            "btn_arc180": "arc180.png",
            "btn_arc240": "arc240.png",
            "btn_arrow": "arrow.png",
            "btn_axis": "axis.png",
            "btn_bone": "bone.png",
            "btn_bowtie": "bowtie.png",
            "btn_circle": "circle.png",
            "btn_circle_crossed_pins": "circle_crossed_pins.png",
            "btn_circle_top_pin": "circle_top_pin.png",
            "btn_circle_with_arrow_1": "circle_with_arrow_1.png",
            "btn_circle_with_arrow_2": "circle_with_arrow_2.png",
            "btn_circle_with_arrow_3": "circle_with_arrow_3.png",
            "btn_circlecross": "circlecross.png",
            "btn_cog": "cog.png",
            "btn_cross_arrow": "cross_arrow.png",
            "btn_crown": "crown.png",
            "btn_cylinder": "cylinder.png",
            "btn_decagram": "decagram.png",
            "btn_diamond": "diamond.png",
            "btn_drop": "drop.png",
            "btn_eyebrow": "eyebrow.png",
            "btn_FKiK": "FKiK.png",
            "btn_flower": "flower.png",
            "btn_FourPointStar": "FourPointStar.png",
            "btn_gearstar": "gearstar.png",
            "btn_halfcircle": "halfcircle.png",
            "btn_heart": "heart.png",
            "btn_hexa_cone": "hexa_cone.png",
            "btn_hexagon": "hexagon.png",
            "btn_moon_crescent": "moon_crescent.png",
            "btn_oval_rings": "oval_rings.png",
            "btn_paw": "paw.png",
            "btn_pill": "pill.png",
            "btn_plus": "plus.png",
            "btn_pyramid": "pyramid.png",
            "btn_square": "square.png",
            "btn_square_cross": "square_cross.png",
            "btn_square_double_pin": "square_double_pin.png",
            "btn_square_round": "square_round.png",
            "btn_star": "star.png",
            "btn_target": "target.png",
            "btn_thick_arrow": "thick_arrow.png",
            "btn_thick_cross_arrow": "thick_cross_arrow.png",
            "btn_thick_double_arrow": "thick_double_arrow.png",
            "btn_triangle": "triangle.png",
            "btn_triangle_pin": "triangle_pin.png",
            "btn_visor": "visor.png",
            "btn_cube": "cube.png",
            "btn_crossarrow": "crossarrow.png",
        }

        # Loads icons
        self.load_tool_button_icons()

    def resizeEvent(self, event):
        """Called on automatically generated resize event."""

        self.widget.resize(
            self.width(),
            self.height()
        )

    def load_tool_button_icons(self):
        """Load transparent icons onto tool buttons."""

        for btn_name, icon_filename in self.button_icon_map.items():

            tool_btn = self.widget.findChild(
                QtWidgets.QToolButton,
                btn_name
            )

            if tool_btn:

                icon_file_path = os.path.join(
                    self.iconsPath,
                    icon_filename
                )

                if os.path.exists(icon_file_path):

                    pixmap = QtGui.QPixmap(
                        icon_file_path
                    )

                    if not pixmap.isNull():

                        tool_btn.setIcon(
                            QtGui.QIcon(pixmap)
                        )

                        tool_btn.setIconSize(
                            QtCore.QSize(125, 125)
                        )

                    else:
                        print(
                            f"// Warning: Maya failed to read "
                            f"graphic data for {icon_filename}"
                        )

                else:
                    print(
                        f"// Warning: File does not exist at "
                        f"{icon_file_path}"
                    )

            else:
                print(
                    f"// Warning: Could not find UI tool "
                    f"button named '{btn_name}'"
                )

def load_preset_7():
    curve_data_reconstruction(
        cv_presets["preset_7"]
    )

def openWindow():
    """Attach CV Toolkit to Maya's main window."""

    if QtWidgets.QApplication.instance():

        # Find any existing instances and destroy them
        for win in QtWidgets.QApplication.allWindows():

            if "CVToolkitWindow" in win.objectName():
                win.destroy()

    mayaMainWindowPtr = omui.MQtUtil.mainWindow()

    mayaMainWindow = wrapInstance(
        int(mayaMainWindowPtr),
        QtWidgets.QWidget
    )

    CVToolkit.window = CVToolkit(
        parent=mayaMainWindow
    )

    CVToolkit.window.setObjectName(
        "CVToolkitWindow"
    )

    CVToolkit.window.setWindowTitle(
        "CV Toolkit v1"
    )

    CVToolkit.window.show()
