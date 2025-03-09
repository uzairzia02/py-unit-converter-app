import streamlit as st

st.title("🔄 Unit Converter App")
st.markdown("### Convert Length, Weight, and Time Instantly!")
st.write("Welcome to the Unit Converter App. Enter the value and convert it instantly")

category = st.selectbox("⚙️ Select a conversion type", ["Length", "Weight", "Time"])

def convertUnits(category, value, unit):
    if category == "Length":
        if unit == "Kilometers to Miles":
            return value * 0.621371
        elif unit == "Miles to Kilometers":
            return value / 0.621371
    elif category == "Weight":
        if unit == "Kilograms to Pounds":
            return value * 2.20462
        elif unit == "Pounds to Kilograms":
            return value / 2.20462
    elif category == "Time":
        if unit == "Seconds to Minutes":
            return value / 60
        elif unit == "Minutes to Hours":
            return value / 60
        elif unit == "Hours to Days":
            return value / 24
        elif unit == "Days to Hours":
            return value * 24

if category == "Length":
    st.markdown("## Length Conversion")
    unit = st.selectbox("Select a unit", ["Kilometers to Miles", "Miles to Kilometers"])
elif category == "Weight":
    st.markdown("## Weight Conversion")
    unit = st.selectbox("Select a unit", ["Kilograms to Pounds", "Pounds to Kilograms"])
elif category == "Time":
    st.markdown("## Time Conversion")
    unit = st.selectbox("Select a unit", ["Seconds to Minutes", "Minutes to Hours", "Hours to Days", "Days to Hours"])

value = st.number_input("## Enter a value to convert")
if st.button("Convert"):
    result = convertUnits(category, value, unit)
    st.write(f"## ✅ Result : {result:.2f}")

