from datetime import date, datetime # import date and datetime modules from datetime library

def days_lived(birth_date):
    today = date.today() # get current date
    birth_date = datetime.strptime(birth_date, "%Y-%m-%d").date() # convert string birthdate to date object
    return (today - birth_date).days # subtract birthdate from current date and return the difference in days

birth_date = input("Enter your birthdate in YYYY-MM-DD format: ") # prompt user to enter birthdate
print("You have lived for ", days_lived(birth_date), " days.") # call days_lived function and print the result
