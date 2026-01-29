import streamlit as st
a = 10
b = 20
c = 35
d =45
result = a + b +c + d
# Streamlit app
st.title("Addition App")
st.text("Welcome")
st.write(f"The sum of {a} and {b} is: {result}")