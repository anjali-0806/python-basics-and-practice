# Python Lists

# Creating a list
fruits = ["apple", "banana", "mango", "orange"]

print("Fruits:", fruits)

# Accessing elements
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Adding an element
fruits.append("grapes")
print("After append:", fruits)

# Inserting an element
fruits.insert(1, "watermelon")
print("After insert:", fruits)

# Removing an element
fruits.remove("banana")
print("After remove:", fruits)

# Changing an element
fruits[0] = "pineapple"
print("After changing:", fruits)

# Length of list
print("Number of fruits:", len(fruits))

# Loop through a list
print("\nAll fruits:")

for fruit in fruits:
    print(fruit)

# Sorting a list
numbers = [5, 2, 8, 1, 9, 3]

numbers.sort()
print("\nSorted numbers:", numbers)

# Reverse a list
numbers.reverse()
print("Reversed numbers:", numbers)
