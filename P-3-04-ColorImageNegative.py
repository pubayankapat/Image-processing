import cv2 as cv
import numpy as np
filepath="ImageProcessing/Ch3-images/nature.jpg"
img=cv.imread(filepath)
img2=255-img
imgs=np.hstack((img,img2))
cv.imshow("A)Image B)Negative",imgs)
cv.waitKey(0)