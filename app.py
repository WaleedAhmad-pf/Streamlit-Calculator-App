import streamlit as st

# Streamlit app title
st.set_page_config(page_title="Simple Calculator", page_icon="🧮")
st.title("🧮 Simple Streamlit Calculator")

# Input numbers
st.subheader("Enter numbers:")
num1 = st.number_input("Enter first number", value=0.0, step=1.0)
num2 = st.number_input("Enter second number", value=0.0, step=1.0)

# Operation selection
st.subheader("Choose operation:")
operation = st.selectbox("Operation", ("Add", "Subtract", "Multiply", "Divide"))

# Perform calculation
if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
        st.success(f"The result of addition is: {result}")
    elif operation == "Subtract":
        result = num1 - num2
        st.success(f"The result of subtraction is: {result}")
    elif operation == "Multiply":
        result = num1 * num2
        st.success(f"The result of multiplication is: {result}")
    elif operation == "Divide":
        if num2 == 0:
            st.error("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
            st.success(f"The result of division is: {result}")

# Footer
st.markdown("---")
st.caption("Built with ❤️ using Streamlit")
