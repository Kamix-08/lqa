from .settings.settings import get_property

import ollama

model = None

def set_model(_model):
    global model
    model = _model

def get_models() -> list[str]:
    models = ollama.list()
    models_names = []

    for model in models.__getitem__('models'):
        models_names.append(model.__getitem__('model'))

    return models_names

def strip_answer(answer:str) -> str:
    pattern = '</think>'
    return answer[answer.find(pattern)+len(pattern):]

def get_response(prompt: str) -> str:
    return ollama.chat(model=model, messages=[
        {"role": "system", "content": get_property('prompt')},
        {"role": "user", "content": prompt}
    ], stream=False)['message']['content']