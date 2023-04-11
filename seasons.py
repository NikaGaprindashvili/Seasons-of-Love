import sys
from datetime import date, datetime
import inflect


def calculate_age_in_minutes(birth_date):
    today = date.today()
    age_timedelta = today - birth_date
    age_in_minutes = int(age_timedelta.total_seconds() // 60)
    return age_in_minutes


def get_birth_date_from_user():
    date_string = input("Please enter your birthdate in YYYY-MM-DD format: ")
    try:
        birth_date = datetime.strptime(date_string, "%Y-%m-%d").date()
        return birth_date
    except ValueError:
        print("Invalid date format. Please enter a date in YYYY-MM-DD format.")
        sys.exit()


def convert_to_english_words(number):
    p = inflect.engine()
    return p.number_to_words(p.ordinal(number))


def print_age_in_minutes(birth_date):
    age_in_minutes = calculate_age_in_minutes(birth_date)
    age_in_words = convert_to_english_words(age_in_minutes)
    print(f"You are {age_in_words} minutes old.")


def main():
    birth_date = get_birth_date_from_user()
    print_age_in_minutes(birth_date)


if __name__ == "__main__":
    main()
