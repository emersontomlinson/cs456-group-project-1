import json
import os

PATH = "checkpoint.json"


def save(state):
    with open(PATH, "w") as f:
        json.dump(state, f)


def load():
    if os.path.exists(PATH):
        with open(PATH) as f:
            return json.load(f)
    return {"sessions": {}}
