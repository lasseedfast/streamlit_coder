"""
Number Calculator Example Script

This example demonstrates various number calculations using Streamlit.
It showcases basic arithmetic, advanced mathematical functions, and statistical operations.
"""

import streamlit as st
import math
import statistics
import numpy as np
import pandas as pd

def main():
    st.title("📊 Number Calculator Example")
    st.markdown("This example demonstrates various number calculations you can perform with Streamlit.")
    
    # Sidebar for navigation
    st.sidebar.title("Calculator Categories")
    calculation_type = st.sidebar.selectbox(
        "Choose calculation type:",
        ["Basic Arithmetic", "Advanced Math", "Statistics", "List Operations", "Scientific Calculator"]
    )
    
    if calculation_type == "Basic Arithmetic":
        basic_arithmetic()
    elif calculation_type == "Advanced Math":
        advanced_math()
    elif calculation_type == "Statistics":
        statistics_calculations()
    elif calculation_type == "List Operations":
        list_operations()
    elif calculation_type == "Scientific Calculator":
        scientific_calculator()

def basic_arithmetic():
    st.header("🔢 Basic Arithmetic Operations")
    
    col1, col2 = st.columns(2)
    
    with col1:
        num1 = st.number_input("Enter first number:", value=10.0, step=0.1)
    with col2:
        num2 = st.number_input("Enter second number:", value=5.0, step=0.1)
    
    st.subheader("Results:")
    
    # Display results in columns
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Addition", f"{num1 + num2:.2f}")
    with col2:
        st.metric("Subtraction", f"{num1 - num2:.2f}")
    with col3:
        st.metric("Multiplication", f"{num1 * num2:.2f}")
    with col4:
        if num2 != 0:
            st.metric("Division", f"{num1 / num2:.2f}")
        else:
            st.metric("Division", "Cannot divide by zero")
    
    # Additional operations
    st.subheader("Additional Operations:")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.write(f"**Modulo:** {num1 % num2 if num2 != 0 else 'N/A'}")
    with col2:
        st.write(f"**Power:** {num1 ** num2:.2f}")
    with col3:
        st.write(f"**Floor Division:** {num1 // num2 if num2 != 0 else 'N/A'}")

def advanced_math():
    st.header("🧮 Advanced Mathematical Functions")
    
    number = st.number_input("Enter a number:", value=16.0, step=0.1)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Power & Root Functions")
        st.write(f"**Square:** {number ** 2:.2f}")
        st.write(f"**Cube:** {number ** 3:.2f}")
        if number >= 0:
            st.write(f"**Square Root:** {math.sqrt(number):.2f}")
        else:
            st.write("**Square Root:** Not defined for negative numbers")
        st.write(f"**Cube Root:** {number ** (1/3):.2f}")
    
    with col2:
        st.subheader("Trigonometric Functions")
        angle_deg = st.number_input("Angle in degrees:", value=45.0, step=1.0)
        angle_rad = math.radians(angle_deg)
        
        st.write(f"**Sine:** {math.sin(angle_rad):.4f}")
        st.write(f"**Cosine:** {math.cos(angle_rad):.4f}")
        st.write(f"**Tangent:** {math.tan(angle_rad):.4f}")
    
    col3, col4 = st.columns(2)
    
    with col3:
        st.subheader("Logarithmic Functions")
        if number > 0:
            st.write(f"**Natural Log:** {math.log(number):.4f}")
            st.write(f"**Log Base 10:** {math.log10(number):.4f}")
            st.write(f"**Log Base 2:** {math.log2(number):.4f}")
        else:
            st.write("**Logarithms:** Not defined for non-positive numbers")
    
    with col4:
        st.subheader("Other Functions")
        st.write(f"**Absolute Value:** {abs(number):.2f}")
        st.write(f"**Ceiling:** {math.ceil(number)}")
        st.write(f"**Floor:** {math.floor(number)}")
        st.write(f"**Factorial:** {math.factorial(int(abs(number))) if number >= 0 and number.is_integer() and number <= 20 else 'N/A (too large or non-integer)'}")

def statistics_calculations():
    st.header("📈 Statistical Calculations")
    
    # Input methods
    input_method = st.radio("Choose input method:", ["Manual Entry", "Upload CSV", "Generate Random"])
    
    numbers = []
    
    if input_method == "Manual Entry":
        numbers_input = st.text_area(
            "Enter numbers (comma-separated):", 
            value="1, 2, 3, 4, 5, 6, 7, 8, 9, 10",
            help="Enter numbers separated by commas"
        )
        try:
            numbers = [float(x.strip()) for x in numbers_input.split(',') if x.strip()]
        except ValueError:
            st.error("Please enter valid numbers separated by commas")
            return
    
    elif input_method == "Upload CSV":
        uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file)
            st.write("Data preview:")
            st.dataframe(df.head())
            
            column = st.selectbox("Select column for analysis:", df.select_dtypes(include=[np.number]).columns)
            if column:
                numbers = df[column].dropna().tolist()
    
    elif input_method == "Generate Random":
        col1, col2, col3 = st.columns(3)
        with col1:
            count = st.number_input("Number of values:", min_value=5, max_value=1000, value=50)
        with col2:
            min_val = st.number_input("Minimum value:", value=1.0)
        with col3:
            max_val = st.number_input("Maximum value:", value=100.0)
        
        if st.button("Generate Random Numbers"):
            np.random.seed(42)  # For reproducibility
            numbers = np.random.uniform(min_val, max_val, count).tolist()
    
    if numbers:
        st.subheader("Statistical Results:")
        
        # Basic statistics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Count", len(numbers))
        with col2:
            st.metric("Mean", f"{statistics.mean(numbers):.2f}")
        with col3:
            st.metric("Median", f"{statistics.median(numbers):.2f}")
        with col4:
            if len(numbers) > 1:
                st.metric("Std Dev", f"{statistics.stdev(numbers):.2f}")
            else:
                st.metric("Std Dev", "N/A")
        
        # Additional statistics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Minimum", f"{min(numbers):.2f}")
        with col2:
            st.metric("Maximum", f"{max(numbers):.2f}")
        with col3:
            st.metric("Range", f"{max(numbers) - min(numbers):.2f}")
        with col4:
            st.metric("Sum", f"{sum(numbers):.2f}")
        
        # Visualization
        if len(numbers) > 1:
            st.subheader("Data Visualization:")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.write("**Histogram:**")
                st.bar_chart(pd.Series(numbers).value_counts().sort_index())
            
            with col2:
                st.write("**Line Chart:**")
                st.line_chart(numbers)

