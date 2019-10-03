import time
from src.LinkedListCells import *

usersVideo = "D:/Ksu_Football_Tackle_Study/Online Repo/Football-Tackle-Study/data/Videos/7.MOD"

newCell = AddDatatoCells(usersVideo)
print("Identify the frame where the player has almost touch the bag.")
print("press SPACEBAR when found")
print("press SHIFT+D to skip 5 frames forwards")
print("press SHIFT+A to skip 5 frames backwards")
print("press D to move 1 frame forwards")
print("press A to move 1 frame backwards")
time.sleep(3)
cv2.imshow("First Image",newCell.Data)
key = cv2.waitKey(1)

while (key != ord("q")):

    if (key == ord("d")):
        cv2.destroyAllWindows()
        newCell = newCell.Next
        cv2.imshow("RIGHT", Resize(newCell.Data))

    if (key == ord("D")):
        cv2.destroyAllWindows()
        newCell = SkipFive(newCell)
        cv2.imshow("RIGHT", Resize(newCell.Data))

    if (key == ord("a")):
        cv2.destroyAllWindows()
        newCell = newCell.Prev
        cv2.imshow("LEFT", Resize(newCell.Data))

    if (key == ord("A")):
        cv2.destroyAllWindows()
        newCell = PrevFive(newCell)
        cv2.imshow("LEFT", Resize(newCell.Data))

    key = cv2.waitKey(1)
