# Python File Handling

# Writing to a file
with open("sample.txt", "w") as file:
    file.write("Hello, Python!\n")
    file.write("I am learning file handling.")


# Reading from a file
with open("sample.txt", "r") as file:
    content = file.read()

print("File content:")
print(content)


# Appending to a file
with open("sample.txt", "a") as file:
    file.write("\nThis line was added later.")


# Reading the updated file
with open("sample.txt", "r") as file:
    content = file.read()

print("\nUpdated file content:")
print(content)
