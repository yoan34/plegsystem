import json
import urllib.request
from pprint import pprint

def request(action, **params):
    return {'action': action, 'params': params, 'version': 6}

def invoke(action, **params):
    requestJson = json.dumps(request(action, **params)).encode('utf-8')
    response = json.load(urllib.request.urlopen(urllib.request.Request('http://127.0.0.1:8765', requestJson)))
    if len(response) != 2:
        raise Exception('response has an unexpected number of fields')
    if 'error' not in response:
        raise Exception('response is missing required error field')
    if 'result' not in response:
        raise Exception('response is missing required result field')
    if response['error'] is not None:
        raise Exception(response['error'])
    return response['result']

decknames = invoke('deckNames')
deck_plegsystem = []
for deckname in decknames:
    if "plegsysteme" in deckname and "::" in deckname:
        deck_plegsystem.append(deckname.split('::')[1])
        

data = {}
for deckname in deck_plegsystem:
    if deckname not in data:
        data[deckname] = {}
    cards = invoke('findCards', query=f'deck:plegsysteme::{deckname}')
    cards = invoke("cardsInfo", cards=cards)
    for card in cards:
        front = card["fields"]["Front"]["value"]
        if "objectBox-string" in front:
            front = front.split('objectBox-string">')[1]
            front = front.split('</span></span></span></span>')[0]
            if "<br>" in front:
                front = front.split('<br>')[0]
        if "<br>" in front:
            front = front.split('<br>')[0]
        if "[sound:ank" in front:
            front = front.split("[sound:ank")[0]
        back = card["fields"]["Back"]["value"]
        if "objectBox-string" in back:
            back = back.split('objectBox-string">')[1]
            back = back.split('</span></span></span></span>')[0]
        if "<br>" in back:
            back = back.split("<br>")[0]
        if "[sound:ank" in back:
            back = back.split("[sound:ank")[0]
        
        try:
            int(front)
            if "-" in back and back not in ["jean-francois", "jean-louis", "t-shirt", "new-york", "talkie-walkie"]:
                back = back.split('-')[0]
            data[deckname][front] = back
        except Exception:
            pass


pprint(data)


import json
with open("data.json", "w") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
    