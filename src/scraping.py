import pyautogui

def take_screenshot(region: tuple[int, int, int, int] | None = None):
    image = pyautogui.screenshot("image.png", region=region)
    return image