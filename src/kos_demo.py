import random
from flask import Flask

app = Flask(__name__)

PERCENTAGE_WIN: float = 0.2


@app.route('/win')
def get_win_or_nowin(name: str) -> str:
    return 'win' if random.random() < PERCENTAGE_WIN else 'nowin'

@app.route('/liveness')
def liveness() -> str:
    return "OK"

