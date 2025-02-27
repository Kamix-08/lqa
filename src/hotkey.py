import keyboard

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

def main():
    print("Awaiting hotkeys.")
    keyboard.add_hotkey(get_property('hotkey_1'), callback=on_hk_1)