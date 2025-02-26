import json

config: dict | None = None

def load_config():
    global config
    if config is not None:
        return

    with open('data.json', 'r') as f:
        config = json.load(f)

def set_property(key:str, value:object):
    global config
    load_config()

    config[key] = value # type: ignore
    with open('data.json', 'w') as f:
        json.dump(config, f)

def get_property(key:str) -> object:
    load_config()

    if not config.__contains__(key): # type: ignore
        return None
    return config[key] # type: ignore