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

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

with col3:
    for index, row in df[0:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source code]({row['url']})")