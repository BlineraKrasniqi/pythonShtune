import streamlit as st

def calculate(num1, num2, operation):
    if operation == "Addition":
        result = num1 + num2
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
        try:
            result = num1 / num2
        except ZeroDivisionError:
    return result

def main():
    st.title("Simple Calculator")
    num1 = st.number_input("Enter the first number", step=1)
    num2 = st.number_input("Enter the second number", step=1)

    result = calculate(num1, num2, operation)

    st.write(f"Result of the {operation} of {num1} and {num2} is {result}")

if __name__ == "__main__":
    main()
