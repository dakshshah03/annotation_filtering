# import tkinter as tk
import numpy as np
import cv2
import os
from collections import namedtuple

image_dir = os.getcwd() + "/kitti/images/"    # relative directory to images
GT_dir = os.getcwd() + "/kitti/labels/"             # relative directory to ground truth data
HL_dir = os.getcwd() + "/original/"           # relative directory to predicted data
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
    x2 = int(coords[1])
    y1 = int(coords[2])
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
def validate_data(outfile, label, x1, y1, x2, y2):
    file = open(outfile)

def display_image(infile):
    GT_coords = []
    HL_coords = []
    false_positives = []
    no_break = False
    
    GT_file = open(GT_dir + infile + ".txt", "r")
    for x in GT_file:
        x = x.split(sep=" ")
        GT_coords.append(Coordinates(x[0], (float(x[4]), float(x[5]), float(x[6]), float(x[7]))))
    GT_file.close()
    
    HL_file = open(HL_dir + infile + ".txt", "r")
    for x in HL_file:
        no_break = False
        x = x.split(sep=" ")
        HL_coords.append(Coordinates(x[0], (float(x[4]), float(x[5]), float(x[6]), float(x[7]))))
        for gt in GT_coords:
            # if(gt.label == HL_coords[-1].label):
            # if it finds any gt box that overlaps, continues outer loop
            if(calculate_IoU(gt.coords, HL_coords[-1].coords) >= min_IoU_thres):
                no_break = True
                break
        if(not no_break):
           false_positives.append(HL_coords[-1])
    HL_file.close()
    print(len(false_positives))
    for x in false_positives:
        # opens image
        img = cv2.imread(image_dir + infile + '.png')
        print(img.shape)
        img_prototype = overlay_box(img, x.coords, HL_color)
        print(x.coords)
        cv2.imshow(image_dir + infile + ".png", img_prototype)
        if((cv2.waitKey(0) & 0xFF) == ord('q')):
            # if q, then approve
            # to do
            print("Approve")
            # `````````````````````` insert function call to validate_coordinate
            # cv2.destroyAllWindows()
        elif((cv2.waitKey(0) & 0xFF) == ord('e')):
            # if q, then deny
            print("Deny")
    cv2.destroyAllWindows()


if __name__ == '__main__':
    
    num_images = 500
    
    file = np.genfromtxt(HL_dir + image_name(1) + ".txt", delimiter=" ")
    # print(file)
    
    display_image(image_name(1))
    # window_name = image_name(1) + '.png'