import streamlit
streamlit.title('My Healthy Foods')
streamlit.header('My Favorites')
streamlit.text('🍳🍳 Eggs 🍳🍳')
streamlit.text('🌮🌮  Taco 🌮🌮')
streamlit.text('🍗🍗 Meat 🍗🍗')
streamlit.text('🍕🍕 Pizza 🍕🍕')
streamlit.text('🍔 Burgers 🍔🍔')
streamlit.title('My smoothies')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.multiselect("pick some fruits:",list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)
