import streamlit as st

# Streamlit UI
st.title("Power Calculator")
st.write("Enter a number to caculate its square, cube, fifth power.")

# Get uesr input
n = st.number_input("Write an integer", value=1, step=1)

# Calculate Results
square = n ** 2
cube = n ** 3
fifth_power = n ** 5

# Display Results
st.write(f"The square of {n} is: {square}")
st.write(f"The cube of {n} is: {cube}")
st.write(f"The fifth_power of {n} is: {fifth_power}")


