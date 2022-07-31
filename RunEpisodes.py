import cv2
import time
import keyboard
import random
from utils.grabscreen import grab_screen
import pyautogui

# File for stats
f = open("stats.csv", "w")

time.sleep(5)
keyboard.press('space')
keyboard.release("space")

program_time = time.time()
episode_scores = []

# Enter number of episodes you want to run.
for i in range(5000):

    # Choose look ahead amount at random
    start_ahead = random.randint(33, 85)
    ahead = start_ahead

    # Choose amount of time before increasing look ahead.
    start_speedup = random.randint(100, 170)
    count = 0

    # Setting zero and white we will flip when game colors invert
    zero = 0
    white = 247

    # Starts game
    keyboard.press('space')
    time.sleep(2)
    keyboard.release("space")
    episode_start = time.time()
    start = time.time()

    # Bot rules you must update pixels!
    while True:
        last_time = time.time()
        image = grab_screen(region=(690, 250, 1035, 325))
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        (thresh, image) = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

        if image[74][105] == zero:
            ahead += 4
            holder = zero
            zero = white
            white = holder

        # Three cactus small
        if image[55][ahead] == zero or image[55][ahead - 1] == zero or image[55][ahead - 2] == zero:
            keyboard.release("down")
            keyboard.press("space")
            time.sleep(0.1)
            keyboard.release("space")
            im = pyautogui.screenshot()
            screen = im.getpixel((214,189))
            x1 = im.getpixel((920, 295))
            if screen[0] == 247:
                if x1[0] == 83:
                    keyboard.press("down")
                    time.sleep(0.2)
                    keyboard.release("down")


        # DUCK
        elif image[20][ahead] == zero:
            # print("down")
            keyboard.press("down")





        count += int(time.time() - start)

        if count > start_speedup:
            count = 0
            start = time.time()
            ahead += 3

            # Replay
            im = pyautogui.screenshot()
            screen = im.getpixel((917, 225))
            if screen[0] == 83:
                pyautogui.press('space')
                break

            else:
                pass
