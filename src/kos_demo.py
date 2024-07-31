import os
import random
from flask import Flask
from flask_cors import CORS
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
CORS(app)
metrics = PrometheusMetrics(app)

PERCENTAGE_WIN: float = 0.2
metrics.info("app_info", "Application info", version="1.0.3")


@app.route("/win")
def get_win_or_nowin() -> dict[str, str]:
    win_result = "win" if random.random() < PERCENTAGE_WIN else "nowin"
    additional_info = ""
    return {"win_result": win_result, "additional_info": additional_info}


@app.route("/liveness")
def liveness() -> str:
    return "OK"

