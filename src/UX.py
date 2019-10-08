def instructions():
    '''
    :return: A string for the user to read. Will provide instructions the user MUST know
    :rtype: String
    '''
    return ("Opening Video Player. It may be hiding (check taskbar) \nPress 'Spacebar' to exit video playback or 'S' to stop playback temporarily\n")

def askVideoPath():
    '''
    This will ask for the path and video name of the video the user want's to analyze
    :return: Video Path + Video Name
    :rtype: String
    '''
    return (str(input("Enter <video path/video name> ")))

def ShowContour():
    '''
    This will ask the user if they want to see the Contour picked up by the motion detection of their video
    :return: True or False
    :rtype: Bool
    '''
    reply = (str(input("Would you like to see the Contours of this video (Y/N): ")))
    if(reply.upper() == 'Y'):
        return True
    else:
        return False

def ShowGrayScaleMotion():
    '''
    This will ask the user if they want to see the Grayscale imagery picked up by the motion detection of their video
    :return: True or False
    :rtype: Bool
    '''
    reply = (str(input("Would you like to see the GrayScale Contours of this video? (Y/N): ")))
    if(reply.upper() == 'Y'):
        return True
    else:
        return False

def ShowBox():
    '''
    This will ask the user if they want to see the Bounding Boxes picked up by the motion detection of their video
    :return: True or False
    :rtype: Bool
    '''
    reply = (str(input("Would you like to see the Bounding Boxes found in this video? (Y/N): ")))
    if(reply.upper() == 'Y'):
        return True
    else:
        return False

def ShowLinkedCellsInstructions():
    print("Identify the frame where the player has almost touch the bag.")
    print("press SPACEBAR when found")
    print("press SHIFT+D to skip 5 frames forwards")
    print("press SHIFT+A to skip 5 frames backwards")
    print("press D to move 1 frame forwards")
    print("press A to move 1 frame backwards")
    print("Video Player may be hiding (check taskbar) ")
