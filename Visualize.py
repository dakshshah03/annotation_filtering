# import tkinter as tk
import numpy as np
import cv2
import os
from collections import namedtuple

image_dir = "/kitti/images/"    # relative directory to images
GT_dir = "/labels/"             # relative directory to ground truth data
HL_dir = "/original/"           # relative directory to predicted data
GT_color = (255, 0, 0)          # ground truth box color
HL_color = (0, 0, 255)          # human label box color
min_IoU_thres = 0.5             # minumum IoU threshold
Detection = namedtuple("Detection", ["image_name", "label", "gt", "pred"])
Coordinates = namedtuple("Coordinates", ["label", "coords"])


def image_name(image_number):
    file_name = str(image_number)
    return (6 - len(file_name))* '0' + file_name

def overlay_box(img, x1, y1, x2, y2, color):
    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)
    
    
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
    

def validate_data(outfile, label, x1, y1, x2, y2):
    file = open(outfile)

def display_image(infile, image_dir, GT_dir, HL_dir):
    GT_coords = []
    HL_coords = []
    false_positives = []
    
    GT_file = open(GT_dir + infile + ".txt", "r")
    for x in GT_file:
        x = x.split(sep=" ")
        GT_coords.append(Coordinates(x[0], (x[4], x[5], x[6], x[7])))
    GT_file.close()
    
    HL_file = open(HL_dir + infile + ".txt", "r")
    for x in HL_file:
        x = x.split(sep=" ")
        HL_coords.append(Coordinates(x[0], (x[4], x[5], x[6], x[7])))
        for e in GT_coords:
            if(e.label == x[0]):            
                if(calculate_IoU(e.))
    HL_file.close()
    
    for HL in HL_coords:
        for 
        if(calculate_IoU)
    
    # opens image
    img = cv2.imread(os.getcwd() + image_dir + infile + '.png')
    
    img_prototype = overlay_box(img, 599.41, 156.40, 629.75, 189.25, GT_color)
    cv2.imshow(window_name, img_prototype)
    if((cv2.waitkey(1) & 0xFF) == ord('q')):
        # if q, then approve
        # `````````````````````` insert function call to validate_coordinate
        cv2.destroyAllWindows()
    elif((cv2.waitkey(1) & 0xFF) == ord('e')):
        # if q, then deny
        cv2.destroyAllWindows()


if __name__ == '__main__':
    
    num_images = 500
    
    file = np.genfromtxt(os.getcwd() + HL_dir + image_name(1) + ".txt", delimiter=" ")
    # print(file)
    
    display_image(image_name(1), image_dir, GT_dir, HL_dir)
    # window_name = image_name(1) + '.png'
    
    
    
        
    
# class ImageStruct:
#     def __init__(self, img, labels, GT_coords, HL_coords):
#         self.img = img;             # image array
#         self.GT_coords = GT_coords  # array of GT coordinates
#         self.HL_coords = HL_coords  # array of HL coordinates
#         self.labels = labels        # array of labels
        
# class LabelStruct:
#     def __init__(self, label, x1, y1, x2, y2):
#         self.label = label
#         self.x1 = x1
#         self.y1 = y1
#         self.x2 = x2
#         self.y2 = y2