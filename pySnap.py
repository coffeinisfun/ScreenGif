import pyautogui
import time
import datetime
import sys

LENGTH_GIF = 20*1000  # in milliseconds


def make_gif(frames: [pyautogui.screenshot]):
    frame_one = frames[0]
    name = time.strftime("%H%M%S", time.localtime()) + ".gif"
    number_shots = len(frames)
    time_per_shot = LENGTH_GIF / number_shots
    # doc: https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#gif
    frame_one.save(name, format="GIF", append_images=frames, save_all=True, duration=time_per_shot, loop=0)


def screen_gif(interval, max_time):
    now = 0
    screenshots = []

    while now < max_time:
        time.sleep(interval)
        now += interval
        screenshot = pyautogui.screenshot()
        screenshots.append(screenshot)
        print("snap @ " + datetime.datetime.now().strftime("%H-%M-%S"))

    make_gif(screenshots)


if __name__ == '__main__':
    if len(sys.argv) > 2:
        screen_gif(int(sys.argv[1]), int(sys.argv[2]))
    else:
        print("not enough parameters\nfirst: interval between screenshots\nsecond: recording time")
