import streamlit as st 

st.title("AI Web App")

st.divider()

st.write("Enter your prompt and get a helpful response")

prompt = st.text_input("Your Prompt:")

st.divider()

if prompt:
    st.snow()
    st.write(f"You entered: {prompt}")
