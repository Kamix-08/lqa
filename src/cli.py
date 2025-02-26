#!/usr/bin/env python3
from .llm import get_models

import argparse
import ollama

def main():
    parser = argparse.ArgumentParser(description='LQA - Local Quick Assistant')
    parser.add_argument('-m', '--model', help='Specify the LMM model to use')

    args = parser.parse_args()

    init_session(args.model)

def init_session(model):
    models = get_models()

    if model not in models:
        print(f'Invalid model: {model}.\n\nAvailable models:\n\t{",\n\t".join(models)}\n')
        res = input(f'Pull {model}? (y/n): ').strip().lower()

        if res == 'y':
            try:
                ollama.pull(model)
            except:
                print(f'\nFailed to pull {model}.')
                return
        else: 
            return
        
    print(f'Initiating session: {model}')

    # test
    print(ollama.generate(model=model, prompt='Who are you?').__getitem__('response'))

if __name__ == '__main__':
    main()