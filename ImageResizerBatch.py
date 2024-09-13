from tkinter import *
import tkinter.filedialog as filedialog
import tkinter.messagebox as tmsg
import cv2
import tkinter.simpledialog as sd
import os

file_paths = []  # List to store multiple file paths
output_path = None
DPI = 150  # You can change this depending on your use case, e.g., 300 for print


def cm_to_pixels(cm, dpi):
    return int(cm * dpi / 2.54)  # Converting cm to pixels using DPI


def select_files():
    global file_paths
    file_paths = filedialog.askopenfilenames(title="Open Files")  # Opening File Dialogue box to Select Multiple Image Files
    if file_paths:
        for file_path in file_paths:
            verify_image = cv2.imread(file_path, cv2.IMREAD_UNCHANGED)
            if verify_image is None:
                tmsg.showerror(title='Error', message="One or more selected files are not valid image files.")
                return
        Button(root, text="Select Output Folder", command=output_folder).pack(pady=20)  # Button to Select Output Folder


def output_folder():
    global output_path
    output_path = filedialog.askdirectory(title="Select folder")  # Opening File Dialogue box to Select Output Folder location
    if output_path:
        height_cm = sd.askfloat("Height", "Enter Height in centimeters:")  # Dialogue to Select new Height of the image
        width_cm = sd.askfloat("Width", "Enter Width in centimeters:")  # Dialogue to Select new Width of the image
        if height_cm and width_cm:
            height_px = cm_to_pixels(height_cm, DPI)
            width_px = cm_to_pixels(width_cm, DPI)
            for file_path in file_paths:
                Resize(file_path, output_path, width_px, height_px)
            tmsg.showinfo(title='Completed', message="Batch resizing completed successfully.")
            restart_application()  # Restarting application


def Resize(input_image_path, output_folder_path, new_width, new_height):
    '''This function has the main logic of program.
       Here image gets resized into the new selected dimensions'''
    try:
        image = cv2.imread(input_image_path, cv2.IMREAD_UNCHANGED)  # Loading image

        resized_image = cv2.resize(image, (new_width, new_height))  # Resize function of OpenCV
        base_name = os.path.splitext(os.path.basename(input_image_path))[0]  # Taking name of the file
        name = input_image_path.split(".")
        extension = name[1]  # Getting extension
        output_file_path = os.path.join(output_folder_path, f"{base_name}_resized.{extension}")  # Saving file on output path with same name and extension but with specifying resized
        cv2.imwrite(output_file_path, resized_image)
    except Exception as e:
        tmsg.showerror(title='Error', message=str(e))


def restart_application():
    global file_paths, output_path
    file_paths = []  # Resetting file paths
    output_path = None  # Resetting output path

    root.destroy()  # Destroying app window
    start_application()  # Reopening application


def start_application():
    global root
    root = Tk()
    root.geometry("663x333")
    root.title("Image Resizer")

    Label(root, text="Welcome to Image Resizer", font=("Times New Roman", 20, "bold")).pack()
    Label(root, text="Select Files", pady=10).pack()
    Button(root, text="Select Images", command=select_files).pack()  # Button to Select Images

    root.mainloop()


# Start of application
start_application()
