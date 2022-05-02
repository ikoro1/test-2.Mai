

username = input("What is your username? ")
password = input(f"Type the password for username {username}: ")
valid = {"username": "admin", "password": "admin"}
if password == valid["password"] and username == valid["username"]:
    print("Welcome, admin!")
else:
    print("You are NOT admin!")

