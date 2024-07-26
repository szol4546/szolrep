import streamlit as st

st.title("Welcome to My First Streamlit App.")

name = st.text_input("Seth:")

if name:
  st.write(f"Hello, {Seth}! Welcome to the app.")
