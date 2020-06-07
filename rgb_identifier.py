import cv2
import numpy as np
import pandas as pd
import argparse

#Creating argument parser to take image path from command line
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help="Image Path")
args = vars(ap.parse_args())
img_path = args['image']

#Reading the image with opencv
img = cv2.imread(img_path)

#declaring global variables (are used later on)
r = g = b = xpos = ypos = 0

#function to get a pixel location in image as input image will be plain in color so location does not matter
def draw_function(xpos,ypos):
    global b,g,r
    b,g,r = img[ypos,xpos]
    b = int(b)
    g = int(g)
    r = int(r)
       
cv2.namedWindow('image')
draw_function(10,10)

#Checking image to find out which RGB color it suits and printing the output color
cv2.imshow("image",img)
if b>g and b>r:
    print("BLUE")
elif g>b and g>r:
    print("GREEN")
else:
    print("RED") 
#Break the loop when user hits 'esc' key    
cv2.waitKey(900)

cv2.destroyAllWindows()