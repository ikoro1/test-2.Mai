import datetime

username = input("What is your username?")
password = input(f"Type the password for username {username}: ")
valid = {"username": "admin", "password": "admin"}


def isweekend(date=datetime.datetime.now()):
    if date.weekday() > 4:
        return True
    return False


def weekend(today):
    if (username == valid["username"] and password == valid["password"]) or isweekend(today) == True:
        print(f"Welcome, {username}")
    else:
        print("Credentials are invalid")


if __name__ == '__main__':
    weekend(datetime.date(2022, 5, 1))