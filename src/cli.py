#!/usr/bin/env python3
from .llm import get_models
from .settings.settings import set_property, get_property

import argparse
import ollama

def main():
    parser = argparse.ArgumentParser(description='LQA - Local Quick Assistant')

    group = parser.add_mutually_exclusive_group(required=True)

    group.add_argument('-m', '--model', help='Specify the LMM model to use')
    group.add_argument('--config', nargs=2, metavar=('OPTION', 'VALUE'), help='Set a configuration option')

    args = parser.parse_args()

    if args.config:
        if len(args.config) != 2:
            print('Invalid config option. Must specify both OPTION and VALUE.')
            return

        args.config[0] = args.config[0].strip().lower()

        if not get_property(args.config[0]):
            print(f'Invalid config option: {args.config[0].upper()}.')
            return

        args.config[1] = args.config[1].strip().lower()

        set_property(args.config[0], args.config[1])
        print(f'Set {args.config[0].upper()} to {args.config[1]}')
        return

    init_session(args.model.strip().lower())

def init_session(model):
    if not model:
        print('No model specified.')
        return

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