""" CV Toolkit by Melodi """
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
        Selects all joints in the current maya scene
        '''
    import maya.cmds as cmds

    joints = cmds.ls(type="joint")

    if joints:
        cmds.select(joints)

    else:
        raise RuntimeError("There are no joints in this scene")


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

def orient_joints():
    def orient_joints_X():
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

    orient_joints_X()

def lock_selection_translate_joints():
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

def lock_selection_scale_joints():
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

def curve_selection():
    curves_selection = cmds.ls(type="nurbsCurve")

    if curves_selection:
        curves = cmds.listRelatives(curves_selection, parent=True, fullPath=True)

        cmds.select(curves)

    else:
        cmds.warning("There are no curves in this scene")


from maya import cmds
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

mirror_curves()
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

        # Assign functionality to buttons
        if self.btn_close:
            self.btn_close.clicked.connect(
                self.close
            )

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
