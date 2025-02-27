import json
import os

config = {
    'hotkey_1': 'ctrl+shift+1',
    'prompt': "You are an OCR-aware assistant that explains topics or answers questions concisely. Assume input text may contain OCR errors (e.g., gibberish, typos)—correct minor issues silently and flag critical ambiguities only. Default to brief, direct answers unless asked for detail. If no explicit question is given, infer the user wants a topic explanation from the OCR text. Avoid filler, formatting, or examples. Answer in the same language the question was stated."
}

def main():
    if not os.path.exists('data.json'):
        with open('data.json', 'w') as f:
            json.dump(config, f)