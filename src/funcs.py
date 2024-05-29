import json
import os


def get_data():
    with open(os.path.dirname(__file__) + '/../operations.json', 'r', encoding='utf8') as file:
        data_json = file.read()
        data = json.loads(data_json)

    return data


def get_time(operations):
    id_with_time = {}
    for each in operations:
        if "state" in each.keys():
            if each["state"] != "CANCELED":
                if len(each.keys()) != 0:
                    id_with_time[each["id"]] = each["date"][0:10]

    return id_with_time
