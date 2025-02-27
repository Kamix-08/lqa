import keyboard

from .settings.settings import get_property
from .scraping import take_screenshot
from .ocr import get_text
from .llm import get_response, strip_answer
from .output import output

def pipeline(image):
    text = get_text(image)
    answer = strip_answer(get_response(text))
    output(answer)

def on_hk_1():
    image = take_screenshot()
    pipeline(image)

keyboard.add_hotkey(hotkey=get_property('hotkey_1'), on_press=on_hk_1)