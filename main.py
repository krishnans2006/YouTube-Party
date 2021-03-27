from flask import Flask, render_template, redirect, url_for, request, flash, session
from flask_socketio import SocketIO
from data import *

import random

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


# Generates Random 6 digit Room Code
def generateCode(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return random.randint(range_start, range_end)
# End

# Creates Room!


@app.route("/createroom", methods=['GET', 'POST'])
def create_room():
    if request.method == 'POST':
        username = request.form.get("username")
        code = generateCode(6)
        session['username'] = username
        # d_add_room(code=code, username=username)
        # You shouldn't need creator to redirect to room - that is only needed for database purposes
        return redirect(url_for("room", code=code))
    else:
        return render_template("createRoom.html")
    return render_template("createRoom.html")
# End


@app.route("/joinroom", methods=["GET", "POST"])
def join_room():
    if request.method == "POST":
        room_id = request.form.get("user_code")
        room_exists = d_get_room(room_id)
        if room_exists:
            if 'username' in session:
                flash(
                    f"You have successfully joined room {room_id}!", category="success")
            else:
                flash(f"You Have To Have A Username To Enter The Room",
                      category="error")
                render_template("make_username.html")
            return redirect(url_for("room"))
        else:
            flash(
                "This room code does not exist. Please use a valid room code!", category="error")
            return redirect(url_for("join_room"))
    return render_template("join_room.html")


@app.route("/makeusername", methods=['GET', 'POST'])
def username():
    if request.method == 'POST':
        if 'username' in session:
            flash("Username Already Made", category="error")
            return redirect(url_for("join_room"))
        else:
            username = request.form.get("username")
            session['username'] = username
            flash(f"Successfully Created Username", category="success")
            return redirect(url_for("join_room"))
    return render_template("make_username.html")


@app.route("/room/<code>", methods=["GET", "POST"])
def room(code=None):
    if not code:
        return redirect(url_for("join_room"))
    room_exists = d_get_room(code)
    if not room_exists:
        flash("This room code does not exist. Please use a valid room code!",
              category="error")
        return redirect(url_for("join_room"))
    # Some SOCKETIO stuff here:


@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    return render_template("register.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
