from pytube import YouTube
import cv2
import os
#Desired Video to download from youtube
###url = 'https://www.youtube.com/watch?v=krSxqVgNZyo'
url = str(input("Enter YouTube url: \n"))

print("***Downloading Video***\n")

#Download Video from youtube
YouTube(url).streams.first().download('D:\\OpenCV\\Full Body Detection', filename='video1')
print("***Video successfully downloaded***")


# Function to extract frames
def FrameCapture(path):
    # Path to video file
    vidObj = cv2.VideoCapture(path)

    # Used as counter variable
    count = 1

    # checks whether frames were extracted
    success = 1

    num_images = get_num_Frames(path)

    The_Question = "About to produce {0} images. Would you like to continue? (y/n)".format(num_images)
    ask_user_to_cont = str(input(The_Question))
    print("***Converting frames into independent images***")

    while success:
        # vidObj object calls read
        # function extract frames
        success, image = vidObj.read()

        # Saves the frames with frame-count
        cv2.imwrite(os.path.join("Frames-Data","frame%d.jpg" % count), image)

        count += 1
    # print("***Process canceled***")

def get_num_Frames(path):
    vidObj = cv2.VideoCapture(path)

    (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
    vidObj.set(cv2.CAP_PROP_POS_AVI_RATIO, 1)
    seconds = vidObj.get(cv2.CAP_PROP_POS_MSEC) / 1000

    if int(major_ver)  < 3 :
        fps = vidObj.get(cv2.cv.CV_CAP_PROP_FPS)
        print("Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fps))
    else :
        fps = vidObj.get(cv2.CAP_PROP_FPS)
        print ("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))

    return seconds * fps

FrameCapture('video1.mp4')
