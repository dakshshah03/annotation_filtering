# import tkinter as tk
import numpy as np
import cv2
import os
from collections import namedtuple
import tkinter as tk
from PIL import Image, ImageTk

image_dir = os.path.expanduser('~') + "/annotation_filtering/kitti/images/"    # relative directory to images
GT_dir = os.path.expanduser('~') + "/annotation_filtering/kitti/labels/"             # relative directory to ground truth data
HL_dir = os.path.expanduser('~') + "/annotation_filtering/original/"           # relative directory to predicted data
validated_dir = os.path.expanduser('~') + "/annotation_filtering/validated_FP_data/"

GT_color = (255, 0, 0)          # ground truth box color
HL_color = (0, 0, 255)          # human label box color
min_IoU_thres = 0.5             # minumum IoU threshold
Detection = namedtuple("Detection", ["image_name", "label", "gt", "pred"])
Coordinates = namedtuple("Coordinates", ["label", "coords"])


def image_name(image_number):
    file_name = str(image_number)
    return (6 - len(file_name))* '0' + file_name

def overlay_box(img, coords, color):
    x1 = int(coords[0])
    y1 = int(coords[1])
    x2 = int(coords[2])
    y2 = int(coords[3])
    return cv2.rectangle(img, (x1, y1), (x2, y2), color=color, thickness=3)

def calculate_IoU(boxA, boxB):
    # Function taken from here:
    # https://pyimagesearch.com/2016/11/07/intersection-over-union-iou-for-object-detection/

    # determine the (x, y)-coordinates of the intersection rectangle
    xA = max(boxA[0], boxB[0])
    yA = max(boxA[1], boxB[1])
    xB = min(boxA[2], boxB[2])
    yB = min(boxA[3], boxB[3])
    # compute the area of intersection rectangle
    interArea = max(0, xB - xA + 1) * max(0, yB - yA + 1)
    # compute the area of both the prediction and ground-truth
    # rectangles
    boxAArea = (boxA[2] - boxA[0] + 1) * (boxA[3] - boxA[1] + 1)
    boxBArea = (boxB[2] - boxB[0] + 1) * (boxB[3] - boxB[1] + 1)
    # compute the intersection over union by taking the intersection
    # area and dividing it by the sum of prediction + ground-truth
    # areas - the interesection area
    iou = interArea / float(boxAArea + boxBArea - interArea)
    # return the intersection over union value
    return iou
    
# to do    

def display_image(infile):
    GT_coords = []
    HL_coords = []
    HL_info = []
    false_positives = []
    no_break = False
    
    GT_file = open(GT_dir + infile + ".txt", "r")
    for x in GT_file:
        x = x.split(sep=" ")
        GT_coords.append(Coordinates(x[0], (float(x[4]), float(x[5]), float(x[6]), float(x[7]))))
    GT_file.close()
    
    HL_file = open(HL_dir + infile + ".txt", "r")
    for n, x in enumerate(HL_file):
        no_break = False
        HL_info.append(x)
        x = x.split(sep=" ")
        HL_coords.append(Coordinates(x[0], (float(x[4]), float(x[5]), float(x[6]), float(x[7]))))
        for gt in GT_coords:
            # if(gt.label == HL_coords[-1].label):
            # if it finds any gt box that overlaps, continues outer loop
            if(calculate_IoU(gt.coords, HL_coords[-1].coords) >= min_IoU_thres):
                no_break = True
                break
        if(not no_break):
           false_positives.append((n, HL_coords[-1]))
    HL_file.close()
    
    # opens image
    img = cv2.imread(image_dir + infile + '.png')
    
    # opens file to write to
    outfile = open(validated_dir + infile + ".txt", "w")
    print(false_positives)
    for n, x in false_positives:
        img_prototype = cv2.cvtColor(overlay_box(img, x.coords, HL_color), cv2.COLOR_BGR2RGB)
        
        window = tk.Tk()
        window.title(image_dir + infile + ".png, " + str(n+1) + " of " + str(len(false_positives)))
        img_tk = ImageTk.PhotoImage(Image.fromarray(img_prototype))
        label_img = tk.Label(window, image=img_tk)
        label_img.pack()
        
        # Create buttons and place them below the image
        button1 = tk.Button(window,
                            text="Accept Label",
                            command=lambda: accept_button(outfile, n, HL_info, window))
        button1.pack(pady=10)  # Adjust the padding as needed

        button2 = tk.Button(window,
                            text="Reject Label",
                            command=lambda: reject_button(window))
        button2.pack(pady=10)  # Adjust the padding as needed
        
        # cv2.imshow(image_dir + infile + ".png", img_prototype)
        
        window.mainloop()
    
    outfile.close()

def reject_button(window):
    print("Rejected")
    window.destroy()
    
def accept_button(outfile, n, HL_info, window):
    validate_data(outfile, n, HL_info)
    print("Accepted")
    window.destroy()
    
def validate_data(outfile, n, HL_info):
    outfile.write(HL_info[n])

if __name__ == '__main__':
    
    num_images = 500
    
    display_image(image_name(8))