import os
import shutil

# Task 1
print("Task 1:")
print("What to do?\n"
      "1. List only directories\n"
      "2. List directories and files\n"
      "3. List files in a specified path")

option = int(input("Enter the number (1-3): "))

if option == 1:
    print("Directories:")
    dirs = os.listdir()
    for i in dirs:
        if os.path.isdir(i):
            print(i)

elif option == 2:
    print("Files and Directories:")
    fdirs = os.listdir()
    for i in fdirs:
        print(i)

elif option == 3:
    PATH = input("Path: ")
    print(f"Files in {PATH}:")
    files = os.listdir(path=PATH)
    for i in files:
        if os.path.isfile(os.path.join(PATH, i)):
            print(i)

# Task 2
print("\nTask 2: Checking access")
PATH = input("Path: ")
print("Exists:", os.access(PATH, os.F_OK))
print("Readable:", os.access(PATH, os.R_OK))
print("Writable:", os.access(PATH, os.W_OK))
print("Executable:", os.access(PATH, os.X_OK))

# Task 3
print("\nTask 3: Filename and Directory")
PATH = input("Path: ")
print("Path exists:", os.path.exists(PATH))
print("Filename:", os.path.basename(PATH))
print("Directory:", os.path.dirname(PATH))

# Task 4
print("\nTask 4: Count the number of lines in a file")
with open("textfile.txt", "r") as file:
    print("Number of lines:", len(file.readlines()))

# Task 5
print("\nTask 5: Write a list to file")
mylist = [str(i) for i in range(1, 11)]
with open("list.text", "w") as file:
    file.writelines(s + "\n" for s in mylist)
print("Done.")

# Task 6
print("\nTask 6: Create 26 .txt files")
if not os.path.exists("Letter Files"):
    os.makedirs("Letter Files")

uppercases = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in uppercases:
    with open(os.path.join("Letter Files", i) + ".txt", "w"):
        pass
print("Done.")

# Task 7
print("\nTask 7: Copy file")
shutil.copyfile("textfile.txt", "copied.txt")
print("Done.")

# Task 8
print("\nTask 8: Delete file")
PATH = input("Path: ")

if os.path.exists(PATH) and os.access(PATH, os.F_OK):
    os.remove(PATH)
    print("Done.")
else:
    print("Something went wrong.")

