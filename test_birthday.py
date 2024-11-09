import pandas as pd
import pytest

def test_add_birthday():
    df = pd.read_csv('birthdays.csv')
    expected_birthday_count = 1
    actual_birthday_count = df[df['Name'] == 'Matthew'].shape[0]
    assert actual_birthday_count == expected_birthday_count, ">>> [ERROR] Matthew's birthday should be added to birthdays.csv <<<"
