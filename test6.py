users = [
    {
        "name": "Clark",
        "type": "Publisher",
        "items": [
            {
                "title": "The ABC of Blockchain",
                "status": "Draft",
                "reads": 10
            }
        ]
    },
    {
        "name": "Peter",
        "type": "Publisher",
        "items": []
    },
    {
        "name": "Samantha",
        "type": "Publisher",
        "items": [
            {
                "title": "The ABC of JavaScript",
                "status": "Published",
                "reads": 3254
            },
            {
                "title": "The XYZ of JavaScript",
                "status": "Published",
                "reads": 226
            }
        ]
    },
    {
        "name": "Mathilda",
        "type": "Reviewer",
        "items": [
            {
                "title": "The ABC of Blockchain",
                "status": "Pending"
            }
        ]
    }
]

def has_hits(author):
    find_author = None
    for user in users:
        if user['name'] == author:
            find_author = user
    if find_author:
        for article in find_author['items']:
            if "reads" in article and article['reads'] > 1000:
                return True
    return False

if __name__ == '__main__':
    print("Clark", has_hits("Clark"))
    print("Peter", has_hits("Peter"))
    print("Samantha", has_hits("Samantha"))
    print("Mathilda", has_hits("Mathilda"))
    print("Mario", has_hits("Mario"))