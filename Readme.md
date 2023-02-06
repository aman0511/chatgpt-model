# Chatgpt customized model

This repo is created to customize the model and retrain the model with provided input data
# Setup

## Update open api key

1. Crete `openaiapikey.txt` and store your api key
2. Create virtualenv `python -m venv venv`
3. Activate virtual env `source venv/bin/activate`
4. Install requirement `pip install -r requirements.txt`

## Fine tune 

`openai api fine_tunes.create -t "depression_prepared.jsonl"`

############# or

`python finetune.py`


# Run the chatbot

`python chatbot.py`





