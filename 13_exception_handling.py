# Python Exception Handling

# Handling invalid input
try:
    number = int(input("Enter a number: "))
    print("You entered:", number)

except ValueError:
    print("Please enter a valid number.")


# Handling division by zero
try:
    a = int(input("\nEnter first number: "))
    b = int(input("Enter second number: "))

    result = a / b
    print("Result:", result)

except ZeroDivisionError:
    print("Cannot divide by zero.")

except ValueError:
    print("Please enter valid numbers.")


# try-except-else-finally
try:
    number = int(input("\nEnter another number: "))

except ValueError:
    print("Invalid input.")

else:
    print("Valid number:", number)

finally:
    print("Program execution completed.")
