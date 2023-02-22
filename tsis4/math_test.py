import math

# Task 1
print("Task 1:")
degree = int(input("Input degree:"))
print(f"Output radian: {math.radians(degree):.6f}\n")


# Task 2
print("Task 2:")
height = float(input("Height:"))
base_1 = float(input("Base, first value:"))
base_2 = float(input("Base, second value:"))
print(f"Area of a trapezoid: {(base_1 + base_2) / 2 * height}\n")


# Task 3
print("Task 3:")
sides = float(input("Number of sides:"))
length = float(input("Length of a side:"))
print(f"Area of a {sides}-sided polygon is: {(sides * pow(length, 2)) / (4 * math.tan(math.radians(180/sides))):.0f}\n")


# Task 4
print("Task 4:")
lenbase = float(input("Length of base:"))
height = float(input("Heigth of parallelogram:"))
print(f"Area of a parallelogram: {lenbase * height}")

