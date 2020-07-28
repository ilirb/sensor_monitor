'''WIP'''

import sys
import json
import requests
import config
from config import log

PUSHBULLET_TOKEN=""
headers = {"Access-Token": PUSHBULLET_TOKEN}

r = requests.get(f"{config.PUSHBULLET_URI}/users/me", headers=headers)
if not r == 200:
    log.error(r.text)

class PushBullet(object):
    pass
