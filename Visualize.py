# import tkinter as tk
import numpy as np
import cv2
import os

def image_name(image_number):
    file_name = str(image_number)
    return (6 - len(file_name))* '0' + file_name + '.png'

def overlay_box(img, x1, y1, x2, y2, color):
    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)
    
    
    return cv2.rectangle(img, (x1, y1), (x2, y2), color=color, thickness=3)

def calculate_IOU(img, GT_coords, HL_coords, error = 5):
    # x coord 1 comparison
    if(np.abs(GT_coords[0][0] - HL_coords[0][0]) < error):
        pass
    pass
    # x coord 2 comparison
    # y coord 1 comparison
    # y coord 2 comparison

# def display_image(window_name, )



if __name__ == '__main__':
    image_dir = "/kitti/images/"
    GT_dir = "/labels/"
    HL_dir = "/original/"
    
    GT_color = (255, 0, 0) # ground truth box color
    HL_color = (0,0,255) # human label box color
    
    num_images = 500
    
    window_name = image_name(1)
    
    img = cv2.imread(os.getcwd() + image_dir + window_name)
    img_prototype = overlay_box(img, 599.41, 156.40, 629.75, 189.25, GT_color)
    cv2.imshow(window_name, img_prototype)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    