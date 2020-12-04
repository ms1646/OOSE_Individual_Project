import cv2
import numpy as np
import glob

videoframeSize = (500, 500)

output = cv2.VideoWriter('final_video.avi',cv2.VideoWriter_fourcc(*'DIVX'), 60, videoframeSize)

for each in glob.glob('/home/administrator/Desktop/opencv/images/*.jpg'):
    image = cv2.imread(each)
    output.write(image)

output.release()
