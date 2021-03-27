from os import getenv
from dotenv import load_dotenv
import json
import os
import base64

import firebase_admin
from firebase_admin import credentials


load_dotenv()

h = base64.b64decode(os.getenv("creds"))
print(h)
cred = credentials.Certificate(json.loads(h))
firebase_admin.initialize_app(cred)

def d_get_room(code):
  return True