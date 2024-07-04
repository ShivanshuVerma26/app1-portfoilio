import streamlit as st
import send_email as se

st.header("Contact US")

with st.form(key="my-email-form"):
    email_address = st.text_input("Your email address")
    raw_message = st.text_area("Enter your message")
    message = f"""\
Subject: New email from the {email_address}
From: {email_address}
{raw_message}
"""
    button = st.form_submit_button("Submit")

    if button:
        se.sendemail(message)
        st.info("Your email is sent successfully!")
