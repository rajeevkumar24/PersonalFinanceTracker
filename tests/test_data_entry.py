import pytest
from unittest.mock import patch
from src.data_entry import get_date, get_amount, get_category, get_description



 
def test_get_date_valid():
    with patch("builtins.input", return_value="05-04-2025"):
        assert get_date("Enter date: ")=="05-04-2025"

def test_get_date_invalid():
    with patch("builtins.input", side_effect=["invalid","05-04-2025"]):
        assert get_date("Enter date: ")=="05-04-2025"


def test_get_date_default():
    with patch("builtins.input", return_value=""):
        assert get_date("Enter date: ", allow_default=True) is not None

def test_get_amount_valid():
    with patch("builtins.input", return_value="100"):
        assert get_amount() == 100.0


def test_get_amount_invalid_then_valid():
    with patch("builtins.input", side_effect=["-50", "0", "100"]):
        assert get_amount() == 100.0


def test_get_category_income():
    with patch("builtins.input", return_value="I"):
        assert get_category() == "Income"


def test_get_category_expense():
    with patch("builtins.input", return_value="E"):
        assert get_category() == "Expense"


def test_get_category_invalid_then_valid():
    with patch("builtins.input", side_effect=["Invalid", "I"]):
        assert get_category() == "Income"


def test_get_description():
    with patch("builtins.input", return_value="Groceries"):
        assert get_description() == "Groceries"