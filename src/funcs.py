import json
import os
from datetime import date


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


def get_five_latest(operations):
    id_with_date = {}
    id_with_correct_date = []
    for k, v in operations.items():
        id_with_date[k] = date.fromisoformat(v)
    operations_with_date_sorted = dict(sorted(id_with_date.items(), key=lambda item: item[1], reverse=True))
    for k, v in operations_with_date_sorted.items():
        operations_with_date_sorted[k] = v.strftime('%d.%m.%Y')
    for k, v in operations_with_date_sorted.items():
        id_with_correct_date.append({'id': k, 'data': v})

    five_latest = id_with_correct_date[0:5]

    return five_latest
