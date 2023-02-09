# Task 1
def toGrams(grams):
    return 28.3495231 * grams


ounces = int(input("Ounces: "))
print(toGrams(ounces))


# Task 2
def toCelsius(temp):
    return (5 / 9) * (temp - 32)


F = int(input("Fahrenheit temperature: "))
print(toCelsius(F))


# Task 3
def solve(numheads, numlegs):
    rabbit = numlegs / 2 - numheads
    chicken = numheads - rabbit
    if rabbit == round(rabbit, 0) and chicken == round(chicken, 0) and rabbit >= 0 and chicken >= 0:
        print(f"Rabbits: {int(rabbit)}, Chickens: {int(chicken)}")
    else:
        print("No solution")


heads = int(input("Heads: "))
legs = int(input("Legs: "))
solve(heads, legs)

# Task 4
myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


def isPrime(n):
    prime = False
    if n > 1:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                prime = False
                break
            else:
                prime = True
    else:
        prime = False
    return prime


primeList = list(filter(isPrime, myList))
print(primeList)

# Task 5
from itertools import permutations


def permute(string):
    return [''.join(p) for p in permutations(string)]


print(permute("abc"))


# Task 6
def stringReverse(string):
    reverse = []
    words = string.split()
    for word in words:
        reverse.insert(0, word)
    print(" ".join(reverse))


myString = input("String: ")
stringReverse(myString)


# Task 7
def has_33(nums):
    for num in range(len(nums) - 1):
        if nums[num] == nums[num + 1] == 3:
            return True
    else:
        return False


has_33([1, 3, 3])
has_33([1, 3, 1, 3])
has_33([3, 1, 3, 3])


# Task 8
def spy_game(myList):
    nums = list(filter(lambda x: x == 0 or x == 7, myList))
    print(nums)

    for num in range(len(nums) - 2):
        if nums[num:num + 3] == [0, 0, 7]:
            return True
    else:
        return False


spy_game([1, 2, 4, 0, 0, 7, 5])
spy_game([1, 0, 2, 4, 0, 5, 7])
spy_game([1, 7, 2, 0, 4, 5, 0])

# Task 9
import math


def volumeSphere(rad):
    return round((4 / 3 * math.pi * (rad ** 3)), 1)


print(volumeSphere(10))


# Task 10
def unique(mess):
    uniqueList = []
    for i in mess:
        if i not in uniqueList:
            uniqueList.append(i)
    print(uniqueList)


myList = [1, 1, 2, 5, 2, 3, 4, 5, 6, 6, 5, 1, 8, 10]
unique(myList)


# Task 11
def palindrome(word):
    rev_word = word[::-1]
    if word == rev_word:
        return True
    return False


print(palindrome("lattal"))
print(palindrome("keyboard"))


# Task 12
def histogram(biglist):
    for i in biglist:
        print(i * '*')


myList = [1, 5, 3, 4, 1, 0]
histogram(myList)

# Task 13
import random

x = random.randint(1, 20)
guess = 0

print("Hello! What is your name?")
name = input()
print()
print(f"Well, {name}, I am thinking of a number between 1 and 20.")

while True:
    print("Take a guess.")
    number = int(input())
    guess += 1

    print()

    if number > x:
        print("Your guess is too high.")
    elif number < x:
        print("Your guess is too low.")
    elif number == x:
        print(f"Good job, {name}! You guessed my number in {guess} guesses!")
        break
