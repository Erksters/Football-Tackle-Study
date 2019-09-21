
def askVideoPath():
    return (str(input("Enter video name ")))

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
