import keyboard
from pynput import mouse

from .settings.settings import get_property
from .scraping import take_screenshot
from .ocr import get_text, preprocess_image
from .llm import get_response, strip_answer
from .output import output

def pipeline(image):
    print("Detected hotkey.")
    text = get_text(preprocess_image(image))

    print("\nText detected:\n")
    print(text)

    answer = strip_answer(get_response(text))
    output(answer)

def on_hk_1():
    image = take_screenshot()
    pipeline(image)

def on_mouse(x,y,button,pressed):
    global coordinates
    if pressed:
        coordinates.append((x,y))

coordinates = []

def on_hk_2():
    if len(coordinates) < 2:
        return

    if coordinates[-1] < coordinates[-2]:
        coordinates[-2], coordinates[-1] = coordinates[-1], coordinates[-2]

    image = take_screenshot((min(coordinates[-2][0], coordinates[-1][0]), min(coordinates[-2][1], coordinates[-1][1]), 
                             abs(coordinates[-1][0] - coordinates[-2][0]), abs(coordinates[-1][1] - coordinates[-2][1])))
    pipeline(image)
    
    coordinates.clear()

def main():
    listener = mouse.Listener(on_click=on_mouse)
    listener.start()

    print("Awaiting hotkeys.")

    keyboard.add_hotkey(get_property('hotkey_1'), callback=on_hk_1)
    keyboard.add_hotkey(get_property('hotkey_2'), callback=on_hk_2)