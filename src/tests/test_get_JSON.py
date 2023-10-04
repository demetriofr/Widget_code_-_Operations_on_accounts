from src.wg_operations_on_accounts.get_JSON import *
from src.tests.AFTER import after


def test_get_json_from_zip():
    assert get_json_from_zip("operations.zip", "operations.json") == after()


def test_get_json():
    assert get_json("operations.json") == after()


def test_choice_use_json_or_zip():
    assert choice_use_json_or_zip("ZIP", "operations.zip", "operations.json") == after()
    assert choice_use_json_or_zip("JSON", "operations.zip", "operations.json") == after()
    assert choice_use_json_or_zip("zip", "operations.zip", "operations.json") == after()
