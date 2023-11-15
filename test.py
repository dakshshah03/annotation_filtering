import cv2
import tkinter as tk
from PIL import Image, ImageTk
import os

def on_button1_click():
    print("Button 1 clicked")

def on_button2_click():
    print("Button 2 clicked")

# Load an example image using OpenCV
image_path = os.getcwd() + "/kitti/images/000001.png"
img_cv2 = cv2.imread(image_path)
img_rgb = cv2.cvtColor(img_cv2, cv2.COLOR_BGR2RGB)

# Create a Tkinter window
root = tk.Tk()
root.title("OpenCV Image with Buttons")

# Convert the OpenCV image to a Tkinter PhotoImage
img_tk = ImageTk.PhotoImage(Image.fromarray(img_rgb))

# Create a label to display the image
label_img = tk.Label(root, image=img_tk)
label_img.pack()

# Create buttons and place them below the image
button1 = tk.Button(root, text="Button 1", command=on_button1_click)
button1.pack(pady=10)  # Adjust the padding as needed

button2 = tk.Button(root, text="Button 2", command=on_button2_click)
button2.pack(pady=10)  # Adjust the padding as needed

# Run the Tkinter main loop
root.mainloop()
