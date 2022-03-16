from flask import Flask

# Super useful Flask tutorial:
# https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

app = Flask(__name__)
app.config['SECRET_KEY'] = "lmao try cracking this"

from app import routes

