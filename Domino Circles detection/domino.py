import cv2  
import numpy as np
points=0
def getcontours(img):
    global points ,real
    countours,herirarchy=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for cnt in countours :
        area=cv2.contourArea(cnt)
        print(area)
        cv2.drawContours(img,cnt,-1,(255,0,0),2)
        arc=cv2.arcLength(cnt,True)
        angles=cv2.approxPolyDP(cnt,0.033*arc,True)
        print(len(angles))
        x , y , w , h =cv2.boundingRect(angles)
        if len (angles) > 4:
            if abs(w-h)<20 :    
                cv2.circle(real,(int(x+(w/2)),int(y+(h/2))),5,(255,0,0),-1)
                points+=1                      

path="Resources/domino.jpg"
img=cv2.imread(path)
img=cv2.resize(img,(1024,700))
real=img.copy()
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img=cv2.GaussianBlur(img,(5,5),cv2.BORDER_CONSTANT)
cv2.threshold(img,145,255,cv2.THRESH_BINARY,img)
img=cv2.Canny(img,50,50)
img=cv2.dilate(img,(5,5),2)
img=cv2.erode(img,(7,7),5)
getcontours(img)
cv2.imshow("real",real)
cv2.imshow("img",img)
print(f"points={points}")
cv2.waitKey(0)


