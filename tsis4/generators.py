# Task 1
print("Task 1:")
n = int(input("Input the value of n:"))
squaring = (i ** 2 for i in range(1, n + 1))

for x in squaring:
    print(x)
print("\n")

# Task 2
print("Task 2:")
n = int(input("Input the value of n:"))

even_numbers = (num for num in range(1, n) if num % 2 == 0)

for num in even_numbers:
    print(num, end=' ')
print("\n \n")


# Task 3
def divisible(n):
    start = 1
    while start < n:
        if start % 3 == 0 and start % 4 == 0:
            yield start
        start += 1


print("Task 3:")
n = int(input("Input the value of n:"))
divisibles = divisible(n)
for num in divisibles:
    print(num, end=' ')
print("\n \n")


# Task 4
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2


print("Task 4:")
a = int(input("Input the value of a:"))
b = int(input("Input the value of b:"))
squares = squares(a, b)

for sq in squares:
    print(sq)
print("\n")

# Task 5
print("Task 5:")
n = int(input("Input the value of n:"))
reverse = (i for i in range(n, -1, -1))

for num in reverse:
    print(num, end=' ')
