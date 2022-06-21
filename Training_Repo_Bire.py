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
my_fruit_list = my_fruit_list.set_index('Fruit')
Fruits_Selecetd = streamlit.multiselect("pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
Fruit_to_show = my_fruit_list.loc[Fruits_Selecetd]
streamlit.dataframe(Fruit_to_show)
import requests
streamlit.title('Fruityvice Fruit advice')
Fruit_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(Fruit_response.json())
Fruit_Normalize = pandas.json_normalize(Fruit_response.json())
streamlit.dataframe(Fruit_Normalize)
