from json import load, loads
from pathlib import Path, PurePath
from zipfile import ZipFile


def get_path_to_operations_zip(zip_name):
    """Получает путь к архиву данных с операциями"""

    this_file_path = Path(__file__)
    path_to_this_project = PurePath(this_file_path).parents[2]
    path_to_operations = Path(path_to_this_project, "data", zip_name)

    return path_to_operations


def get_json_from_zip(zip_name, json_name):
    """Получение JSON файла с операциями из zip архива"""

    # Открытие zip архива
    with ZipFile(get_path_to_operations_zip(zip_name), 'r') as operations_zip:
        with operations_zip.open(json_name) as operations_json:

            # Получение данных из JSON
            operations = loads(operations_json.read().decode("utf-8"))

            return operations


def get_path_to_operations_json(json_name):
    """Получает путь к JSON с операциями"""

    this_file_path = Path(__file__)
    path_to_this_project = PurePath(this_file_path).parents[2]
    path_to_operations = Path(path_to_this_project, "data", json_name)

    return path_to_operations


def get_json(json_name):
    """Получить JSON"""

    # Получение данных из JSON
    with open(get_path_to_operations_json(json_name), "r", encoding='utf-8') as operations_json:
        operations = load(operations_json)

    return operations


def choice_use_json_or_zip(use_json_or_zip, zip_name, json_name):
    """Выбрать откуда загружать данные из архива или JSON"""

    if use_json_or_zip == "JSON":
        return get_json(json_name)
    elif use_json_or_zip == "ZIP":
        return get_json_from_zip(zip_name, json_name)
    else:
        return get_json_from_zip(zip_name, json_name)
