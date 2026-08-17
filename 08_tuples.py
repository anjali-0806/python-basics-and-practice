# Python Tuples

# Creating a tuple
fruits = ("apple", "banana", "mango", "orange")

print("Fruits:", fruits)

# Accessing elements
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Length
print("Number of fruits:", len(fruits))

# Loop through a tuple
print("\nAll fruits:")

for fruit in fruits:
    print(fruit)

# Checking if an item exists
print("\nIs mango present?", "mango" in fruits)

# Tuple with numbers
numbers = (10, 20, 30, 40, 50)

print("\nNumbers:", numbers)
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sum:", sum(numbers))
