
from datetime import date, timedelta
from seasons import calculate_age_in_minutes, convert_to_english_words


def test_calculate_age_in_minutes():
    birth_date = date(2000, 1, 1)
    today = date.today()
    age_in_minutes = calculate_age_in_minutes(birth_date)
    expected_age_in_minutes = int((today - birth_date).total_seconds() // 60)
    assert age_in_minutes == expected_age_in_minutes


def test_convert_to_english_words():
    assert convert_to_english_words(0) == "zeroth"
    assert convert_to_english_words(1) == "first"
    assert convert_to_english_words(11) == "eleventh"
    assert convert_to_english_words(20) == "twentieth"
    assert convert_to_english_words(21) == "twenty-first"
 
