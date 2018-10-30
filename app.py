import json
import os
import random
import sys

import requests

import xmltodict
from flask import Flask, request

app = Flask(__name__)

# Webhook for all requests
@app.route('/', methods=['POST'])
def webhook():
  data = request.get_json()
  log('Recieved {}'.format(data))
  
  msg = ''
  if data['name'] != os.getenv('BOT_NAME'):
    msg = get_res(data['text'].lower())
  send_message(msg)
  return "ok", 200

# Choose response based on keywords
def get_res(text):
  if 'mad' in text:
    return 'Jonathan, calm down!'

# Debug
def log(msg):
  print(str(msg))
  sys.stdout.flush()
