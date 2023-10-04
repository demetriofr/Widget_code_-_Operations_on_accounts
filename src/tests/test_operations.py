from src.wg_operations_on_accounts.operations import *


def test_get_date_in_formate_dd_mm_yyyy():
    assert get_date_in_formate_dd_mm_yyyy("2018-03-23T10:45:06.972075") == "23.03.2018"


def test_disguise_card_number():
    assert disguise_card_number("7158300734726758") == "7158 30** **** 6758"


def test_disguise_account_number():
    assert disguise_account_number("35383033474447895560") == "**5560"


def test_preparation_card_or_account_number():
    assert get_from_operation("Maestro 1596837868705199") == "Maestro 1596 83** **** 5199"
    assert get_from_operation("Счет 75106830613657916952") == "Счет **6952"
    assert get_from_operation("Visa Classic 6831982476737658") == "Visa Classic 6831 98** **** 7658"


def test_get_from_operation():
    assert get_from_operation("Maestro 1596837868705199") == "Maestro 1596 83** **** 5199"
    assert get_from_operation("Счет 75106830613657916952") == "Счет **6952"
    assert get_from_operation("Visa Classic 6831982476737658") == "Visa Classic 6831 98** **** 7658"
    assert get_from_operation(None) == "Вклад"


def test_get_to_operation():
    assert get_from_operation("Maestro 1596837868705199") == "Maestro 1596 83** **** 5199"
    assert get_from_operation("Счет 75106830613657916952") == "Счет **6952"
    assert get_from_operation("Visa Classic 6831982476737658") == "Visa Classic 6831 98** **** 7658"


def test_get_sort_date_operations():
    before_sort = [
        {'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041',
         'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}},
         'description': 'Перевод организации', 'from': 'Maestro 1596837868705199', 'to': 'Счет 64686473678894779589'},
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364',
         'operationAmount': {'amount': '8221.37', 'currency': {'name': 'USD', 'code': 'USD'}},
         'description': 'Перевод организации', 'from': 'MasterCard 7158300734726758',
         'to': 'Счет 35383033474447895560'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572',
         'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}},
         'description': 'Перевод организации', 'from': 'Счет 75106830613657916952', 'to': 'Счет 11776614605963066702'},
        {'id': 587085106, 'state': 'EXECUTED', 'date': '2018-03-23T10:45:06.972075',
         'operationAmount': {'amount': '48223.05', 'currency': {'name': 'руб.', 'code': 'RUB'}},
         'description': 'Открытие вклада', 'to': 'Счет 41421565395219882431'},
        {'id': 142264268, 'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878',
         'operationAmount': {'amount': '79114.93', 'currency': {'name': 'USD', 'code': 'USD'}},
         'description': 'Перевод со счета на счет', 'from': 'Счет 19708645243227258542',
         'to': 'Счет 75651667383060284188'},
        {'id': 873106923, 'state': 'EXECUTED', 'date': '2019-03-23T01:09:46.296404',
         'operationAmount': {'amount': '43318.34', 'currency': {'name': 'руб.', 'code': 'RUB'}},
         'description': 'Перевод со счета на счет', 'from': 'Счет 44812258784861134719',
         'to': 'Счет 74489636417521191160'}
    ]

    after_sort = [
        {'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041',
         'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}},
         'description': 'Перевод организации', 'from': 'Maestro 1596837868705199', 'to': 'Счет 64686473678894779589'},
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364',
         'operationAmount': {'amount': '8221.37', 'currency': {'name': 'USD', 'code': 'USD'}},
         'description': 'Перевод организации', 'from': 'MasterCard 7158300734726758',
         'to': 'Счет 35383033474447895560'},
        {'id': 142264268, 'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878',
         'operationAmount': {'amount': '79114.93', 'currency': {'name': 'USD', 'code': 'USD'}},
         'description': 'Перевод со счета на счет', 'from': 'Счет 19708645243227258542',
         'to': 'Счет 75651667383060284188'},
        {'id': 873106923, 'state': 'EXECUTED', 'date': '2019-03-23T01:09:46.296404',
         'operationAmount': {'amount': '43318.34', 'currency': {'name': 'руб.', 'code': 'RUB'}},
         'description': 'Перевод со счета на счет', 'from': 'Счет 44812258784861134719',
         'to': 'Счет 74489636417521191160'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572',
         'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}},
         'description': 'Перевод организации', 'from': 'Счет 75106830613657916952', 'to': 'Счет 11776614605963066702'},
        {'id': 587085106, 'state': 'EXECUTED', 'date': '2018-03-23T10:45:06.972075',
         'operationAmount': {'amount': '48223.05', 'currency': {'name': 'руб.', 'code': 'RUB'}},
         'description': 'Открытие вклада', 'to': 'Счет 41421565395219882431'}
    ]
    assert get_sort_date_operations(before_sort) == after_sort


