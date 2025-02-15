import streamlit as st



def convert_weight(value, operation):
    if operation == "Pounds to Kilograms":
        result = value * 0.453592
    elif operation == "Kilograms to Pounds":
        result = value / 0.453592
    return result


def main():
    st.title("Weight Converter")


    value = st.number_input("Enter the weight", step=1)


    operation = st.radio("Select conversion", ['Pounds to Kilograms', 'Kilograms to Pounds'])


    result = convert_weight(value, operation)


    st.write(f"Result of {operation} for {value} is {result:.2f}")


if __name__ == "__main__":
    main()
