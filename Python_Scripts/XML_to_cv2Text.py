from xml.dom import minidom
import os

Path_to_XML = str(input("Where are the XML files located?\n"))
Path_to_images = str(input("vWhere are the images located?\n"))
newFile = str(input("Enter the Name for the TextFile to be created:\n"))

def createTextFile(Final_Text, newName):
    f = open(newName, "w+")
    f.write(Final_Text)
    f.close()


Final_Text = ""
count_XML = 0
for filename in os.listdir(Path_to_XML):
    if filename.endswith(".xml"):
        doc = minidom.parse(Path_to_XML+"\\"+filename)
        object = doc.getElementsByTagName("object")
        for nodes in object:
            boundingbox = nodes.getElementsByTagName('bndbox')
            for values in boundingbox:  #there are four values that need to be read

                # This is the location of teh top left corner of the bounding box
                xmin_loc = values.getElementsByTagName('xmin')
                ymin_loc = values.getElementsByTagName('ymin')

                #This is the location of the bottom right corner of the boundig box
                xmax_loc = values.getElementsByTagName('xmax')
                ymax_loc = values.getElementsByTagName('ymax')

                #This is the boxes width and height
                boxwidth = eval( xmax_loc[0].childNodes[0].nodeValue + "-" + xmin_loc[0].childNodes[0].nodeValue)
                boxheight = eval( ymax_loc[0].childNodes[0].nodeValue + "-" + ymin_loc[0].childNodes[0].nodeValue)

                #Appending to the Final Text output after analyzing the
                Final_Text += Path_to_images +"/" + str(filename)+ " 1 " + str(xmin_loc[0].childNodes[0].nodeValue) + " " + str(ymin_loc[0].childNodes[0].nodeValue) + " " + str(boxwidth) + " " + str(boxheight) + "\n"

createTextFile(Final_Text,newFile)
