import streamlit as st
# from rich.table import Column
#
# col1, col2, col3, col4, col5 = st.columns(5, gap="small", vertical_alignment="center")
#
# with col1:
#     st.header("Column 1")
#     st.write("Content for column 1")
#
# with col2:
#      st.header("Column 2")
#      st.write("Content for column 2")
#
# with col3:
#     st.header("Column 3")
#     st.write("Content for column 3")
#
# with col4:
#     st.header("Column 4")
#     st.write("Content for column 4")
#
# with col5:
#     st.header("Column 5")
#     st.write("Content for column 5")

with st.form("my_form", clear_on_submit=True):
    name = st.text_input('Name')
    age = st.slider('Age')
    email = st.text_input('Email')
    biography = st.text_area('Bio')
    terms = st.checkbox('I agree to the terms an conitions')
    submit_button = st.form_submit_button(label='submit')

    st.write(f"Name {name}")

if submit_button:
    st.write(f"age {age}")
    st.write(f"email {email}")
    st.write(f"Short bio {biography}")

else:
    st.write('You did agree with the terms and conditions')
    st.write('You did not agree with the terms and condition')


tab1, tab2, tab3 = st.tabs(["Tab1", "Tab2", "Tab3"])

with tab1:
    st.header("This is tab1")
    st.write("Content for tab1")

with tab2:
    st.header("This is tab2")
    st.write("Content for tab2")

with tab3:
    st.header("This is tab3")
    st.write("Content for tab3")

