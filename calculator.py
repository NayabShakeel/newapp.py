import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Scientific Calculator
def scientific_calculator():
    st.header("Scientific Calculator")
    
    operation = st.selectbox("Choose an operation", 
                             ["Addition", "Subtraction", "Multiplication", "Division", "Square Root"])
    
    if operation in ["Addition", "Subtraction", "Multiplication", "Division"]:
        num1 = st.number_input("Enter first number", value=0.0)
        num2 = st.number_input("Enter second number", value=0.0)
        
        if operation == "Addition":
            result = num1 + num2
        elif operation == "Subtraction":
            result = num1 - num2
        elif operation == "Multiplication":
            result = num1 * num2
        elif operation == "Division":
            result = num1 / num2 if num2 != 0 else "Error! Division by zero."
        
        st.write(f"Result: {result}")
    
    elif operation == "Square Root":
        num = st.number_input("Enter a number", value=0.0)
        result = np.sqrt(num)
        st.write(f"Result: {result}")

# Graphical Calculator
def graphical_calculator():
    st.header("Graphical Calculator")
    
    expression = st.text_input("Enter a function (e.g., x**2, sin(x))", value="x**2")
    
    if expression:
        x = sp.symbols('x')
        expr = sp.sympify(expression)
        
        # Generate values for plotting
        x_vals = np.linspace(-10, 10, 400)
        y_vals = [expr.subs(x, val) for val in x_vals]
        
        # Plot the function
        plt.figure(figsize=(10, 5))
        plt.plot(x_vals, y_vals, label=str(expr))
        plt.title(f"Graph of {expr}")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.axhline(0, color='black',linewidth=0.5, ls='--')
        plt.axvline(0, color='black',linewidth=0.5, ls='--')
        plt.grid(True)
        plt.legend()
        
        st.pyplot(plt)

# Main Streamlit App
def main():
    st.title("Scientific & Graphical Calculator")
    
    calculator_type = st.sidebar.selectbox("Choose Calculator Type", ["Scientific", "Graphical"])
    
    if calculator_type == "Scientific":
        scientific_calculator()
    elif calculator_type == "Graphical":
        graphical_calculator()

if __name__ == "__main__":
    main()
