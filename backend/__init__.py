from flask import Flask
from flask_socketio import SocketIO


app = Flask(__name__)
# Any object to be use by backend create here


socketio = SocketIO(app)

import backend.routes