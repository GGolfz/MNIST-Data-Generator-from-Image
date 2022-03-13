import os
import pandas as pd
import numpy as np
import cv2

img = cv2.imread("image-abc.jpeg", cv2.IMREAD_GRAYSCALE)
print(img.shape)
box_size = 148
width = img.shape[1]
height = img.shape[0]
try:
    os.makedirs("data",exist_ok=True)
except:
    pass
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in alphabet:
    os.makedirs("data/" + i,exist_ok=True)
    os.makedirs("data/" + i +"/upper",exist_ok=True)
    os.makedirs("data/" + i +"/lower",exist_ok=True)
print(width,height)
    
round = 0
for i in range(0, height, box_size):
    num = 0
    for j in range(0, width, box_size):
        print(num, round)
        letter = alphabet[num % 26]
        if i + box_size <= height and j + box_size <= width:
            crop_img = img[i:i+box_size, j:j+box_size]
            crop_img[100 <= crop_img] = 255
            resized = cv2.resize(crop_img, (100,100), interpolation = cv2.INTER_AREA)
            if round % 2 == 0:
                count = len(os.listdir("data/" + str(letter)+"/upper"))
                cv2.imwrite("data/"+str(letter)+"/upper/image_" + str(count+1) + ".jpeg", resized)
            else:
                count = len(os.listdir("data/" + str(letter)+"/lower"))
                cv2.imwrite("data/"+str(letter)+"/lower/image_" + str(count+1) + ".jpeg", resized)
            num += 1
    round += 1