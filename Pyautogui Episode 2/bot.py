import pyautogui
import time
import random,pyscreeze
import PIL
pyscreeze.USE_IMAGE_NOT_FOUND_EXCEPTION = False

#https://pyautogui.readthedocs.io/en/latest/quickstart.html
#https://pyautogui.readthedocs.io/en/latest/keyboard.html
#https://github.com/asweigart/pyautogui/blob/master/pyautogui/__init__.py





def center_finder_region(path,confidence = 0.9,region= None):
    x, y = pyautogui.locateCenterOnScreen(f"{path}",confidence = confidence, region = region)
    return x,y


def center_finder(path,confidence = 0.9):

    x, y = pyautogui.locateCenterOnScreen(f"{path}",confidence = 0.9)

    return x,y

def prepration():

    x, y = center_finder("images/chrome_icon.png")
    pyautogui.click(x,y)

    time.sleep(1)

    x, y = center_finder("images/first_start.png")
    pyautogui.click(x,y)

    time.sleep(6.5)

    pyautogui.hotkey('pageup')
    time.sleep(2)
    x, y = center_finder("images/start.png")
    pyautogui.click(x,y)
    time.sleep(4.5)
    
# (left=536, top=421, width=830, height=218)
def click_on_RGBpixel(r_value,g_value,b_value,coords):
    pic = pyautogui.screenshot(region = coords)

    for x in range(0,coords[2],6):
        for y in range(0, coords[3],6):
            r,g,b = pic.getpixel((x,y))

            if r == r_value and g == g_value and b == b_value:
                pyautogui.click(x + coords[0],y + coords[1])
                break

btc= (255,153,49)
doge= (200,168,64)
blue1= (91,128,231)
blue2= (0,116,184)
gray= (141,141,141)

def play():
    scan = pyautogui.screenshot()
    RgbCheck = scan.getpixel((338, 48))

    values = [(btc),(doge),(blue1),(blue2),(gray)]

    while (PIL.ImageGrab.grab().load()[338, 48]==RgbCheck):
        
        for value in values:
            click_on_RGBpixel(value[0],value[1],value[2],(536,421,830,218))
        

#def play():
    #scan = pyautogui.screenshot()
    #RgbCheck = scan.getpixel((1251,279))

    #while (PIL.ImageGrab.grab().load()[1251, 279]==RgbCheck):

        #random_target_coins = random.choice(['1.PNG','2.PNG','3.PNG','4.PNG','5.PNG'])
        #try:

            #x, y = center_finder_region(f"images/{random_target_coins}",confidence = 0.6,region = (536,421,830,218))
            #pyautogui.click(x,y)

        #except:pass


def main():
    prepration()

    play()

if __name__ == "__main__":
    main()

    

    