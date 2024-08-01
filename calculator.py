print("Welcome to Simple Calculator!")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Available operations:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

# Take input from the user
choice = input("Enter operation number (1, 2, 3, 4): ")


if choice == '1':
    print(f"{num1} + {num2} = {num1 + num2}")
elif choice == '2':
    print(f"{num1} - {num2} = {num1 - num2}")
elif choice == '3':
    print(f"{num1} * {num2} = {num1 * num2}")
elif choice == '4':
    if num2 != 0:
        print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print("Error! Division by zero is not allowed")
else:
    print("Invalid choice. Please enter a valid operation number between 1 to 4.")


