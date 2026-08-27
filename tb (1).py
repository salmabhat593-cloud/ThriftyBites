import json
import os

def log_user_intake(cart):
    filename = 'user_intake.json'
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            intake = json.load(f)
    else:
        intake = {}

    for item in cart:
        name = item['name']
        intake[name] = intake.get(name, 0) + 1

    with open(filename, 'w') as f:
        json.dump(intake, f)

def get_most_frequent_item():
    filename = 'user_intake.json'
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            intake = json.load(f)
        if intake:
            most_frequent = max(intake, key=intake.get)
            return most_frequent, intake[most_frequent]
    return None, 0