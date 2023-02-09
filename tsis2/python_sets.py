# Set
thisset = {"apple", "banana", "cherry"}
print(thisset)

# Duplicates Not Allowed
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

# Get the Length of a Set
thisset = {"apple", "banana", "cherry"}
print(len(thisset))

# Set Items - Data Types
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

set4 = {"abc", 34, True, 40, "male"}

# type()
myset = {"apple", "banana", "cherry"}
print(type(myset))

# The set() Constructor
thisset = set(("apple", "banana", "cherry"))  # note the double round-brackets
print(thisset)


# Access Items - 1
thisset = {"apple", "banana", "cherry"}

for x in thisset:
    print(x)

# Access Items - 2
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

# Change Items - Impossible to do


# Add Items
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

# Add Sets
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

# Add Any Iterable for update()
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)


# Remove Item - remove()
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

# Remove Item - discard()
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

# Remove Item - pop() to remove random element
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)

# Clear the set - clear()
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

# Delete the set - del keyword
thisset = {"apple", "banana", "cherry"}

del thisset

# print(thisset)  # Error


# Loop Items
thisset = {"apple", "banana", "cherry"}

for x in thisset:
    print(x)


# Join Two Sets - union()
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

# Join Two Sets - update()
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

# Keep ONLY the Duplicates - Update set
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)

# Keep ONLY the Duplicates - Create new set
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)

# Keep All, But NOT the Duplicates - Update set
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)

# Keep All, But NOT the Duplicates - Create new set
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)

# True and 1 are treated the same
x = {"apple", "banana", "cherry", True}
y = {"google", 1, "apple", 2}

z = x.symmetric_difference(y)
