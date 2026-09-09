# CVToolkit

CVToolkit is a Maya rigging tool I created to make working with NURBS controls and modeling landmarks faster and more convenient.

The project originally started as a smaller Landmark Tool, but I continued expanding it as I learned more about rigging and Maya tool development. It now includes a control library, custom presets, curve editing tools, color controls, mirroring, and several utilities I can now use regularly as assistance while rigging.

The main idea behind CVToolkit is to keep common control-building tasks in one place instead of repeatedly setting them up by hand. 

## Features

### CV Controls
- Library of predefined NURBS control shapes
- Support for controls made from multiple curve shapes
- Scale control CVs without changing transform values
- Mirror curve controls
- Extract and rebuild curve data

### User Presets
- Save custom controls for later use
- Save modeling landmarks as presets
- Rename saved presets
- Recreate single and multi-shape controls

### Modeling Landmarks
- Create colored landmarks directly on a model
- Save selected polygon faces as landmark presets
- Choose from several landmark colors
- Quickly reuse saved landmark selections

### Rigging Utilities
- Select joints or curve controls
- Mirror joints, curves, and supported transforms
- Lock and unlock transform channels
- Visibility controls
- Create offset groups
- Freeze and center utilities

### Control Colors
- Built-in RGB color presets
- Custom RGB sliders
- Apply custom colors directly to controls

## Built With
- Autodesk Maya 2025
- Python
- PySide6
- Qt Designer
- Also I used a heavily modified UI template made by isaacoster-img for the UI design
https://www.youtube.com/watch?v=i9T0AudMS4U

## Installation

1. Download the CVToolkit folder.
2. Place the entire `CVToolkit` folder inside your Maya scripts directory:

   `Documents/maya/2025/scripts/`

3. Restart Maya.
4. Open the **Python** tab of Maya's Script Editor.
5. Run:

```python
import CVToolkit.CVToolkit as cvt
cvt.openWindow()
```

CVToolkit should now open inside Maya.

You can also add the launch code to a Maya shelf button for quicker access.

## How It Works

One of the main systems I wanted to experiment with while building CVToolkit was saving custom NURBS controls as data.

Instead of requiring separate Maya scene files for every control, CVToolkit can store information about a curve, including:

- CV positions
- Degree
- Curve form
- Knot values
- Multiple curve shapes

That information can then be used to reconstruct the control inside Maya.

I use a similar preset idea for modeling landmarks, allowing selected polygon faces to be saved and reused later.

## Why I Made It

A lot of rigging involves small tasks that get repeated constantly: creating controls, changing their colors, scaling CVs, making offset groups, mirroring objects, and organizing controls.

I built CVToolkit as a way to put those operations into one interface while also giving myself a larger project for learning Maya Python and technical art.

It also gave me the opportunity to expand my original Landmark Tool into something that fits more naturally into my rigging workflow.

## Compatibility

CVToolkit was developed and tested in **Autodesk Maya 2025**.

Other Maya versions have not been fully tested, particularly versions that use different Python or Qt/PySide versions.

## Future Development

CVToolkit is still something I would like to continue developing. Some areas I would like to explore in future versions include:

- More rigging utilities
- Improved preset management
- Additional control shapes
- Better organization of the tool's internal modules
- More workflow automation

## Author

**Melodi Clark**

Technical Artist / Rigger