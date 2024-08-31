# Task 1: Arithmetic Operations
print("\nTask 1: Arithmetic Operations")
a = 7  # assign integer value 7 to variable a
b = 4  # assign integer value 4 to variable b

# Perform arithmetic operations

# addition
print('Sum: ', a + b)  # Output: Sum: 11
# The above line adds the values of a and b and prints the result

# subtraction
print('Subtraction: ', a - b)   # Output: Subtraction: 3
# The above line subtracts the value of b from a and prints the result

# multiplication
print('Multiplication: ', a * b)  # Output: Multiplication: 28
# The above line multiplies the values of a and b and prints the result

# division
print('Division: ', a / b)  # Output: Division: 1.75
# The above line divides the value of a by b and prints the result

# floor division (integer division)
print('Floor Division: ', a // b)  # Output: Floor Division: 1
# The above line performs integer division of a by b and prints the result

# modulo (remainder)
print('Modulo: ', a % b)  # Output: Modulo: 3
# The above line calculates the remainder of a divided by b and prints the result

# a to the power b (exponentiation)
print('Power: ', a ** b)  # Output: Power: 2401
# The above line calculates the value of a raised to the power of b and prints the result

# Task 2: Integer Literals with Underscores
print("\nTask 2: Integer Literals with Underscores")
num1 = 25_000_000  # with underscores
# The above line assigns an integer value to num1 using underscores for readability
num2 = 25000000  # without underscores
# The above line assigns the same integer value to num2 without using underscores

# Print num1 and num2 on two separate lines
print(num1)
print(num2)

# Task 3: Data Types
print("\nTask 3: Data Types")
num1 = 5
# The above line reassigns the value of num1 to 5
print(num1, 'is of type', type(num1))
# The above line prints the value and data type of num1

num2 = 2.0
# The above line assigns a floating-point value to num2
print(num2, 'is of type', type(num2))
# The above line prints the value and data type of num2

num3 = 1+2j
# The above line assigns a complex number value to num3
print(num3, 'is of type', type(num3))
# The above line prints the value and data type of num3
