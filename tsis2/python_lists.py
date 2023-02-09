# Creating a List
thislist = ["apple", "banana", "cherry"]
print(thislist)

# Allow duplicates
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

# List Length
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

# List Items - Data Types
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

list1 = ["abc", 34, True, 40, "male"]

# type()
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

# The list() Constructor
thislist = list(("apple", "banana", "cherry"))  # note the double round-brackets
print(thislist)

# Access Items
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

# Negative Indexing
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

# Range of Indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

# Starting from the beginning till 4th (index) element
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

# Starting from the 2nd (index) element till the end
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

# Range of Negative Indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

# Check if Item Exists
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")

# Change Item Value
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

# Change a Range of Item Values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

# Remaining items will be inserted (More)
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

# Remaining items will be inserted (Less)
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

# Insert Items
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

# Append Items
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# Insert Items (Again)
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

# Extend List
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# Extend List - Add Any Iterable
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

# Remove Specified Item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# Remove Specified Index
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

# Pop() method - if index is not specified it removes the last item
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

# Remove using del keyword
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# Delete list using del
thislist = ["apple", "banana", "cherry"]
del thislist

# Clear the List
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

# Loop Through a List
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

# Loop Through the Index Numbers
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])

# Using a While Loop
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1

# Looping Using List Comprehension
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

# No List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)

# Using List Comprehension: newlist = [expression for item in iterable if condition == True]
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

# Condition
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if x != "apple"]

print(newlist)

# Condition can be omitted
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits]

print(newlist)

# Iterable can be any iterable object
newlist = [x for x in range(10)]

print(newlist)

# Iterable - with condition
newlist = [x for x in range(10) if x < 5]

print(newlist)

# Expression
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x.upper() for x in fruits]

print(newlist)

# Set the outcome in expression
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = ['hello' for x in fruits]

print(newlist)

# The expression can contain coniditions
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x if x != "banana" else "orange" for x in fruits]

print(newlist)

# Sort List Alphanumerically - Alphabetically
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

# Sort List Alphanumerically - Numerically
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

# Sort Descending - 1
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse=True)
print(thislist)

# Sort Desceding - 2
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse=True)
print(thislist)


# Customize Sort Function
def myfunc(n):
    return abs(n - 50)


thislist = [100, 50, 65, 82, 23]
thislist.sort(key=myfunc)
print(thislist)

# Case Insensitive Sort
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

# Case Insensitive Sort - use str,lower as key
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key=str.lower)
print(thislist)

# Reverse Order
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

# Copy List - copy()
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# Copy List - list()
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

# Join Lists by +
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# Join Lists by append()
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

for x in list2:
    list1.append(x)

print(list1)

# Join Lists by extend()
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)
