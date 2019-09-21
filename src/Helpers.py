import cv2
def Resize(Image):
    return cv2.resize(Image, (1080,720))

def ToGray(Image):
    return cv2.cvtColor(Image,cv2.COLOR_BGR2GRAY)

def AddContours(contours, frame1,showBoxes):
    for contour in contours:
        #prepare to create a box around the moving object
        (x, y, w, h) = cv2.boundingRect(contour)

        #if the total area is less than 100000 pixels^2, then go ahead and draw the box
        if (cv2.contourArea(contour) > 100000 and showBoxes ):
            cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)

def ShowContours(contours, frame1):
    cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)
    cv2.imshow("With Contours", Resize(frame1))

def ShowGray(image):
    cv2.imshow("GrayScale Motion",Resize(image))

def ShowOrig(image):
    cv2.imshow("Origional", Resize(image))

def ShowBoxes(image):
    cv2.imshow("With Bounding Boxes", Resize(image))

def ShowWithContours(image, contours):
    temp = image
    cv2.drawContours(temp,contours, -1,(0,255,0))
    cv2.imshow("With Contours", Resize(temp))

