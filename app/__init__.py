import os
from flask import Flask

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(os.path.normpath(__file__ + '\\..'))

app = Flask(__name__)
from app import views

app.config.from_object(__name__)

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(ROOT_DIR, 'fyglex.db'),
    # SECRET_KEY='development key',
    # USERNAME='admin',
    # PASSWORD='default'
))
