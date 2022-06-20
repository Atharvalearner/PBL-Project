# PBL-Project
import cv2

# path of image
path=r"C:\Users\Shree\Documents\image.jpg"
# read image
image=cv2.imread(path)
# convert to black and white image
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) 
(minVal,maxVal,minLoc,maxLoc)=cv2.minMaxLoc(gray)
# for denoting circle,having parameters
cv2.circle(image,maxLoc,45,(255,255,255),10)
# output window name
cv2.namedWindow("brightest spot",cv2.WINDOW_NORMAL)
# for resize window co-ordinates
cv2.resizeWindow("brightest spot",400,500) 
# for showing output
cv2.imshow("brightest spot",image)
# for output window screen time
cv2.waitkey(0) 
