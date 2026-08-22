""" CV Toolkit by Melodi """

import maya.cmds as cmds
import maya.mel as mel
from maya import OpenMayaUI as omui
from shiboken6 import wrapInstance
from PySide6 import QtUiTools, QtCore, QtGui, QtWidgets
from functools import partial
import sys
import os


# landmark functions

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
    cmds.confirmDialog(
        title="CV Toolkit",
        message="Please select at least one polygon face.",
        button=["OK"]
    )


# function for creating landmarks
def create_landmark(colors):

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
                r"C:\Users\melme\OneDrive - Rutgers University"
                r"\Desktop\CVToolkit"
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
        self.resize(600, 850)

        # Locate core UI widgets
        self.btn_close = self.widget.findChild(
            QtWidgets.QPushButton,
            "btn_close"
        )

        # Map custom curve buttons to PNG files
        self.button_icon_map = {
            "btn_CVlogo": "CVtoolKitlogo.png",
            "btn_square": "square.png",
            "btn_cube": "cube.png",
            "btn_arrow": "arrow.png",
        }

        # Load icons
        self.load_tool_button_icons()

        # Assign functionality to buttons
        if self.btn_close:
            self.btn_close.clicked.connect(
                self.close
            )

    def load_tool_button_icons(self):
        """Load transparent icons onto tool buttons."""

        for btn_name, icon_filename in self.button_icon_map.items():

            tool_btn = self.widget.findChild(
                QtWidgets.QToolButton,
                btn_name
            )

            if tool_btn:

                tool_btn.setStyleSheet(
                    """
                    QToolButton {
                        background-color: transparent;
                        border: none;
                    }
                    """
                )

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

    def resizeEvent(self, event):
        """Called on automatically generated resize event."""

        self.widget.resize(
            self.width(),
            self.height()
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
        "CV Toolkit"
    )

    CVToolkit.window.show()