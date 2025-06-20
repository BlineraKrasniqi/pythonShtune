import pandas as pd
import streamlit as st
import plotly.express as px


st.header("Display Data Frame")

df = pd.DataFrame({
    'name': ['Liron', 'Morea', 'Arteida'],
    'age': [20, 16, 18],
    'city': ['New York', 'Miami', 'London']
})
st.write(df)

# Make sure the file path is correct and the CSV file exists
books_df = pd.read_csv('lesson18/bestsellers_with_categories_2022_03_27.csv')
st.title("Best Selling Books on Amazon")
st.write("This app shows the best selling books from the Amazon store")

st.sidebar.header("Add New Book Data")
with st.sidebar.form("book_form"):
    new_name = st.text_input("Book Name")
    new_author = st.text_input("Author Name")
    new_user_rating = st.slider("User Rating", 0.5, 5.0, 0.0, 0.1)
    new_review = st.number_input("Review", min_value=0, step=1)
    new_price = st.number_input("Price", min_value=0, step=1)
    new_year = st.number_input("Year", min_value=2009, max_value=2022, step=1)
    new_Genre = st.selectbox("Genre", books_df['Genre'].unique())
    submit_button = st.form_submit_button(label="Add Book")

if submit_button:
    new_data = {
        'Name': new_name,
        'Author': new_author,
        'User Rating': new_user_rating,
        'Review': new_review,
        'Price': new_price,
        'Year': new_year,
        'Genre': new_Genre
    }

st.subheader("Summary Statistics")
quantity = books_df.shape[0]
title = books_df['Name'].nunique()
rating = books_df['User Rating'].mean()
price = books_df['Price'].mean()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Books", quantity)
col2.metric("Titles", title)
col3.metric("Average Rating", f"{rating:.2f}")
col4.metric("Average Price", f"${price:.2f}")

st.subheader("Dataset Preview")
st.write(books_df.head())

col1, col2 = st.columns(2)
with col1:
    st.subheader("Top 10 Book Titles")
    top_titles = books_df['Name'].value_counts().head(10)
    st.bar_chart(top_titles)

with col2:
    st.subheader("Top 10 Authors")
    top_authors = books_df['Author'].value_counts().head(10)
    st.bar_chart(top_authors)

st.subheader("Genre Distribution")


fig = px.pie(books_df, names='Genre', title='Most Liked Genre (2009 - 2022)', color='Genre',
             color_discrete_sequence=px.colors.sequential.Plasma)
st.plotly_chart(fig)

st.subheader("Number of Fiction vs Non-Fiction Books over the Years")
size = books_df.groupby(['Year', 'Genre']).size().reset_index(name="Count")
fig = px.bar(size, x='Year', y='Count',color='Genre' , title="Number of Fiction vs Non-Fiction Books from 2009-2022",
             color_discrete_sequence=px.colors.sequential.Plasma, barmode='group')
st.plotly_chart(fig)

st.header('Top 15 Authors by Count of Books over the Years')
top_authors = books_df['Author'].value_counts().head(15).reset_index()
top_authors.columns = ['Author', 'Count']
fig = px.bar(top_authors, x='Count', y='Author', orientation='h',
             title='Top 15 Authors by Count of Books Published',
             labels={'Count': 'Count of Books Published', 'Author': 'Author'},
             color='Count', color_continuous_scale=px.colors.sequential.Plasma)
st.plotly_chart(fig)
st.subheader("Filter Data by Genre")
genre_filter = st.selectbox('Select Genre', books_df['Genre'].unique())
filter_df = books_df[books_df['Genre'] == genre_filter]
st.write(filter_df)