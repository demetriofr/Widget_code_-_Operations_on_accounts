def get_date_in_formate_dd_mm_yyyy(date: str):
    """Извлечение и преобразование даты в формат ДД.ММ.ГГГГ"""
    date_ = date[:10].split('-')
    return f'{date_[2]}.{date_[1]}.{date_[0]}'


def disguise_card_number(card_number: str):
    """Маскировка номера карты в формате 0000 00** **** 0000"""
    return f'{card_number[0:4]} {card_number[4:6]}** **** {card_number[-4:]}'


def disguise_account_number(account_number: str):
    """Маскировка номер счёта в формате **0000"""
    return f'**{account_number[-4:]}'


def preparation_card_or_account_number(card_or_account_number: str):
    """Подготовка для вывода замаскированный карты или счёта"""
    number = card_or_account_number.split(" ")
    if number[0] == "Счет":
        return f'{number[0]} {disguise_account_number(number[1])}'
    elif number[1].isdigit():
        return f'{number[0]} {disguise_card_number(number[1])}'
    else:
        return f'{number[0]} {number[1]} {disguise_card_number(number[2])}'


def get_from_operation(from_):
    """Извлечение от кого операция"""
    if from_ is None:
        return f'Вклад'
    else:
        return preparation_card_or_account_number(from_)


def get_to_operation(to_):
    """Извлечение куда операция"""
    return preparation_card_or_account_number(to_)


def get_sort_date_operations(data_json):
    """Сортировка по дате"""
    data_json.sort(key=lambda x: x.get('date') or "", reverse=True)
    return data_json


def get_executed_operations(data_json):
    """Извлечение выполненных операций"""
    data_executed = [data_executed for data_executed in data_json if data_executed.get('state') == 'EXECUTED']
    return data_executed


def preparation_message(prepared_json: dict):
    """Подготовка вывода с сообщениями об операций"""

    date_ = get_date_in_formate_dd_mm_yyyy(prepared_json.get('date'))
    desc_ = prepared_json.get('description')
    from_ = get_from_operation(prepared_json.get('from'))
    to___ = get_to_operation(prepared_json.get('to'))

    amount_ = prepared_json.get('operationAmount').get('amount')
    curr___ = prepared_json.get('operationAmount').get('currency').get('name')

    return f'{date_} {desc_}\n{from_} -> {to___}\n{amount_} {curr___}\n'


def display_n_messages(executed_operations, n_messages=5):
    """Отображать n-ное количество сообщений, по-умолчанию 5"""

    list_messages = []

    for i in range(n_messages):
        list_messages.append(preparation_message(executed_operations[i]))

    return list_messages
