print(10 + 5)

#                       Python Arithmetic Operators
# Addition
x = 5
y = 3
print(x + y)

# Subtraction
print(x - y)

# Multiplication
print(x * y)

# Division
x = 12
y = 3
print(x / y)

# Modulus
x = 5
y = 2
print(x % y)

# Exponentiation
x = 2
y = 5
print(x ** y)  # same as 2*2*2*2*2

# Floor division
x = 15  # the floor division // rounds the result down
y = 2   # to the nearest whole number

print(x // y)

#                       Python Assignment Operators
# Operator =
x = 5
print(x)

# Operator +=
x += 3
print(x)

# Operator -=
x -= 3
print(x)

# Operator *=
x *= 3
print(x)

# Operator /=
x /= 3
print(x)

# Operator %=
x %= 3
print(x)

# Operator //=
x //= 3
print(x)

# Operator  **=
x **= 3
print(x)

# Operator &=
x = 5
x &= 3
print(x)

# Operator |=
x |= 3
print(x)

# Operator ^=
x = 5
x ^= 3
print(x)

# Operator >>=
x = 5
x >>= 3
print(x)

# Operator <<=
x <<= 3
print(x)

#                       Python Comparison Operators
# Operator ==
x = 5
y = 3
print(x == y)  # returns False because 5 is not equal to 3

# Operator !=
x = 5
y = 3
print(x != y)  # returns True because 5 is not equal to 3

# Operator >
x = 5
y = 3

print(x > y)  # returns True because 5 is greater than 3

# Operator <
x = 5
y = 3
print(x < y)  # returns False because 5 is not less than 3

# Operator >=
x = 5
y = 3
print(x >= y)  # returns True because five is greater, or equal, to 3

# Operator <=
x = 5
y = 3
print(x <= y)  # returns False because 5 is neither less than nor equal to 3

#                   Python Logical Operators
# Operator and
x = 5  # returns True because 5 is greater than 3 AND 5 is less than 10
print(x > 3 and x < 10)

# Operator or
x = 5  # returns True because one of the conditions are true (5 is greater than 3, but 5 is not less than 4)
print(x > 3 or x < 4)

# Operator not
x = 5  # returns False because not is used to reverse the result
print(not(x > 3 and x < 10))

#                   Python Identity Operators
# Operator is
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)  # returns True because z is the same object as x
print(x is y)  # returns False because x is not the same object as y, even if they have the same content
print(x == y)  # to demonstrate the difference between "is" and "==": this \
               # comparison returns True because x is equal to y

# Operator is not
print(x is not z)  # returns False because z is the same object as x
print(x is not y)  # returns True because x is not the same object as y, even if they have the same content
print(x != y)  # to demonstrate the difference between "is not" and "!=": this
               # comparison returns False because x is equal to y

#                   Python Membership Operators
# Operator in
x = ["apple", "banana"]
print("banana" in x)  # returns True because a sequence with the value "banana" is in the list

# Operator not in
x = ["apple", "banana"]
print("pineapple" not in x)  # returns True because a sequence with the value "pineapple" is not in the list

#                   Python Bitwise Operators
# Operator &
print(6 & 3)

# Operator |
print(6 | 3)

# Operator ^
print(6 ^ 3)

# Operator ~
print(~3)

# Operator <<
print(3 << 2)

# Operator >>
print(8 >> 2)