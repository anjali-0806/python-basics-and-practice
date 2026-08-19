# Ternary Operator in Python

# Basic syntax:
# value_if_true if condition else value_if_false

age = 20

status = "Adult" if age >= 18 else "Minor"
print(status)


# Example 2: Even or Odd
num = 7

result = "Even" if num % 2 == 0 else "Odd"
print(result)


# Example 3: Find the smaller number
a = 10
b = 20

minimum = a if a < b else b
print("Minimum:", minimum)


# Example 4: Pass or Fail
marks = 75

result = "Pass" if marks >= 40 else "Fail"
print(result)


# Example 5: Nested Ternary Operator
score = 85

grade = (
    "A" if score >= 90
    else "B" if score >= 80
    else "C" if score >= 70
    else "F"
)

print("Grade:", grade)
