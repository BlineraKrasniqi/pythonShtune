def simple_calculator(number1, number2, operator):
    if operator == "+":
        return number1 + number2
    elif operator == "-":
        return number1 - number2
    elif operator == "*":
        return number1 * number2
    elif operator == "/":
        return number1 / number2 if number2 != 0 else "Error: Division by zero"
    else:
        return "Error: Invalid operator"


print(simple_calculator(10, 5, "+"))  # 15
print(simple_calculator(10, 0, "/"))  # Error: Division by zero
print(simple_calculator(10, 5, "*"))  # 50
