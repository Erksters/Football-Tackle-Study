import cv2
from src.Helpers import *

class LinkedListCells:
    # Create cell
    def __init__(self):
        self.Data = None
        self.Next = None
        self.Prev = None
        self.Position = None

def AddDatatoCells(Video):
    capture = cv2.VideoCapture(Video)
    CurrentCell = LinkedListCells()
    count = 0
    print("***** Creating Linked List of Cells *****")
    frames = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
    while (count < frames):
        print(count , "frame(s) loaded")
        what, small = capture.read()
        CurrentCell.Data = cv2.resize(small, (854, 480))
        CurrentCell.Position = count
        CurrentCell.Next = LinkedListCells()
        CurrentCell.Next.Prev = CurrentCell
        CurrentCell = CurrentCell.Next
        count = count + 1
    capture.release()

    print("*****Frames Done Loading*****\n\n")

    while(CurrentCell.Prev != None):
        CurrentCell = CurrentCell.Prev

    return CurrentCell

def SkipFive(LinkCell):
    for i in range(5):
        LinkCell = LinkCell.Next
    return LinkCell

def PrevFive(LinkCell):
    for i in range(5):
        LinkCell = LinkCell.Prev
    return LinkCell
