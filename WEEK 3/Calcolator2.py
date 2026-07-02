print("-- MENU-DRIVEN CALCULATOR --")
print("1. Addition (+)")
print("2. Substraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("=================================================")

choice = input("Enter your choice (1-4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    result = num1 + num2
    print(f"Result: {num1} + {num2} = {result}")

elif choice == '2':
    result = num1 - num2
    print(f"Result: {num1} - {num2} = {result}")

elif choice == '3':
    result = num1 * num2
    print(f"Result: {num1} * {num2} = {result}")  

elif choice == '4':
    if num2 == 0:
        print("Error: Division by zero is not allowed.")

    else:
        result  = num1 / num2
        print(f"Result: {num1} / {num2} = {result}")

else:
    print("Invalid Choice! Please select a valid option from 1 to 4.")
    




   