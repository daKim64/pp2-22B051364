import re


# Task 1
def task1(text):
    pattern = ".*ab*"
    match = re.search(pattern, text)
    if match:
        print(f"Matched part: {match.group()}")
    else:
        print("Nothing found")


print("Task 1:")
task1("String")
task1("Example")
task1("abb")


# Task 2
def task2(text):
    pattern = ".*ab{2,3}"
    match = re.search(pattern, text)
    if match:
        print(f"Matched part: {match.group()}")
    else:
        print("Nothing found")


print("\nTask 2:")
task2("String")
task2("Example")
task2("abb")
task2("ab")


# Task 3
def task3(text):
    pattern = "[a-z]+_[a-z]+"
    match = re.search(pattern, text)
    if match:
        print(f"Matched part: {match.group()}")
    else:
        print("Nothing found")


print("\nTask 3:")
task3("Abc_Dbc")
task3("abc_dbc")
task3("abcdbc")


# Task 4
def task4(text):
    pattern = "^[A-Z][a-z]+"
    match = re.search(pattern, text)
    if match:
        print(f"Matched part: {match.group()}")
    else:
        print("Nothing found")


print("\nTask 4:")
task4("Abcd")
task4("AAbbbb")


# Task 5
def task5(text):
    pattern = "a.+b$"
    match = re.search(pattern, text)
    if match:
        print(f"Matched part: {match.group()}")
    else:
        print("Nothing found")


print("\nTask 5:")
task5("aaaaaaaaaabb")
task5("aaaaaaaaabd")
task5("ab")


# Task 6
def task6(text):
    pattern = "[ ,.]"
    match = re.sub(pattern, ":", text)
    print(match)


print("\nTask 6:")
task6("Column row space matrix, vector space.")


# Task 7
def task7(text):
    x = re.split("_", text)
    string = ''.join(word.capitalize() for word in x)
    print(string)


print("\nTask 7:")
task7("what_a_day")


# Task 8
def task8(text):
    pattern = "[A-Z][^A-Z]*"
    x = re.findall(pattern, text)
    print(x)


print("\nTask 8:")
task8("TheBigSentence")


# Task 9
def task9(text):
    pattern = "(.)([A-Z])"
    match = re.sub(pattern, r"\1 \2", text)
    print(match)


print("\nTask 9:")
task9("TheSentenceIsHere")


# Task 10
def task10(text):
    x = re.findall("[A-Z][^A-Z]*", text)
    string = '_'.join(word.lower() for word in x)
    print(string)


print("\nTask 10:")
task10("CamelCaseDoesItWork")
