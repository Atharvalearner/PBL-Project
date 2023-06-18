import cv2
path=r"C:\Users\Shree\Documents\image.jpg"
image=cv2.imread(path)
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) 
(minVal,maxVal,minLoc,maxLoc)=cv2.minMaxLoc(gray)
cv2.circle(image,maxLoc,45,(255,255,255),10)
cv2.namedWindow("brightest spot",cv2.WINDOW_NORMAL)
cv2.resizeWindow("brightest spot",400,500) 
cv2.imshow("brightest spot",image)
cv2.waitkey(0) 
