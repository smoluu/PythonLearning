from PIL import Image, ImageGrab
import numpy as np
import cv2 as cv

class Bot:
    pass

def Update_screen():
    screenshot = ImageGrab.grab()
    screenshot = np.array(screenshot)
    screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2BGR)

    cv.imshow("computer vision",screenshot)
    cv.waitKey(0)

    



if __name__ == "__main__":
    Update_screen()