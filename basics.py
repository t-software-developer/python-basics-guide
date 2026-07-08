# ============================================
# PYTHON BASICS - BEGINNER TO PYTHONIC
# ============================================

# -------------------------
# Variables
# -------------------------

# Store an integer
age = 25

# Store a floating-point number
height = 5.9

# Store a string
name = "Alice"

# Store a boolean
is_student = True

# Print values
print(age)
print(height)
print(name)
print(is_student)

# Pythonic
print(age, height, name, is_student)


# -------------------------
# User Input
# -------------------------

# Ask for the user's name
user_name = input("Enter your name: ")

# Display greeting
print("Hello", user_name)

# Pythonic
print(f"Hello {input('Enter your name: ')}")


# -------------------------
# If Statement
# -------------------------

number = 15

if number > 10:
    print("Greater than 10")
else:
    print("10 or less")

# Pythonic
print("Greater than 10" if number > 10 else "10 or less")


# -------------------------
# For Loop
# -------------------------

# Print numbers 1-5
for i in range(1, 6):
    print(i)

# Pythonic
print(*range(1, 6))


# -------------------------
# While Loop
# -------------------------

count = 1

while count <= 5:
    print(count)
    count += 1


# -------------------------
# Lists
# -------------------------

numbers = [10, 20, 30]

# Add item
numbers.append(40)

# Remove item
numbers.remove(20)

# Print each item
for num in numbers:
    print(num)

# Pythonic
print(*numbers)


# -------------------------
# Dictionary
# -------------------------

person = {
    "name": "Alice",
    "age": 25
}

print(person["name"])

# Pythonic
print(person.get("name"))


# -------------------------
# Functions
# -------------------------

def square(number):
    # Return squared value
    return number * number

print(square(5))

# Pythonic (lambda)
square = lambda x: x * x
print(square(5))


# -------------------------
# List Comprehension
# -------------------------

squares = []

for i in range(10):
    squares.append(i * i)

print(squares)

# Pythonic
print([i * i for i in range(10)])


# -------------------------
# Exception Handling
# -------------------------

try:
    number = int(input("Enter a number: "))
    print(number)
except ValueError:
    print("Invalid number.")

# Pythonic
try:
    print(int(input("Number: ")))
except ValueError:
    print("Invalid")


# -------------------------
# File Writing
# -------------------------

with open("sample.txt", "w") as file:
    file.write("Hello Python")

# Read file
with open("sample.txt") as file:
    print(file.read())


# -------------------------
# Classes
# -------------------------

class Person:

    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello", self.name)

person = Person("Alice")
person.greet()

# Pythonic
class Person:
    def __init__(self, name): self.name = name
    def greet(self): print(f"Hello {self.name}")

Person("Bob").greet()


# -------------------------
# Enumerate
# -------------------------

fruits = ["Apple", "Banana", "Orange"]

for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)


# -------------------------
# Zip
# -------------------------

names = ["Alice", "Bob"]
ages = [20, 30]

for name, age in zip(names, ages):
    print(name, age)


# -------------------------
# Dictionary Comprehension
# -------------------------

squares = {x: x * x for x in range(5)}
print(squares)


# -------------------------
# Set Comprehension
# -------------------------

unique = {x % 3 for x in range(10)}
print(unique)


# -------------------------
# Lambda + Sorted
# -------------------------

students = [
    ("Alice", 85),
    ("Bob", 92),
    ("Charlie", 78)
]

students.sort(key=lambda x: x[1], reverse=True)

print(students)


# -------------------------
# Generator
# -------------------------

def countdown(n):
    while n > 0:
        yield n
        n -= 1

for value in countdown(5):
    print(value)


# -------------------------
# f-Strings
# -------------------------

name = "Alice"
score = 95

print(f"{name} scored {score}%")

# ============================================
# End of Python Basics Snippets
# ============================================