import json
import os

OUTPUT_FILE = "output.json"

def save_document(record):

    if os.path.exists(OUTPUT_FILE):
        with open(OUTPUT_FILE, "r") as f:
            data = json.load(f)
    else:
        data = []

    data.append(record)

    with open(OUTPUT_FILE, "w") as f:
        json.dump(data, f, indent=4)
