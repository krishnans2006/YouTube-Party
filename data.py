import base64
import json
import os
from os import getenv

import firebase_admin
from dotenv import load_dotenv
from firebase_admin import credentials

load_dotenv()

h = base64.b64decode(os.getenv("creds"))
print(h)
cred = credentials.Certificate(json.loads(h))
firebase_admin.initialize_app(cred)


def d_get_room(code):
    return True
