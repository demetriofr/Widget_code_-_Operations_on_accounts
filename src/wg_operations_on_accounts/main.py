from src.wg_operations_on_accounts.get_JSON import choice_use_json_or_zip
from src.wg_operations_on_accounts.operations import get_executed_operations, get_sort_date_operations, \
    display_n_messages

# Данные для JSON
USE_JSON_OR_ZIP = "ZIP"
ZIP_NAME = "operations.zip"
JSON_NAME = "operations.json"

# Выбрать количество сообщений для вывода на экран
N_MESSAGES = 5


def main():
    """Выводит сообщения в виде списка о последних успешных операциях для передачи его в виджет"""

    operations = choice_use_json_or_zip(USE_JSON_OR_ZIP, ZIP_NAME, JSON_NAME)
    executed_operations = get_executed_operations(get_sort_date_operations(operations))

    return display_n_messages(executed_operations)


# Временно выводятся сообщения в консоль для демонстрации, т.к. по условию ТЗ требуется выводить с бэкенда в виджет
print('\n')
print(*main(), sep='\n')
