import streamlit as st
from numpy.random import choice


def main():
    st.title("Welcome!!")


if __name__ == '__main__':
    main()

if st.button("Click here"):
    st.write("Button clicked")

    st.checkbox("Check me!!")

if st.checkbox("Check me!!"):
    st.write("You are here because you clicked the button ")

user_input = st.text_input("Enter text", "Sheno nje tekst")
st.write("You entered", user_input)

age = st.number_input("Enter your age", min_value=1, max_value=100)
st.write(f"You are {age} years old")


message = st.text_area("Enter a text")
st.write(f"You typed {message}")

choice= st.radio("Pick a choice", ['Choice 1', 'Choice 2', 'Choice 3'])
st.write(f"You chose:{choice}")

if st.button("Success")
    st.success("It was senr successfully")

try:
    1 / 0

except Exception as e
    st.Exception(e)