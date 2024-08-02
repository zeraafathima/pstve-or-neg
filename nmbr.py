import streamlit as st
st.title('positive or negative')
st.header('find out positive or negative')
x=st.number_input(label='enter the number')

clicked=st.button('submit')
if clicked:
    if x>=0:
        st.subheader('positive numbers')
    else:
        st.subheader('negative numbers')