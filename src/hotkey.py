import keyboard
from .settings.settings import get_property
from .scraping import get_image_from_clipboard

def on_hk_1():
    get_image_from_clipboard()

keyboard.add_hotkey(hotkey=get_property('hotkey_1'), on_press=on_hk_1)