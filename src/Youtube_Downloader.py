from pytube import YouTube
import cv2
import os
#Desired Video to download from youtube
###url = 'https://www.youtube.com/watch?v=krSxqVgNZyo'
url = str(input("Enter YouTube url: \n"))

print("***Downloading Video***\n")

#Download Video from youtube
YouTube(url).streams.first().download('Youtube_Videos\\', filename='video1')
print("***Video successfully downloaded***")


