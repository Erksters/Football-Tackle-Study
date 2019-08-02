import cv2

video_name = str(input("Enter video name "))

body_cascade = cv2.CascadeClassifier("/opencv/sources/data/haarcascades/haarcascade_fullbody.xml")

video = cv2.VideoCapture(video_name) #'video1.mp4'

print("Creating window to view video and bounding boxes. If the window does not automatically pop up, it may be hiding behind another application")
# Capture frame-by-frame
print("press spacebar to exit the window")

while True:
    check, frame = video.read()
    # print(frame)
#convert video to Gray
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
#identifiy faces
    faces = body_cascade.detectMultiScale(gray)
#create rectangle and show image
    for x, y, w, h in faces:
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
#show image
    cv2.imshow('capturing',frame)

#Exit
    key = cv2.waitKey(1)

    if key == ord(" "):
        break

#Show Gray
    # time.sleep(3)
    # faces = body_cascade.detectMultiScale(gray,scaleFactor=1.05,minNeighbors=5)

video.release()
cv2.destroyAllWindows()



