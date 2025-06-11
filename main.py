import streamlit as st

# Set page configuration
st.set_page_config(page_title="BMI Calculator", page_icon="💪", layout="centered")

# Custom CSS for professional styling
st.markdown("""
    <style>
        .main {
            background-color: #f0f2f6;
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        }
        h1, h2 {
            color: #333333;
        }
        .stButton>button {
            background-color: #0072ff;
            color: white;
            border-radius: 8px;
        }
    </style>
""", unsafe_allow_html=True)

# Title and subtitle
st.title("💪 BMI Calculator")
st.markdown("### Calculate your Body Mass Index easily and quickly!")

# Input section
with st.container():
    height = st.number_input("Enter your height in centimeters (cm):", min_value=50.0, max_value=300.0, value=170.0)
    weight = st.number_input("Enter your weight in kilograms (kg):", min_value=10.0, max_value=300.0, value=70.0)

# BMI calculation
if st.button("Calculate BMI"):
    height_m = height / 100
    bmi = weight / (height_m ** 2)
    st.success(f"✅ Your BMI is: **{bmi:.2f}**")

    # BMI category
    if bmi < 18.5:
        st.warning("You are underweight.")
    elif 18.5 <= bmi < 24.9:
        st.info("You have a normal weight.")
    elif 25 <= bmi < 29.9:
        st.warning("You are overweight.")
    else:
        st.error("You are obese.")
