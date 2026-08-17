# Python Functions

# Simple function
def greet():
    print("Hello! Welcome to Python.")


greet()


# Function with a parameter
def greet_user(name):
    print("Hello,", name)


greet_user("Anjali")


# Function with multiple parameters
def add(a, b):
    return a + b


result = add(10, 20)
print("Sum:", result)


# Function to calculate square
def square(number):
    return number * number


print("Square:", square(5))


# Function with a default parameter
def introduce(name, branch="ECE"):
    print("Name:", name)
    print("Branch:", branch)


introduce("Anjali")
introduce("Rahul", "CSE")


# Function to check even or odd
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


print("10 is:", check_even_odd(10))
print("7 is:", check_even_odd(7))
