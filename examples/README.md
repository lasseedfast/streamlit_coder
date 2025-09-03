# Examples

This directory contains example Streamlit scripts that demonstrate various functionality and serve as templates for users.

## Number Calculator Example

**File:** `number_calculator.py`

A comprehensive example script demonstrating number calculations and mathematical operations using Streamlit. This example showcases:

### Features:

#### 🔢 Basic Arithmetic Operations
- Addition, subtraction, multiplication, division
- Modulo, power, and floor division operations
- Interactive number inputs with real-time calculations

#### 🧮 Advanced Mathematical Functions
- Power and root functions (square, cube, square root, cube root)
- Trigonometric functions (sin, cos, tan)
- Logarithmic functions (natural log, log base 10, log base 2)
- Other mathematical functions (absolute value, ceiling, floor, factorial)

#### 📈 Statistical Calculations
- Multiple input methods (manual entry, CSV upload, random generation)
- Basic statistics (mean, median, standard deviation, min, max, range, sum)
- Data visualization (histograms and line charts)
- Support for data analysis from CSV files

#### 📋 List Number Operations
- List sorting (ascending/descending)
- Cumulative sum calculations
- Element transformations (squaring)
- Filtering operations (values above average)

#### 🔬 Scientific Calculator
- Mathematical constants (π, e, golden ratio, √2)
- Unit conversions (angles, temperature, distance)
- Complex calculations:
  - Compound interest calculator
  - Quadratic equation solver

### How to Run

```bash
streamlit run examples/number_calculator.py
```

### Technologies Used
- **Streamlit**: Web interface and widgets
- **NumPy**: Numerical computations
- **Pandas**: Data manipulation and CSV handling
- **Math**: Built-in mathematical functions
- **Statistics**: Statistical calculations

### Use Cases
This example can be used as:
- A template for mathematical applications
- An educational tool for learning Streamlit
- A reference for implementing calculations in web apps
- A starting point for scientific computing interfaces

### Key Streamlit Features Demonstrated
- `st.number_input()` for numerical inputs
- `st.selectbox()` and `st.radio()` for user choices
- `st.columns()` for layout organization
- `st.metric()` for displaying key metrics
- `st.file_uploader()` for file handling
- `st.expander()` for collapsible sections
- `st.bar_chart()` and `st.line_chart()` for visualization
- Session state management
- Error handling and user feedback