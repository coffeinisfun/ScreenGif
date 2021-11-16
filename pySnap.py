import pyautogui
import time
import datetime
from PIL import Image
import sys

def makeGif(frames, duration):
    frame_one = frames[0]
    name = time.strftime("%H%M%S",time.localtime()) + ".gif"

    frame_one.save(name, format="GIF", append_images=frames,
               save_all=True, duration=1000, loop=0)


def screenGif(interval, maxTime):
    now = 0
    screenshots = []

    while(now < maxTime):
        time.sleep(interval)
        now += interval
        screenshot = pyautogui.screenshot()
        screenshots.append(screenshot)
        print("snap @ " + datetime.datetime.now().strftime("%H-%M-%S"))

    makeGif(screenshots, 100*maxTime/interval)

if __name__ == '__main__':
    if len(sys.argv) > 2:
        screenGif(int(sys.argv[1]), int(sys.argv[2]))
    else:
        print("not enough parameters")
