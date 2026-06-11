print('=' * 50)
print("🦸 Welcome to PyCalcHero 🦸")
print("Your Python-powered calculation assistant")
print('=' * 50)

print("Supports: Addition (+), Subtraction (-), Multiplication (*), Division (/)")
print("Type 'exit' to quit.\n")

while True:
    expression = input("Enter Expression: ")

    if expression.lower() == 'exit':
        print("Goodbye! Thanks for using PyCalcHero!")
        break

    try:
        allowed = "0123456789+-*/(). "

        if all(char in allowed for char in expression):
            result = eval(expression)
            print(f"Result: {result}")
        else:
            print("Error: Invalid characters")

    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

    except Exception:
        print("Error: Invalid expression. Please try again.")