def test_get_executed_operations():
    before_ = [
        {'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041',
         'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}},
         'description': 'Перевод организации', 'from': 'Maestro 1596837868705199', 'to': 'Счет 64686473678894779589'},
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364',
         'operationAmount': {'amount': '8221.37', 'currency': {'name': 'USD', 'code': 'USD'}},
         'description': 'Перевод организации', 'from': 'MasterCard 7158300734726758',
         'to': 'Счет 35383033474447895560'},
        {'id': 142264268, 'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878',
         'operationAmount': {'amount': '79114.93', 'currency': {'name': 'USD', 'code': 'USD'}},
         'description': 'Перевод со счета на счет', 'from': 'Счет 19708645243227258542',
         'to': 'Счет 75651667383060284188'},
        {'id': 873106923, 'state': 'EXECUTED', 'date': '2019-03-23T01:09:46.296404',
         'operationAmount': {'amount': '43318.34', 'currency': {'name': 'руб.', 'code': 'RUB'}},
         'description': 'Перевод со счета на счет', 'from': 'Счет 44812258784861134719',
         'to': 'Счет 74489636417521191160'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572',
         'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}},
         'description': 'Перевод организации', 'from': 'Счет 75106830613657916952', 'to': 'Счет 11776614605963066702'},
        {'id': 587085106, 'state': 'EXECUTED', 'date': '2018-03-23T10:45:06.972075',
         'operationAmount': {'amount': '48223.05', 'currency': {'name': 'руб.', 'code': 'RUB'}},
         'description': 'Открытие вклада', 'to': 'Счет 41421565395219882431'},
        {'id': 476991061, 'state': 'CANCELED',
         'operationAmount': {'amount': '26971.25', 'currency': {'name': 'руб.', 'code': 'RUB'}},
         'date': '2018-11-23T17:47:33.127140', 'description': 'Перевод с карты на карту',
         'from': 'Visa Gold 7305799447374042', 'to': 'Maestro 3364923093037194'}
    ]

    after_ = [
        {'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041',
         'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}},
         'description': 'Перевод организации', 'from': 'Maestro 1596837868705199', 'to': 'Счет 64686473678894779589'},
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364',
         'operationAmount': {'amount': '8221.37', 'currency': {'name': 'USD', 'code': 'USD'}},
         'description': 'Перевод организации', 'from': 'MasterCard 7158300734726758',
         'to': 'Счет 35383033474447895560'},
        {'id': 142264268, 'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878',
         'operationAmount': {'amount': '79114.93', 'currency': {'name': 'USD', 'code': 'USD'}},
         'description': 'Перевод со счета на счет', 'from': 'Счет 19708645243227258542',
         'to': 'Счет 75651667383060284188'},
        {'id': 873106923, 'state': 'EXECUTED', 'date': '2019-03-23T01:09:46.296404',
         'operationAmount': {'amount': '43318.34', 'currency': {'name': 'руб.', 'code': 'RUB'}},
         'description': 'Перевод со счета на счет', 'from': 'Счет 44812258784861134719',
         'to': 'Счет 74489636417521191160'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572',
         'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}},
         'description': 'Перевод организации', 'from': 'Счет 75106830613657916952', 'to': 'Счет 11776614605963066702'},
        {'id': 587085106, 'state': 'EXECUTED', 'date': '2018-03-23T10:45:06.972075',
         'operationAmount': {'amount': '48223.05', 'currency': {'name': 'руб.', 'code': 'RUB'}},
         'description': 'Открытие вклада', 'to': 'Счет 41421565395219882431'}
    ]

    assert get_executed_operations(before_) == after_


