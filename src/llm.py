import ollama

def get_models() -> list[str]:
    models = ollama.list()
    models_names = []

    for model in models.__getitem__('models'):
        models_names.append(model.__getitem__('model'))

    return models_names