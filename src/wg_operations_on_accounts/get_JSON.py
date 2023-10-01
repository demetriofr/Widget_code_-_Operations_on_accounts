import codecs
import pathlib
from zipfile import ZipFile


def get_path_to_operations():
    """Получает путь к архиву данных с операциями"""
    this_file_path = pathlib.Path(__file__)
    path_to_this_project = pathlib.PurePath(this_file_path).parents[2]
    path_to_operations = pathlib.Path(path_to_this_project, "data", 'operations.zip')
    return path_to_operations


def get_zip_operations():
    """Извлекает данные из архива"""
    with ZipFile(get_path_to_operations(), 'r') as myzip:
        with myzip.open("operations.json") as my_file:
            operations_json = ""
            # Перекодирует в формат utf8
            for line in codecs.iterdecode(my_file, 'utf8'):
                operations_json += line
    return operations_json


def get_JSON():
    """Получить JSON"""
    return get_zip_operations()
