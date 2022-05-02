import datetime
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def isweekend(date=datetime.datetime.now()):
    if not days[date.weekday()] == "Saturday" or days[date.weekday()] == "Saturday":
        return True
    return False

def isweekend_version2(date=datetime.datetime.now()):
    # print(date.weekday() > 4)
    return date.weekday() > 4

if __name__ == '__main__':

    print(isweekend_version2(datetime.date(2021, 8, 6)))
    print(isweekend_version2(datetime.date(2021, 8, 7)))
    print(isweekend_version2(datetime.date(2022, 8, 8)))
    print(isweekend_version2(datetime.date(2022, 8, 9)))