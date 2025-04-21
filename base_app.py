import streamlit as st

st.title("My First App")

name = st.text_input("What's your name?")

if name:
  st.write(f"Hello, {name}!")
