from src.funcs import *


data = get_data()

data_1 = [
  {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  },
  {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  }
]
data_2 = [
  {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  },
  {"date": "2019-07-03T18:35:29.512364", "description": "Перевод организации"}
]


id_with_time_1 = {441945886: "2019-08-26", 41428829: "2019-07-03"}
id_with_time_2 = {441945886: "2019-08-26", 414244455: "2022-03-06"}
id_with_time_3 = {441945886: "2019-08-26", 41428829: "2019-07-03", 1412123131: "1993-02-11", 1412122222: "2093-03-12",
                  141244444: "2022-05-15", 44194582323: "2001-02-23"}


def test_get_data():
    assert type(get_data()) == list


def test_get_time():
    assert get_time(data_1) == {441945886: "2019-08-26", 41428829: "2019-07-03"}
    assert get_time(data_2) == {441945886: "2019-08-26"}


def test_get_five_latest():
    assert get_five_latest(id_with_time_1) == [{'id': 441945886, 'date': '26.08.2019'}, {'id': 41428829,
                                                                                         'date': '03.07.2019'}]
    assert get_five_latest(id_with_time_2) == [{'id': 414244455, 'date': '06.03.2022'}, {'id': 441945886,
                                                                                         'date': '26.08.2019'}]
    assert get_five_latest(id_with_time_3) == [{'id': 1412122222, 'date': '12.03.2093'},
                                               {'id': 141244444, 'date': '15.05.2022'},
                                               {'id': 441945886, 'date': '26.08.2019'},
                                               {'id': 41428829, 'date': '03.07.2019'},
                                               {'id': 44194582323, 'date': '23.02.2001'}]


def test_get_payers_hidden():
    assert get_payers_hidden(441945886, data_1) == 'Maestro 1596 83** **** 5199 -> Счет **9589'
    assert get_payers_hidden(441945886, data) == 'Maestro 1596 83** **** 5199 -> Счет **9589'
    assert get_payers_hidden(716496732, data) == 'Visa Gold 5999 41** **** 6353 -> Счет **4472'
