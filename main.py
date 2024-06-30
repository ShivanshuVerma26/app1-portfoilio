import streamlit as st


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

