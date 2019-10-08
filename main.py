from src.Helpers import *
import time
from src.UX import *
from src.MotionDetection import *
from src.PreBagTackleFinder import FindPreBagTackle
from src.LinkedListCells import *

'''Ask the user what video will be analyzed'''
# usersVideo = askVideoPath()
usersVideo = "D:/Ksu_Football_Tackle_Study/Online Repo/Football-Tackle-Study/data/Videos/1.mp4"
capture = cv2.VideoCapture(usersVideo)

'''Find the Perfect PreTackle Frame with LinkedListCell'''
PerfectFrame = FindPreBagTackle(usersVideo) #Hold onto the frame position
PerfectFramePosition = PerfectFrame.Position
ReleaseLinkedList(PerfectFrame)
print("The frame you have selected is the {0}th frame".format(PerfectFramePosition))

'''Ask the user what they want to see'''
showGrayScale = ShowGrayScaleMotion()
showContours = ShowContour()
showBoxes = ShowBox()
print(instructions())

'''Get two adjacent frames to make comparisons and identify motion'''
ret, frame1 = capture.read()
ret, frame2 = capture.read()

CellToBeAnalyzed = LinkedListCells()
count = 0

'''Show the user their specifications like showBoxes, showContours, and showGrayScale'''
while capture.isOpened():

    DifferenceInBothFrames = Diff(frame1,frame2)
    GrayedImage = ToGray(DifferenceInBothFrames)
    BlurredImage = ApplyGausBlur(GrayedImage)

    '''This is where the contours are found. Not sure how it happens'''
    _, thresh = cv2.threshold(BlurredImage, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    '''Go here for origional source:
     https://gist.github.com/pknowledge/623515e8ab35f1771ca2186630a13d14
    '''

    if(count == PerfectFramePosition):
        SaveContours(CellToBeAnalyzed, frame1, contours)


    '''Here the Contours are applied onto the 'frame1' and boxes are drawn (if desired) but no contours'''
    AddContours(contours,frame1,showBoxes)

    '''Here we are showing all of the images produced'''
    if(showBoxes):
        ShowBoxes(frame1)

    if(showGrayScale):
        ShowGray(GrayedImage)

    if(showContours):
        ShowContours(contours,frame1)

    frame1 = frame2
    ret, frame2 = capture.read()

    key = cv2.waitKey(1)

    if key == ord(" "):
        capture.release()
        break
    if key == ord("s"):
        time.sleep(5)

cv2.destroyAllWindows()
capture.release()

'''Now Assess the image '''

print("Cell to be analyzed info:\n", CellToBeAnalyzed.x , CellToBeAnalyzed.y , CellToBeAnalyzed.Position)

