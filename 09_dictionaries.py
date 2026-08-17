# Python Dictionaries

# Creating a dictionary
student = {
    "name": "Anjali",
    "age": 21,
    "branch": "ECE",
    "college": "NIT Srinagar"
}

print("Student information:")
print(student)

# Accessing values
print("\nName:", student["name"])
print("Age:", student["age"])
print("Branch:", student["branch"])

# Adding a new key-value pair
student["year"] = 3

print("\nAfter adding year:")
print(student)

# Changing a value
student["age"] = 22

print("\nAfter updating age:")
print(student)

# Removing an item
student.pop("year")

print("\nAfter removing year:")
print(student)

# Getting all keys
print("\nKeys:")
print(student.keys())

# Getting all values
print("\nValues:")
print(student.values())

# Loop through dictionary
print("\nStudent details:")

for key, value in student.items():
    print(key, ":", value)

# Checking if a key exists
print("\nIs name present?", "name" in student)
