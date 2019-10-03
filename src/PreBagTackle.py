import time
from src.UX import ShowLinkedCellsInstructions
from src.LinkedListCells import *

def FindPreBagTackle(Video):
    usersVideo = Video

    newCell = AddDatatoCells(usersVideo)
    ShowLinkedCellsInstructions()
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

        if (key ==ord(" ")):
            cv2.destroyAllWindows()
            return newCell

        key = cv2.waitKey(1)
