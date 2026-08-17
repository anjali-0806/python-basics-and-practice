# Python Strings

name = "Anjali"
message = "Python is fun to learn!"

# Printing strings
print("Name:", name)
print("Message:", message)

# String length
print("Length of name:", len(name))

# Accessing characters
print("First character:", name[0])
print("Last character:", name[-1])

# String slicing
print("First three characters:", name[0:3])

# Changing case
print("Uppercase:", name.upper())
print("Lowercase:", name.lower())

# Removing extra spaces
text = "   Hello Python   "
print("Stripped:", text.strip())

# Replacing text
print("Replaced:", message.replace("fun", "interesting"))

# Checking text
print("Contains Python:", "Python" in message)

# Joining strings
first_name = "Anjali"
last_name = "Rajpoot"

full_name = first_name + " " + last_name
print("Full name:", full_name)

# f-string
age = 21
print(f"{full_name} is {age} years old.")
