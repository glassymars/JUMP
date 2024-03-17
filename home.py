import streamlit as st
import pickle

st.header("My first ML App")

with st.form("first_form"):
    n = st.number_input("Enter the price of the house")
    submitted = st.form_submit_button("Calculate Number of Bedrooms")

    if submitted:
        with open("model.dat", "rb") as f:
            model = pickle.load(f)
        output = model.predict([[n]])
        st.write(f"The number of bedrooms is: {int(output[0])}")