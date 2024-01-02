from tkinter import *
import tkinter.filedialog as filedialog
import tkinter.messagebox as tmsg
import cv2
import tkinter.simpledialog as sd
import os

file_path = None
output_path = None


def select_file():
    global file_path
    file_path = filedialog.askopenfilename(title="Open File") # Opening File Dialogue box to Select Image File
    if file_path != '':
        verify_image = cv2.imread(file_path, cv2.IMREAD_UNCHANGED)
        if verify_image is None:
            tmsg.showerror(title='Error', message="Select valid Image file.")
            return
        Button(root, text="Select Output Folder", command=output_folder).pack(pady=20) # Button to Select Output Folder


def output_folder():
    global output_path
    output_path = filedialog.askdirectory(title="Select folder") # Opening File Dialogue box to Select Output Folder location
    if output_path:
        height = sd.askinteger("Height", "Enter Height in pixels:") # Dialogue to Select new Height of the image
        width = sd.askinteger("Width", "Enter Width in pixels:") # Dialogue to Select new Width of the image
        if height and width:
            Resize(file_path, output_path, width, height) 


def Resize(input_image_path, output_folder_path, new_width, new_height):
    '''This function has the main logic of program.
       Here image gets resized into the new selected dimensions'''
    try:
        image = cv2.imread(input_image_path, cv2.IMREAD_UNCHANGED) # Loading image 

        # height, width = image.shape[:2]
        # if new_width > width or new_height > height:
        #     tmsg.showerror(title='Error', message="Invalid dimensions. Image cannot be up-scaled.")
        #     return

        resized_image = cv2.resize(image, (new_width, new_height)) # Ressize function of OpenCV
        base_name = os.path.splitext(os.path.basename(input_image_path))[0] # Taking name of the file
        name = input_image_path.split(".")
        extension = name[1] # Getting extenstion
        output_file_path = os.path.join(output_folder_path, f"{base_name}_resized.{extension}") # Saving file on output path with same name and extension but with specifying resized
        cv2.imwrite(output_file_path, resized_image)
        tmsg.showinfo(title='Saved', message=f"Your file is saved at {output_file_path}") # Pop up to tell user file is saved and telling him final save location

        global file_path, output_path
        file_path = None # Reseting File path 
        output_path = None # Reseting Output path

        root.destroy() # Destorying app window 
        start_application() # Reopening application 
    except Exception as e:
        tmsg.showerror(title='Error', message=str(e))


def start_application():
    global root
    root = Tk()
    root.geometry("663x333")
    root.title("Image Resizer")

    Label(root, text="Welcome to Image Resizer", font=("Times New Roman", 20, "bold")).pack()
    Label(root, text="Select File", pady=10).pack()
    Button(root, text="Select Image", command=select_file).pack() # Button to Select Image 

    root.mainloop()


# Start of application
start_application()
