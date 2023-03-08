from time import sleep

# Task 1 - Multiply all numbers in a list
print("Task 1:")
mylist = [i for i in range(1, 6)]
multiplier = 1

for i in mylist:
    multiplier *= i

print(multiplier)

# Task 2 - Calculate the number of uppercase and lowercase letters
print("\nTask 2:")
mystring = input("String to check: ")
upper = 0
lower = 0

for i in mystring:
    if i.isupper():
        upper += 1
    elif i.islower():
        lower += 1

print(f"Uppers: {upper}\nLowers: {lower}")

# Task 3
print("\nTask 3:")
mystring = input("String to check: ")

reverse = mystring[::-1]

if mystring == reverse:
    print(True)
else:
    print(False)

# Task 4
print("\nTask 4:")

number = int(input("Number: "))
ms = int(input("Milliseconds: "))

sleep(ms / 1000)

print(f"Square root of {number} after {ms} milliseconds is {number ** 0.5}")


# Task 5
def checkTuple(tup):
    for i in tup:
        if i:
            pass
        else:
            return False
    return True


print("\nTask 5:")
mytuple = (0, 0, 1)
mytuple_2 = (1, 1, 1)

print(checkTuple(mytuple))
print(checkTuple(mytuple_2))
