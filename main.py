import streamlit as st
import pandas as p

st.set_page_config(layout="wide")


col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg")

with col2:
    st.title("Shivanshu Verma")
    content = """
    I am Shivanshu Verma. I am aspring to become a data scientist. I am learning Pythin to start with.
    I have a long way to go to learn and master various other concepts.
    """
    st.info(content)


content2 = """
Below you can find more of my apps. Please contact me for any support!
"""
st.write(content2)

df = p.read_csv("data.csv", sep=";")

col3, col4 = st.columns(2)

with col3:
    for index, row in df[0:10].iterrows():
        st.header(row["title"])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])