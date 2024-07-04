import os

import streamlit as st
import pandas as p

st.set_page_config(layout="wide")

st.header("The Best Company")
st.write("My first developed webiste for a company!")

st.subheader("Our Team")
col1, empty_col1, col2, empty_col2, col3 = st.columns([1.5, 0.5, 1.5, 0.5, 1.5])

df = p.read_csv(os.path.abspath("practice/data.csv"), sep=",")

with col1:
    for index, row in df[0:3].iterrows():
        st.subheader(row["first name"].title() + " " + row["last name"].title())
        st.write(row["role"])
        st.image(os.path.abspath("practice/images/"+row["image"]))

with col2:
    for index, row in df[4:7].iterrows():
        st.subheader(row["first name"].title() + " " + row["last name"].title())
        st.write(row["role"])
        st.image(os.path.abspath("practice/images/"+row["image"]))

with col3:
    for index, row in df[8:].iterrows():
        st.subheader(row["first name"].title() + " " + row["last name"].title())
        st.write(row["role"])
        st.image(os.path.abspath("practice/images/"+row["image"]))
