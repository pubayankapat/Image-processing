# Log Transformation
import cv2 as cv
import numpy as np
filepath="ImageProcessing/Ch3-images/nature.jpg"  # for log transform
img=cv.imread(filepath)

img2=img.copy()
img2=np.log2(img2)
img2=255*(img2/np.max(img2))
img2=img2.astype(np.uint8)

imgs=np.hstack((img,img2))
cv.imshow("A)Image B)Image Log Transform",imgs)
cv.waitKey(0)