#https://gist.github.com/pknowledge/623515e8ab35f1771ca2186630a13d14
import cv2
import time


video_name = str(input("Enter video name "))
cap = cv2.VideoCapture(video_name) #'video1.mp4'

#get two adjacent frames to make comparisons and identify motion
ret, frame1 = cap.read()
ret, frame2 = cap.read()

while cap.isOpened():
    #find their differences and create an image out of that
    diff = cv2.absdiff(frame1, frame2)
    #Go grayscale with those differences
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    #Apply Gaussian Blur to smooth out the image
    blur = cv2.GaussianBlur(gray, (11 ,11), 0)
    #RESIZE AND SHOW THESE HUMUNGUS IMAGES
    # blurIMG = cv2.resize(blur,(1080,720))
    # cv2.imshow("blur",blurIMG)

#   Not sure what happens here
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # begin analyzing the multiple outlines withing the frame
    for contour in contours:
        #prepare to create a box around the moving object
        (x, y, w, h) = cv2.boundingRect(contour)

        #if the total area is less than 100000 pixels^2, then go ahead and draw the box
        if cv2.contourArea(contour) < 100000:
            continue
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)

    #This line can draw on the outlines
    # cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)

    image = cv2.resize(frame1, (1080,720))
    cv2.imshow("feed", image)
    frame1 = frame2
    ret, frame2 = cap.read()

    key = cv2.waitKey(1)

    #TO EXIT THE VIDEO
    if key == ord(" "):
        break

    #TO PAUSE THE VIDEO
    if key == ord("s"):
        time.sleep(45)
    time.sleep(.3)

cv2.destroyAllWindows()
cap.release()
