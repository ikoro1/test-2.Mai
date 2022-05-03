users = [
    {
        "name": "Holly",
        "type": "Student",
        "password": "hunter"
    },
    {
        "name": "Peter",
        "type": "Student",
        "password": "pan"
    },
    {
        "name": "Janis",
        "type": "Teacher",
        "password": "joplin"
    }
]


def show_offers(username, password):
    legend = False
    for user in users:
        if username == user['name'] and user["type"] == "Student" and user["password"] == password:
            print("We have great courses to offer you!")
            legend = True
    if not legend:
        print("Not for you, bitch!")

if __name__ == '__main__':
    username = input("What is your username?")
    password = input(f"Type the password for username {username}: ")
    show_offers(username, password)