# Python program to calculate how many days person survived in this world
from datetime import date, datetime

def days_lived(birth_date):
    today = date.today()
    birth_date = datetime.strptime(birth_date, "%Y-%m-%d").date()
    return (today - birth_date).days


# Enter your birthdate in YYYY-MM-DD format:
birth_date = input("Enter your birthdate in YYYY-MM-DD format: ")
print("You have lived for ", days_lived(birth_date), " days.")
