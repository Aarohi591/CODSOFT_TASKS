# CodSoft Python Programming Internship
# Task 2: Calculator

def calculator():
    print("\n==============================")
    print("        CALCULATOR")
    print("==============================")

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        print("\nChoose an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            result = num1 + num2
            print(f"\nResult: {num1} + {num2} = {result}")

        elif choice == "2":
            result = num1 - num2
            print(f"\nResult: {num1} - {num2} = {result}")

        elif choice == "3":
            result = num1 * num2
            print(f"\nResult: {num1} * {num2} = {result}")

        elif choice == "4":
            if num2 == 0:
                print("\nError: Cannot divide by zero.")
            else:
                result = num1 / num2
                print(f"\nResult: {num1} / {num2} = {result}")

        else:
            print("\nInvalid operation choice.")

    except ValueError:
        print("\nError: Please enter valid numbers.")


calculator()