def list_operations():
    st.header("📋 List Number Operations")
    
    numbers_input = st.text_area(
        "Enter numbers (comma-separated):", 
        value="10, 25, 30, 15, 40, 35, 20",
        help="Enter numbers separated by commas"
    )
    
    try:
        numbers = [float(x.strip()) for x in numbers_input.split(',') if x.strip()]
    except ValueError:
        st.error("Please enter valid numbers separated by commas")
        return
    
    if numbers:
        st.subheader("List Operations:")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Original List:**")
            st.write(numbers)
            
            st.write("**Sorted (Ascending):**")
            st.write(sorted(numbers))
            
            st.write("**Sorted (Descending):**")
            st.write(sorted(numbers, reverse=True))
        
        with col2:
            st.write("**Cumulative Sum:**")
            cumsum = []
            running_total = 0
            for num in numbers:
                running_total += num
                cumsum.append(running_total)
            st.write(cumsum)
            
            st.write("**Squared Values:**")
            st.write([x**2 for x in numbers])
            
            st.write("**Above Average:**")
            avg = statistics.mean(numbers)
            above_avg = [x for x in numbers if x > avg]
            st.write(f"Average: {avg:.2f}")
            st.write(f"Values above average: {above_avg}")

def scientific_calculator():
    st.header("🔬 Scientific Calculator")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Constants")
        st.write(f"**π (Pi):** {math.pi:.6f}")
        st.write(f"**e (Euler's number):** {math.e:.6f}")
        st.write(f"**φ (Golden ratio):** {(1 + math.sqrt(5)) / 2:.6f}")
        st.write(f"**√2:** {math.sqrt(2):.6f}")
    
    with col2:
        st.subheader("Unit Conversions")
        value = st.number_input("Enter value to convert:", value=1.0)
        
        conversion_type = st.selectbox("Conversion type:", [
            "Degrees to Radians", "Radians to Degrees", 
            "Celsius to Fahrenheit", "Fahrenheit to Celsius",
            "Meters to Feet", "Feet to Meters"
        ])
        
        if conversion_type == "Degrees to Radians":
            result = math.radians(value)
            st.write(f"**{value}° = {result:.6f} radians**")
        elif conversion_type == "Radians to Degrees":
            result = math.degrees(value)
            st.write(f"**{value} rad = {result:.2f}°**")
        elif conversion_type == "Celsius to Fahrenheit":
            result = (value * 9/5) + 32
            st.write(f"**{value}°C = {result:.2f}°F**")
        elif conversion_type == "Fahrenheit to Celsius":
            result = (value - 32) * 5/9
            st.write(f"**{value}°F = {result:.2f}°C**")
        elif conversion_type == "Meters to Feet":
            result = value * 3.28084
            st.write(f"**{value} m = {result:.2f} ft**")
        elif conversion_type == "Feet to Meters":
            result = value / 3.28084
            st.write(f"**{value} ft = {result:.2f} m**")
    
    st.subheader("Complex Calculations")
    
    # Compound Interest Calculator
    with st.expander("💰 Compound Interest Calculator"):
        principal = st.number_input("Principal amount ($):", value=1000.0, min_value=0.0)
        rate = st.number_input("Annual interest rate (%):", value=5.0, min_value=0.0) / 100
        time = st.number_input("Time period (years):", value=10.0, min_value=0.0)
        compounds = st.number_input("Compounds per year:", value=12, min_value=1)
        
        if st.button("Calculate Compound Interest"):
            amount = principal * (1 + rate/compounds) ** (compounds * time)
            interest = amount - principal
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Final Amount", f"${amount:.2f}")
            with col2:
                st.metric("Interest Earned", f"${interest:.2f}")
    
    # Quadratic Equation Solver
    with st.expander("📐 Quadratic Equation Solver (ax² + bx + c = 0)"):
        a = st.number_input("Coefficient a:", value=1.0)
        b = st.number_input("Coefficient b:", value=-5.0)
        c = st.number_input("Coefficient c:", value=6.0)
        
        if st.button("Solve Quadratic Equation"):
            if a == 0:
                st.error("Coefficient 'a' cannot be zero for a quadratic equation")
            else:
                discriminant = b**2 - 4*a*c
                
                if discriminant > 0:
                    x1 = (-b + math.sqrt(discriminant)) / (2*a)
                    x2 = (-b - math.sqrt(discriminant)) / (2*a)
                    st.success(f"Two real solutions: x₁ = {x1:.4f}, x₂ = {x2:.4f}")
                elif discriminant == 0:
                    x = -b / (2*a)
                    st.success(f"One real solution: x = {x:.4f}")
                else:
                    real_part = -b / (2*a)
                    imaginary_part = math.sqrt(-discriminant) / (2*a)
                    st.success(f"Two complex solutions: x₁ = {real_part:.4f} + {imaginary_part:.4f}i, x₂ = {real_part:.4f} - {imaginary_part:.4f}i")

if __name__ == "__main__":
    main()