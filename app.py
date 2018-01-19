import json
import os
import random
import sys
from urllib.parse import urlencode
from urllib.request import Request, urlopen

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
  lis = []
  breeds = (json.loads(urlopen('https://dog.ceo/api/breeds/list').read()))['message']
  if 'dog' in text:
    lis = [get_random('dog')]
  if 'cat' in text:
    lis = [get_random('cat')]
  if 'roll tide' in text:
    lis = ['Roll Tide!', 'RMFT!', 'RTR!', 'Roll Tide Roll!']
  else:
    for breed in breeds:
      if breed in text:
        lis = [get_random(breed)]
  return random.choice(lis)

# Send the chosen message to the chat
def send_message(msg):
  url  = 'https://api.groupme.com/v3/bots/post'
  data = {
          'bot_id' : os.getenv('GROUPME_BOT_ID'),
          'text'   : msg,
         }
  request = Request(url, urlencode(data).encode())
  json = urlopen(request).read().decode()
  
# Get random dog or cat
def get_random(switch):
  if (switch == 'dog'):
    link = 'https://dog.ceo/api/breeds/image/random'
    key = 'message'
  elif (switch == 'cat'):
    link = 'http://random.cat/meow'
    key = 'file'
  else: # breed
    link = 'https://dog.ceo/api/breed/' + switch + '/images/random'
    key = 'message'
  html = urlopen(link).read()
  data = json.loads(html)
  reto = data[key]
  # if (switch == 'cat' or switch == 'dog' switch == ''):
  reto.replace('\\/', '/')
  if reto.endswith('jpg') or reto.endswith('png') or reto.endswith('gif'):
    return reto
  else:
    return get_random(link)
  
# Debug
def log(msg):
  print(str(msg))
  sys.stdout.flush()
