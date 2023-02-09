# Python String
print("Hello")
print('Hello')

# Assign String to a Variable
a = "Hello"
print(a)

# Multiline Strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

# Strings are Arrays
a = "Hello, World!"
print(a[1])

# Looping Through a String
for x in "banana":
    print(x)

# String Length
a = "Hello, World!"
print(len(a))

# Check String
txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")

# Check if NOT
txt = "The best things in life are free!"
print("expensive" not in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")

# Slicing
b = "Hello, World!"
print(b[2:5])

# Slice To the End
b = "Hello, World!"
print(b[2:])

# Negative Indexing
b = "Hello, World!"
print(b[-5:-2])

# Modify Strings - Uppercase
a = "Hello, World!"
print(a.upper())

# Lowercase
a = "Hello, World!"
print(a.lower())

# Remove Whitespace
a = " Hello, World! "
print(a.strip())  # returns "Hello, World!"

# Replace String
a = "Hello, World!"
print(a.replace("H", "J"))

# Split String
a = "Hello, World!"
print(a.split(","))  # returns ['Hello', ' World!']

# String Concatenation
a = "Hello"
b = "World"
c = a + b
print(c)

# With whitespace
a = "Hello"
b = "World"
c = a + " " + b
print(c)

# String Format
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

# Escape Character
txt = "We are the so-called \"Vikings\" from the north."

txt = 'It\'s alright.'
print(txt)

txt = "This will insert one \\ (backslash)."
print(txt)

txt = "Hello\nWorld!"
print(txt)

txt = "Hello\tWorld!"
print(txt)

# This example erases one character (backspace):
txt = "Hello \bWorld!"
print(txt)

# A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157"
print(txt)

# A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt)
