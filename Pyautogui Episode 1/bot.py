import pyautogui
import time


#https://pyautogui.readthedocs.io/en/latest/quickstart.html


def center_finder(path,confidence = 0.9):

    x, y = pyautogui.locateCenterOnScreen(f"{path}",confidence = 0.9)

    return x,y

def main():

    x, y = center_finder("images/chrome_icon.png")
    pyautogui.click(x,y)

    time.sleep(1)

    x, y = center_finder("images/first_start.png")
    pyautogui.click(x,y)

    time.sleep(3)

    x, y = center_finder("images/start.png")
    pyautogui.click(x,y)

if __name__ == "__main__":
    main()
    