def test_preparation_message():
    before_ = {
        'id': 863064926, 'state': 'EXECUTED', 'date': '2019-12-08T22:46:21.935582',
        'operationAmount': {'amount': '41096.24', 'currency': {'name': 'USD', 'code': 'USD'}},
        'description': 'Открытие вклада', 'to': 'Счет 90424923579946435907'
    }

    after_ = '08.12.2019 Открытие вклада\nВклад -> Счет **5907\n41096.24 USD\n'

    assert preparation_message(before_) == after_


def test_display_n_messages():
    before_ = [
        {'id': 863064926, 'state': 'EXECUTED', 'date': '2019-12-08T22:46:21.935582',
         'operationAmount': {'amount': '41096.24', 'currency': {'name': 'USD', 'code': 'USD'}},
         'description': 'Открытие вклада', 'to': 'Счет 90424923579946435907'},
        {'id': 114832369, 'state': 'EXECUTED', 'date': '2019-12-07T06:17:14.634890',
         'operationAmount': {'amount': '48150.39', 'currency': {'name': 'USD', 'code': 'USD'}},
         'description': 'Перевод организации', 'from': 'Visa Classic 2842878893689012',
         'to': 'Счет 35158586384610753655'},
        {'id': 154927927, 'state': 'EXECUTED', 'date': '2019-11-19T09:22:25.899614',
         'operationAmount': {'amount': '30153.72', 'currency': {'name': 'руб.', 'code': 'RUB'}},
         'description': 'Перевод организации', 'from': 'Maestro 7810846596785568', 'to': 'Счет 43241152692663622869'},
        {'id': 482520625, 'state': 'EXECUTED', 'date': '2019-11-13T17:38:04.800051',
         'operationAmount': {'amount': '62814.53', 'currency': {'name': 'руб.', 'code': 'RUB'}},
         'description': 'Перевод со счета на счет', 'from': 'Счет 38611439522855669794',
         'to': 'Счет 46765464282437878125'},
        {'id': 801684332, 'state': 'EXECUTED', 'date': '2019-11-05T12:04:13.781725',
         'operationAmount': {'amount': '21344.35', 'currency': {'name': 'руб.', 'code': 'RUB'}},
         'description': 'Открытие вклада', 'to': 'Счет 77613226829885488381'},
        {'id': 509645757, 'state': 'EXECUTED', 'date': '2019-10-30T01:49:52.939296',
         'operationAmount': {'amount': '23036.03', 'currency': {'name': 'руб.', 'code': 'RUB'}},
         'description': 'Перевод с карты на счет', 'from': 'Visa Gold 7756673469642839',
         'to': 'Счет 48943806953649539453'}
    ]

    after_ = [
        '08.12.2019 Открытие вклада\nВклад -> Счет **5907\n41096.24 USD\n',
        '07.12.2019 Перевод организации\nVisa Classic 2842 87** **** 9012 -> Счет **3655\n48150.39 USD\n',
        '19.11.2019 Перевод организации\nMaestro 7810 84** **** 5568 -> Счет **2869\n30153.72 руб.\n',
        '13.11.2019 Перевод со счета на счет\nСчет **9794 -> Счет **8125\n62814.53 руб.\n',
        '05.11.2019 Открытие вклада\nВклад -> Счет **8381\n21344.35 руб.\n',
    ]

    assert display_n_messages(before_) == after_
