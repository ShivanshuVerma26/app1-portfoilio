import os

import streamlit as st
import pandas as pa

import practice.emailUtility as emailUtil

st.header("Contact US")

options = pa.read_csv(os.path.abspath("practice/topics.csv"))

with st.form(key="myemailForm"):
    email_address = st.text_input("Enter your email address")
    option = st.selectbox("What topic do you want to discuss today?", options)
    raw_message = st.text_area("Enter your message here:")
    button = st.form_submit_button("Submit")

    if button:
        message = f"""\
Subject: New email from Company App!
From: {email_address}
{raw_message}
"""
        emailUtil.sendemail(message)
        st.info("Your email is sent successfully!")
