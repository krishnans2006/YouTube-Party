import firebase_admin
from firebase_admin import credentials, firestore
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

url = f"https://api.jsonbin.io/v3/b/605e95589ab74a5f2bcc8065/latest"
headers = {
  "X-Master-Key": "$2b$10$UEHkkph26m8." + os.getenv("creds")
}

req = requests.get(url, json=None, headers=headers).json()
req = req["record"]
cred = credentials.Certificate(req)
firebase_admin.initialize_app(cred)
db = firestore.client()

def d_add_user(username, password):
  if db.collection("Users").document(username).get().exists:
    return False
  db.collection("Users").document(username).set(
    {
      "Password": password
    }
  )
  return True

def d_login(username, password):
  if not db.collection("Users").document(username).get().exists:
    return False
  if db.collection("Users").document(username).get({"Password"}).to_dict()["Password"] == password:
    return True
  return False

def d_get_room(code):
  code = str(code)
  if db.collection("Rooms").document(code).get().exists:
    return db.collection("Rooms").document(code).get().to_dict()
  return None

def d_add_room(code, username, video):
  code = str(code)
  if d_get_room(code):
    return False
  db.collection("Rooms").document(code).set(
    {
      "Video": video,
      "Host": db.document("Users/" + username)
    }
  )
  return True

def d_room_join(room, username):
  room = str(room)
  if not d_get_room(room):
    return False
  return True

def d_get_video(room):
  room = str(room)
  print(room)
  return "https://www.youtube.com/embed/" + db.collection("Rooms").document(room).get({"Video"}).to_dict()["Video"].split("=")[1] + "?enablejsapi=1"
