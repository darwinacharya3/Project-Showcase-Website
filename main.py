import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
col1,col2 = st.columns(2)

with col1:
    st.image("images/photo.png")
    
with col2:
    st.title("Darwin Acharya")
    content = """
    Hey, My name is Darwin Acharya, and I am currently pursuing a
    bachelor's degree in Electronics Communication and Information
    Engineering at the Advanced College of Engineering and Management
    in Kathmandu, Nepal. I have a strong passion for learning,
    especially in coding and technology, and I enjoy exploring
    new ideas. Although I am still in the early stages of my career,
    I aspire to build a future in engineering, focusing on machine
    learning, deep learning, and artificial intelligence. I'm excited 
    about the innovative opportunities these fields present as I continue
    my studies and embrace new challenges.
    """
    st.info(content)
    
content2 = """
Below you can find some of the apps that I have built in python. 
Feel free to contact me!!"""    
st.info(content2)

col3,empty_col,col4 = st.columns([1.5,0.5,1.5])

df = pd.read_csv("data.csv",sep=";")

with col3:
    for index,row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/" + row['image'])
        st.write(f"[Source Code({row['url']})]")
        
with col4:
    for index,row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/" + row['image'])
        st.write(f"[Source Code({row['url']})]")
    
