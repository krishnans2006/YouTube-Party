from flask import Flask, render_template, redirect, url_for, request, flash, session
from flask_socketio import SocketIO
from flask_socketio import send, emit, join_room, leave_room
from data import *

import random

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
socketio = SocketIO(app, cors_allowed_origins="*")


#Generates Random 6 digit Room Code
def generateCode(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return random.randint(range_start, range_end)
# End

@socketio.on('joined', namespace='/room')
def joined(message):
    """Sent by clients when they enter a room.
    A status message is broadcast to all people in the room."""
    room = session.get('room')
    join_room(room)
    print("Joined!!!")
    emit('status', {'msg': session.get('username') + ' has entered the room.'}, room=room)


@socketio.on('text', namespace='/room')
def text(message):    
    """Sent by a client when the user entered a new message.
    The message is sent to all people in the room."""
    room = session.get('room')
    print("Message!!!", message)
    emit('message', {'msg': session.get('username') + ':' + message['msg']}, room=room)


@socketio.on('left', namespace='/room')
def left(message):
    """Sent by clients when they leave a room.
    A status message is broadcast to all people in the room."""
    room = session.get('room')
    leave_room(room)
    print("Left :( :( :(")
    emit('status', {'msg': session.get('username') + ' has left the room.'}, room=room)


@app.route("/", methods=["GET", "POST"])
def index():
  if request.method == "POST":
    if not session.get("username"):
      flash("You are not logged in!", category="error")
      return redirect(url_for("login"))
    video = request.form.get("video")
    code = request.form.get("code")
    if video and code:
      flash("You can't create and join a room!", category="error")
      return redirect(url_for("index"))
    if video:
      code = generateCode(6)
      while not d_add_room(code, session["username"], video):
        code = generateCode(6)
      flash("Your Room was successfully created!", category="success")
      return redirect(url_for("room_view", code=code))
    elif code:
      room_exists = d_get_room(code)
      if room_exists:
        flash("You have successfully joined the room!", category="success")
        return redirect(url_for("room_view", code=code))
      flash("This room code does not exist. Please use a valid room code!", category="error")
      return redirect(url_for("index"))
  return render_template("index.html")


@app.route("/room/<code>", methods=["GET", "POST"])
def room_view(code=None):
  if not session.get("username"):
    flash("You are not logged in!", category="success")
    return redirect(url_for("login"))
  if not code:
    flash("This code could not be found! Please check your code.", category="error")
    return redirect(url_for("index"))
  room_exists = d_get_room(code)
  if not room_exists:
    flash("This room code does not exist. Please use a valid room code!", category="error")
    return redirect(url_for("index"))
  session["room"] = code
  return render_template("room.html", name=d_get_room(code)["Host"].id, room=code, video=d_get_video(code))


@app.route("/register", methods= ["GET", "POST"])
def register():
  if session.get("username"):
    flash("You are already logged in!", category="success")
  if request.method == "POST":
    username = request.form.get("username")
    password = request.form.get("password")
    if d_add_user(username, password):
      flash("Successfully registered!", category="success")
      session["username"] = username
      return redirect(url_for("index"))
    else:
      flash("This Username already exists! Please choose another username.", category="error")
      return redirect(url_for("login"))
  return render_template("register.html")


@app.route("/login", methods= ["GET", "POST"])
def login():
  if session.get("username"):
    flash("You are already logged in!", category="success")
  if request.method == "POST":
    username = request.form.get("username")
    password = request.form.get("password")
    if d_login(username, password):
      flash("You have been successfully logged in!", category="success")
      session["username"] = username
      return redirect(url_for("index"))
    else:
      flash("Invalid Username or Password!", category="error")
      return redirect(url_for("login"))
  return render_template("login.html")

@app.route("/logout")
def logout():
  if not session.get("username"):
    flash("You are not logged in!", category="error")
  session.clear()
  return redirect(url_for("login"))


if __name__ == "__main__":
  socketio.run(app, host="0.0.0.0", debug=True)
