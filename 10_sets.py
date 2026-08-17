# Python Sets

# Creating a set
fruits = {"apple", "banana", "mango", "orange"}

print("Fruits:", fruits)

# Duplicate values are removed
numbers = {1, 2, 2, 3, 4, 4, 5}

print("Numbers:", numbers)

# Adding an element
fruits.add("grapes")
print("After adding:", fruits)

# Removing an element
fruits.remove("banana")
print("After removing:", fruits)

# Checking if an element exists
print("Is mango present?", "mango" in fruits)

# Set operations
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("\nSet A:", A)
print("Set B:", B)

# Union
print("Union:", A | B)

# Intersection
print("Intersection:", A & B)

# Difference
print("A - B:", A - B)
print("B - A:", B - A)
