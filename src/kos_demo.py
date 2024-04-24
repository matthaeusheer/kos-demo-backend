import random
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

PERCENTAGE_WIN: float = 0.2


@app.route('/win')
def get_win_or_nowin() -> str:
    return 'win' if random.random() < PERCENTAGE_WIN else 'nowin'

@app.route('/liveness')
def liveness() -> str:
    return "OK"

