from inky.auto import auto
from flask import Flask
from clear import clear
from image import draw_image
from snap import draw_snapshot

inky = auto(ask_user=True, verbose=True)
app = Flask(__name__)


@app.route("/")
def home():
    return "<p>Ope, hey there!</p>"


# refresh will clear the screen
@app.route("/refresh")
def refresh():
    clear()
    return "<p>Hello, World!</p>"


# the web page that we are drawing
@app.route("/data")
def data():
    return "<p>Hello, World!</p>"


# this will be the trigger that causes a page rerender
@app.route("/draw")
def picture():
    draw_image()
    return "<p>The drawing process has begun.</p>"


# this will be the trigger that causes a page rerender
@app.route("/snap")
def snapshot():
    draw_snapshot()
    return "<p>The drawing process has begun.</p>"
