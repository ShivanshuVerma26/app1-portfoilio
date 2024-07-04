import streamlit as st


st.header("Contact US")

with st.form(key="my-email-form"):
    email_address = st.text_input("Your email address")
    email_message = st.text_area("Enter your message")
    button = st.form_submit_button("Submit")

    if button:
        print("I am pressed!")