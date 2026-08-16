# Python Loops

# For loop
print("For loop:")

for i in range(1, 6):
    print(i)


# Printing even numbers
print("\nEven numbers:")

for i in range(2, 11, 2):
    print(i)


# While loop
print("\nWhile loop:")

count = 1

while count <= 5:
    print(count)
    count += 1


# Sum of numbers
print("\nSum of numbers:")

total = 0

for i in range(1, 11):
    total += i

print("Sum:", total)
