users = [
    {
        "name": "Holly",
        "password": "hunter"
    },
    {
        "name": "Peter",
        "password": "pan"
    },
    {
        "name": "Janis",
        "password": "joplin"
    }
]

def get_user(username, password):
    for user in users:
        if user ["name"] == username and user ["password"] == password:
            return user
    return None

# def get_user2(username, password):
#     return next(u for u in users
#                 if user ['name'] == username and ["password"] == password), None)

username = input("What is your username? ")
password = input(f"Type the password for username {username}: ")
user = get_user(username, password)

if not user:
    print("An error occurred. You are not authorized")
list = [1, 2, 3]
count = 0
for i in list:
    count = count + i
print(count)