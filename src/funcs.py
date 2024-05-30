import json
import os
from datetime import date


def get_data():
    """Получение информации из файла в формате json из директории проекта"""
    with open(os.path.dirname(__file__) + '/../operations.json', 'r', encoding='utf8') as file:
        data_json = file.read()
        data = json.loads(data_json)

    return data


def get_time(operations):
    """
    Из списка с данными получает словарь с айди в ключах и нужной частью даты операции,
    а также отсекает не проведенные операции
    """
    id_with_time = {}
    for each in operations:
        if "state" in each.keys():
            if each["state"] != "CANCELED":
                if len(each.keys()) != 0:
                    id_with_time[each["id"]] = each["date"][0:10]

    return id_with_time


def get_five_latest(operations):
    """
    Переводит даты в класс date, сортирует по ней список и возвращает последние 5 операций словарем с айди
    и датой форматом в соответствии с ТЗ
    """
    id_with_date = {}
    id_with_correct_date = []
    for k, v in operations.items():
        id_with_date[k] = date.fromisoformat(v)
    operations_with_date_sorted = dict(sorted(id_with_date.items(), key=lambda item: item[1], reverse=True))
    for k, v in operations_with_date_sorted.items():
        operations_with_date_sorted[k] = v.strftime('%d.%m.%Y')
    for k, v in operations_with_date_sorted.items():
        id_with_correct_date.append({'id': k, 'date': v})

    five_latest = id_with_correct_date[0:5]

    return five_latest


def get_payers_hidden(action_id, operations):
    """Получает id операции и возвращает данные о отправителе и получателе в соответствии с ТЗ"""
    for each in operations:
        if each['id'] == action_id:
            from_to = ''
            if 'from' in each.keys():
                from_ls = each['from'].split()
                for part in from_ls:
                    if part.isalpha():
                        from_to += part + ' '

                    elif len(part) == 16:
                        card_number = part[0:4] + ' ' + part[4:6] + '** ****' + ' ' + part[12:16]
                        from_to += card_number

                    else:
                        check_number = '**' + part[-4:]
                        from_to += check_number
            else:
                from_to += 'Новый счет'

            from_to += ' -> '

            if 'to' in each.keys():
                to_ls = each['to'].split()
                for part in to_ls:
                    if part.isalpha():
                        from_to += part + ' '

                    elif len(part) == 16:
                        card_number = part[0:4] + ' ' + part[4:6] + '** ****' + ' ' + part[12:16]
                        from_to += card_number

                    else:
                        check_number = '**' + part[-4:]
                        from_to += check_number

            return from_to


def check_operations(five_latest, operations):
    """Выводит информацию о поледних пяти операциях в нужном формате"""
    while len(five_latest) != 0:
        for operation in operations:
            if 'id' in operation.keys():
                if operation['id'] == five_latest[0]['id']:
                    from_to = get_payers_hidden(operation['id'], operations)
                    print(f"{five_latest[0]['date']} {operation['description']}\n{from_to}\n"
                          f"{operation["operationAmount"]["amount"]} "
                          f"{operation["operationAmount"]["currency"]["name"]}\n")

        five_latest.pop(0)
