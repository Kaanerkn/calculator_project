number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

print("Choose the operation you want to perform: ")
print("1 - Addition")
print("2 - Subtraction")
print("3 - Multiplication")
print("4 - Division")

operation = input("Enter your choice (1/2/3/4): ")

if operation == "1":
    print("Result", number1 + number2)
elif operation == "2":
    print("Result", number1 - number2)
elif operation == "3":
    print("Result", number1 * number2)
elif operation == "4":
    if number2 != 0:
        print("Result", number1 / number2)
    else:
        print("Error : Cannot divide by zero!!")
else:
    print("Invalid selection.")
