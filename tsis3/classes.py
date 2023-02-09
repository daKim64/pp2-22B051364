# Task 1
class Class:
    def getString(self):
        self.string = input()
    def printString(self):
        print(self.string.upper())

thing = Class()

thing.getString()
thing.printString()

# Task 2
class Shape:
    def area(self):
        self.area = 0
        print(self.area)

class Square(Shape):
    def __init__(self, length):
        self.length = length
    def area(self):
        self.area = self.length ** 2
        print(self.area)

anything = Square(10)
anything.area()

something = Shape()
something.area()

# Task 3
class Rectangle(Shape):
    def __init__(self, length, width):
       self.length = length
       self.width = width
    def area(self):
        self.area = self.length * self.width
        print(self.area)

nothing = Rectangle(5, 2)
nothing.area()

# Task 4
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(self.x, ':', self.y)

    def move(self, x, y):
        self.x = x
        self.y = y

    def dist(pointA, pointB):
        distance = ((pointA.x - pointB.x) ** 2 + (pointA.y - pointB.y) ** 2) ** 0.5
        print(distance)   # Might use round(distance, 2)

firstPoint = Point(2, 5)
firstPoint.show()

firstPoint.move(5, 10)
firstPoint.show()

secondPoint = Point(-5, 5)
firstPoint.dist(secondPoint)

# Task 5
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, cash):
        self.balance += cash
        print(f"Current balance: {self.balance}")
    def withdraw(self, cash):
        if self.balance >= cash:
            self.balance -= cash
            print(f"Current balance: {self.balance}")
        else:
            print("Withdrawal exceeds the available balance.")

firstBalance = Account("Artem", 500)
firstBalance.withdraw(501)
firstBalance.deposit(500)
firstBalance.withdraw(1000)

# Task 6
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


