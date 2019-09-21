def instructions():
    '''
    :return: A string for the user to read. Will provide instructions the user MUST know
    :rtype: String
    '''
    return ("Opening Video Player. It may be hiding (check taskbar) \nPress 'Spacebar' to exit video playback or 'S' to stop playback temporarily")

def askVideoPath():
    '''
    This will ask for the path and video name of the video the user want's to specify
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
