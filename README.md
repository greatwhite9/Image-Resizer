# Image Resizer Application

## Overview
This application is a simple and user-friendly tool for resizing multiple images in batch mode. It provides a graphical user interface (GUI) to select image files, specify desired dimensions, and save resized images to a specified output folder.

## Files
1. **ImageResizerBatch.py**: The main Python script that contains the logic for the image resizing application.
2. **ImageResizerBatchExeUpdate.bat**: A batch file to convert the Python script (`ImageResizerBatch.py`) to an executable file (`.exe`).

## Requirements
- Python 3.x
- Required Python packages: `tkinter`, `opencv-python`

## How to Use

### Step 1: Convert the Python Script to an Executable
To convert the `ImageResizerBatch.py` script to an executable, follow these steps:

1. Ensure you have **PyInstaller** installed. If not, you can install it using:
   ```bash
   pip install pyinstaller
   ```

2. Run the `ImageResizerBatchExeUpdate.bat` file. This batch file contains the command to convert the Python script to an executable. 

The `ImageResizerBatchExeUpdate.bat` file should include a command similar to:
```batch
pyinstaller --onefile ImageResizerBatch.py
```
This command generates a `dist` folder containing the `ImageResizerBatch.exe` file.

### Step 2: Run the Application
To use the application, run the `.bat` file. This will open the GUI for the image resizer application.

### Using the GUI
1. **Select Images**: Click on the "Select Images" button to open a file dialog and select multiple image files.
2. **Select Output Folder**: After selecting the images, click on the "Select Output Folder" button to choose the folder where the resized images will be saved.
3. **Enter Dimensions**: You will be prompted to enter the desired height and width in centimeters. The application will convert these dimensions to pixels based on the DPI (dots per inch) setting.
4. **Resize Images**: The application will resize all selected images to the specified dimensions and save them in the chosen output folder.

### Restart Application
If you need to process another batch of images, the application will prompt you to restart, clearing the previously selected files and resetting the output folder.

## Example Workflow
1. Run the `ImageResizerBatchExeUpdate.bat` file to generate the executable.
2. Run the resulting `ImageResizerBatch.exe` file.
3. Use the GUI to select image files and the output folder.
4. Enter the desired dimensions for resizing.
5. The application will resize the images and save them to the specified folder.

### Additional Notes
- Ensure all selected files are valid image files to avoid errors.
- The default DPI is set to 150. You can modify this value in the script if needed.

## Contact
For any issues or further assistance, please contact the developer at [vallabhvij2003@gmail.com].
