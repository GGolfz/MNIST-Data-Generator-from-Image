from os import listdir, mkdir
import pandas as pd
import numpy as np
import cv2

img = cv2.imread("image.jpeg", cv2.IMREAD_GRAYSCALE)
print(img.shape)
box_size = 245
width = img.shape[1]
height = img.shape[0]
try:
    mkdir("data")
except:
    pass
for i in range(10):
    try:
        mkdir("data/" +str(i))
    except:
        pass
for i in range(0, height, box_size):
    num = 0
    count = len(listdir("data/" + str(num)))
    for j in range(0, width, box_size):
        if i + box_size < height and j + box_size < width:
            crop_img = img[i:i+box_size, j:j+box_size]
            crop_img[100 <= crop_img] = 255
            resized = cv2.resize(crop_img, (28,28), interpolation = cv2.INTER_AREA)
            cv2.imwrite("data/"+str(num)+"/image_" + str(count+1) + ".jpeg", resized)
            num += 1