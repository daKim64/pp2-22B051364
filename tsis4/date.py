import datetime

# Task 1
print("Task 1:")
thisday = datetime.date.today()
print(thisday - datetime.timedelta(days=5), "\n")

# Task 2
print("Task 2:")
print("Yesterday:", datetime.date.today() - datetime.timedelta(days=1))
print("Today:", datetime.date.today())
print("Tomorrow:", datetime.date.today() + datetime.timedelta(days=1), "\n")

# Task 3
print("Task 3:")
print("No microseconds:", datetime.datetime.now().replace(microsecond=0), "\n")


# Task 4
def diff(dt1, dt2):
    difference = dt2 - dt1
    return difference.total_seconds()


print("Task 4:")
day_1 = datetime.datetime.now()
day_2 = datetime.datetime(year=2025, month=11, day=15, minute=56)
print(diff(day_1, day_2))

