import pickle

import pytest
from utility import Utility


def test_menu_choice_valid_choice(mocker):
    mocker.patch("builtins.input", side_effect=["1"])
    choices = ["Option 1", "Option 2", "Option 3"]
    result = Utility.menu_choice(choices)
    assert result == 0


def test_menu_choice_invalid_choice(mocker):
    mocker.patch("builtins.input", side_effect=["4", "2"])
    choices = ["Option 1", "Option 2", "Option 3"]
    result = Utility.menu_choice(choices)
    assert result == 1


def test_menu_choice_keyboard_interrupt(mocker):
    mocker.patch("builtins.input", side_effect=KeyboardInterrupt)
    choices = ["Option 1", "Option 2"]
    result = Utility.menu_choice(choices)
    assert result is None


def test_get_non_negative_int_valid_input(mocker):
    mocker.patch("builtins.input", side_effect=["5"])
    result = Utility.get_non_negative_int("Enter a number: ")
    assert result == 5


def test_get_non_negative_int_invalid_input(mocker):
    mocker.patch("builtins.input", side_effect=["-3", "abc", "4"])
    result = Utility.get_non_negative_int("Enter a number: ")
    assert result == 4


def test_get_non_negative_int_keyboard_interrupt(mocker):
    mocker.patch("builtins.input", side_effect=KeyboardInterrupt)
    result = Utility.get_non_negative_int("Enter a number: ")
    assert result is None


def test_get_response_success(mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"key": "value"}
    mocker.patch("requests.request", return_value=mock_response)

    result = Utility.get_response("https://example.com")
    assert result == {"key": "value"}


def test_get_response_failure(mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 404
    mocker.patch("requests.request", return_value=mock_response)

    with pytest.raises(SystemExit):
        Utility.get_response("https://example.com")


def test_from_file(mocker):
    mock_data = [1, 2, 3]
    mocker.patch("builtins.open", mocker.mock_open(read_data=pickle.dumps(mock_data)))
    result = Utility.from_file("test.pkl")
    assert result == mock_data


def test_to_file(mocker):
    mock_data = [1, 2, 3]
    mocker_open = mocker.mock_open()
    mocker.patch("builtins.open", mocker_open)

    Utility.to_file("test.pkl", mock_data)
    mocker_open.assert_called_once_with("test.pkl", "wb")


def test_get_not_empty_str_valid_input(mocker):
    mocker.patch("builtins.input", side_effect=["test input"])
    result = Utility.get_not_empty_str("Enter a string: ")
    assert result == "test input"


def test_get_not_empty_str_empty_input(mocker):
    mocker.patch("builtins.input", side_effect=["", "valid input"])
    result = Utility.get_not_empty_str("Enter a string: ")
    assert result == "valid input"