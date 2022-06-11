import streamlit as st
from multiapp import MultiApp
from apps import number1, number2

app = MultiApp()

st.markdown("""
# Merkle (Dentsu International) Test

Data from [bigquery-public-data.covid19_open_data.covid19_open_data](https://console.cloud.google.com/marketplace/product/bigquery-public-datasets/covid19-open-data).
""")

# Add all your application here
app.add_app("Answer Number 1", number1.app)
app.add_app("Answer Number 2", number2.app)
# The main app
app.run()
