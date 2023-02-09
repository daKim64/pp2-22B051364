# Dictionary
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)

# Dictionary Items
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict["brand"])

# Duplicates Not Allowed
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,  # This element is ignored
    "year": 2020
}
print(thisdict)

# Dictionary Length
print(len(thisdict))

# Dictionary Items - Data Types
thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}

# type()
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(type(thisdict))

# The dict() Constructor
thisdict = dict(name="John", age=36, country="Norway")
print(thisdict)


# Accessing Items
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict["model"]
print(x)

# Accessing Items - get()
x = thisdict.get("model")
print(x)


# Get Keys
x = thisdict.keys()
print(x)

# Get Keys - Example
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.keys()

print(x)  # before the change

car["color"] = "white"

print(x)  # after the change


# Get Values
x = thisdict.values()

# Get Values - Example 1
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.values()

print(x)  # before the change

car["year"] = 2020

print(x)  # after the change

# Get Values - Example 2
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.values()

print(x)  # before the change

car["color"] = "red"

print(x)  # after the change


# Get Items
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = thisdict.items()

print(x)

# Get Items - Example 1
x = car.items()

print(x)  # before the change

car["year"] = 2020

print(x)  # after the change

# Get Items - Example 2
car["color"] = "red"

print(x)  # after the change


# Check if Key Exists
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")


# Change Values
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict["year"] = 2018
print(thisdict)

# Update Dictionary
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.update({"year": 2020})
print(thisdict)


#  Adding Items
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

# Update Dictionary - Agains
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.update({"color": "red"})
print(thisdict)


# Removing Items
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.pop("model")
print(thisdict)

# Remove last inserted item
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.popitem()
print(thisdict)

# Remove item using del keyword
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
del thisdict["model"]
print(thisdict)

# Delete dictionary
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
del thisdict
# print(thisdict) #this will cause an error because "thisdict" no longer exists.

# Clear dictionary
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.clear()
print(thisdict)


# Loop Through a Dictionary
thisdict =	{
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

# Print all key names
for x in thisdict:
    print(x)

# Print all values
for x in thisdict:
    print(thisdict[x])

# Return values using values()
for x in thisdict.values():
    print(x)

# Return keys using keys()
for x in thisdict.keys():
    print(x)

# Return keys and values using items()
for x, y in thisdict.items():
    print(x, y)


# Copy a Dictionary - copy()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

# Copy a Dictionary - dict()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)


# Nested Dictionaries
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

# Adding dictionaries, separately
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

# Access Items in Nested Dictionaries
print(myfamily["child2"]["name"])
