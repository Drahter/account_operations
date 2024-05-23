import json
import os


def get_data():
    with open(os.path.dirname(__file__) + '/../operations.json', 'r', encoding='utf8') as file:
        data_json = file.read()
        data = json.loads(data_json)

    return data
