import json
import os

config = {
    'hotkey_1': 'ctrl+alt+numpad 1'
}

def main():
    if not os.path.exists('data.json'):
        with open('data.json', 'w') as f:
            json.dump(config, f)