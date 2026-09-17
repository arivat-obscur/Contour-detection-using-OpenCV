import cv2 as cv
import numpy as np
img = cv.imread(r'C:\code\arrow.png', 1)
cv.imshow('image',img)
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
lp1 = np.array([0, 100, 100])
up1 = np.array([10, 255, 255])
lp2 = np.array([160, 100, 100])
up2 = np.array([179, 255, 255])
mask1 = cv.inRange(hsv, lp1, up1)
mask2 = cv.inRange(hsv, lp2, up2)
mask = cv.bitwise_or(mask1, mask2)
masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('works',masked)
# up=np.array([6,6,209])
# lp=np.array([3,3,138])
# mask=cv.inRange(HSV,lp,up)
# masked = cv.bitwise_and(img,img,mask=mask)
# cv.imshow('workpls',masked)
# cv.imshow("sds",masked)
contours , hierarchy = cv.findContours(mask, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(img,contours,-1,(0,255,0),2)
cv.imshow('drew',img)
print(f"{len(contours)} contours found")
cv.waitKey(0)
cv.destroyAllWindows


