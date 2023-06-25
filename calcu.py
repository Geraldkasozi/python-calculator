# Simple Python Calculator

# Function to perform addition
def add(num1, num2):
    return num1 + num2

# Function to perform subtraction
def subtract(num1, num2):
    return num1 - num2

# Function to perform division
def divide(num1, num2):
    return num1 / num2

# Function to perform multiplication
def multiply(num1, num2):
    return num1 * num2

# Main program
print("Welcome to the Simple Python Calculator!")

print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Division")
print("4. Multiplication")

choice = input("Enter your choice (1-4): ")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if choice == '1':
    result = add(num1, num2)
    operation = "+"
elif choice == '2':
    result = subtract(num1, num2)
    operation = "-"
elif choice == '3':
    result = divide(num1, num2)
    operation = "/"
elif choice == '4':
    result = multiply(num1, num2)
    operation = "*"
else:
    print("Invalid choice.")

print("Result: {} {} {} = {}".format(num1, operation, num2, result))
