import streamlit as st

# create a text input box
text_input = st.text_input('Enter some text')

# create a submit button
if st.button('Submit'):
    st.write("You 've inputted", text_input)