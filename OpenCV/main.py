# windows only
from PIL import Image, ImageGrab
import numpy as np
import cv2 as cv
import time
from threading import Thread
import mss

class MainBot:
    def __init__(self) -> None:
        self.agents = []
        self.current_img = None #BGR
        self.current_imgHSV = None #HSV

def Update_screen(bot):
    time_start = time.time()
    while True:
        with mss.mss() as mss_instance:
            monitor_number = 2
            monitor_1 = mss_instance.monitors[monitor_number]
            bot.current_img = mss_instance.grab(monitor_1)
        # Convert to PIL.Image
        bot.current_img = Image.frombytes("RGB", bot.current_img.size, bot.current_img.bgra, "raw", "BGRX")
        bot.current_img = np.array(bot.current_img)
        bot.current_img = cv.cvtColor(bot.current_img, cv.COLOR_RGB2BGR)
        bot.current_imgHSV = cv.cvtColor(bot.current_img,cv.COLOR_BGR2HSV)
        cv.imshow("computer vision",bot.current_img)

        key = cv.waitKey(1)
        if key == ord("q"):
            break
        exec_time = time.time() - time_start
        print(f"fps({str(1 / (exec_time))})")
        time_start = time.time()
        

def print_menu():
    print("Enter command")
    print("S : Start the main bot")
    print("Q : Quit")


if __name__ == "__main__":
    bot = MainBot()

    print_menu()
    while True:
        u_input = input()
        u_input = str.lower(u_input).strip()
        
        if u_input == "s":
            Update_screen_thread = Thread(
                target=Update_screen,
                args=(bot,),
                name = "update screen thread",
                daemon=True)
            Update_screen_thread.start()

        if u_input == "q":
            break
        else:
            print("error")
            print_menu()

