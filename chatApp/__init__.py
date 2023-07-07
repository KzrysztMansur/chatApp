from flask import Flask, render_template, url_for
from flask_socketio import join_room, leave_room, send, SocketIO



app = Flask(__name__)
app.config["SECRET_KEY"] = 'EURIFQ3PRGU3V'
socketio = SocketIO(app)

from chatApp import routes


