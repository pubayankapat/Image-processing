import numpy as np
import cv2 as cv
filepath="ImageProcessing/Ch3-images/brain.jpg"
img=cv.imread(filepath,0)
img2=img.copy().astype(np.float)
img2=img2/np.max(img2) # intensity normalization
img2=np.power(img2+1,2)
img2=255*(img2/np.max(img2))
img2=img2.astype(np.uint8)
imgs=np.hstack((img,img2))
cv.imshow("A)Image B)Image Gamma Transform",imgs)
cv.waitKey(0)