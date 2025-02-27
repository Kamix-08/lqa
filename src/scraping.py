import pyautogui

def take_screenshot():
    image = pyautogui.screenshot("image.png")
    return image