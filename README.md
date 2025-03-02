# Local Quick Assist

![Static Badge](https://img.shields.io/badge/python-grey?style=for-the-badge&logo=python&logoColor=white)
![Static Badge](https://img.shields.io/badge/ollama-white?style=for-the-badge&logo=ollama&logoColor=black)
![Static Badge](https://img.shields.io/badge/tesseract_ocr-blue?style=for-the-badge&logo=google&logoColor=white)

---

**lqa** _(Local Quick Assist)_ is a tool which allows reading text from the screen with an OCR and then fetching it to a local LLM model.

## Installation

Requires [tesserocr](https://github.com/sirfz/tesserocr?tab=readme-ov-file#installation) and [ollama](https://ollama.com/download) to be installed.

Install the dependencies:

```bash
pip install -r requirements.txt
```

To install lqa, clone the repository and run the following command:

```bash
git clone https://github.com/Kamix-08/lqa
cd lqa
pip install -e .
```

Now you can run `lqa` from the terminal.

## Usage

```
usage: lqa [-h] (-m MODEL | --config OPTION VALUE)

LQA - Local Quick Assistant

options:
  -h, --help            show this help message and exit
  -m MODEL, --model MODEL
                        Specify the LMM model to use
  --config OPTION VALUE
                        Set a configuration option
```

Available configuration options:

| Option          | Description                                      | Default                                |
| --------------- | ------------------------------------------------ | -------------------------------------- |
| `hotkey_1`      | Capture the whole screen                         | `ctrl+shift+1`                         |
| `hotkey_2`      | Capture the region between last two mouse clicks | `ctrl+shift+2`                         |
| `show_thoughts` | Show the thought process of the LLM model        | `False`                                |
| `prompt`        | The system prompt for the LLM                    | _Available in the default JSON config_ |

## Examples

```bash
lqa -m deepseek-r1:14b
```

This will check for the DeepSeek-R1:14B model. If it doesn't exist, you will get prompted to pull it from Ollama.

```bash
lqa --config hotkey_1 ctrl+windows+0
```

This will change the hotkey to `ctrl+windows+0`. The config is being saved within the program.
