from flask import render_template, send_from_directory, jsonify, request
from backend import app, socketio

# https://medium.com/@cabreraalex/svelte-js-flask-combining-svelte-with-a-simple-backend-server-d1bc46190ab9
# current_app.root_path is where is instantiated Flask App (lib/web/__init__.py!)
# Path for our main Svelte page
@app.route("/")
def base():
    print("fff")
    return send_from_directory('../frontend/public', 'index.html')



# Path for all the static files (compiled JS/CSS, etc.)
@app.route("/<path:path>")
def home(path):
    return send_from_directory('../frontend/public', path)


@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r
