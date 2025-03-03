import streamlit as st
from deep_translator import GoogleTranslator
from helpers import convert_units, get_conversion_fact
import sys

# Streamlit UI with Dark/Light Mode
st.set_page_config(page_title="Google Unit Converter", layout="wide")
st.title("🔄 Google Unit Converter")

# 🌙 Dark Mode Toggle
dark_mode = st.sidebar.checkbox("🌙 Dark Mode")
if dark_mode:
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #1E1E1E !important;
            color: white !important;
        }
        [data-testid="stHeader"] {
            background-color: #1E1E1E !important;
            color: white !important;
        }
        header, footer {
            visibility: hidden;
            height: 0px;
            display: none;
        }
        .stSidebar .stSelectbox label, .stSidebar .stTextInput label, .stSidebar .stNumberInput label {
            color: white !important;
        }
        .stSelectbox label, .stTextInput label, .stNumberInput label, .stTextArea label {
            color: white !important;
        }
        .stSidebar, .stSelectbox, .stTextInput, .stNumberInput, .stTextArea {
            background-color: #2A2A2A !important;
            color: white !important;
        }
        .stButton>button {
            background-color: #bb86fc !important;
            color: white !important;
            border-radius: 5px;
        }
        ::-webkit-scrollbar {
            width: 10px;
        }
        ::-webkit-scrollbar-track {
            background: #333;
        }
        ::-webkit-scrollbar-thumb {
            background: #bb86fc;
            border-radius: 5px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: #9b67e5;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

# 🌍 Language Selection
st.sidebar.header("🌍 Select Language")
language = st.sidebar.selectbox("Choose Language", ["English", "Urdu", "Hindi", "Spanish", "French"])

# 🔢 Unit Categories
categories = {
    "Area": ["sq meters","sq kilometers", "sq miles", "sq yards", "sq feet", "hectares", "acres"],
    "Data Transfer Rate": ["bps", "kbps", "mbps", "gbps", "gbps", "tbps"],
    "Energy": ["joules", "watts", "watt-hours", "calories", "kilowatt-hours"],
    "Length": ["km", "miles", "meters", "feet", "inches", "centimeters", "millimeters","nanometers","yard"],
    "Mass": ["kg", "lbs", "grams", "ounces",'milligrams','micrograms',"tons"],
    "Pressure": ["pascals", "atm", "bar"],
    "Speed": ["mps", "kph", "mph","fps"],
    "Temperature": ["celsius", "fahrenheit", "kelvin"],
    "Time": ["seconds", "minutes","nanoseconds","microseconds", "hours", "days","weeks","months","years","century"],
    "Volume": ["liters","milliliters", "gallons", "cups"],
}

category = st.selectbox("📏 Select a category", list(categories.keys()))
unit_from = st.selectbox("🔄 Convert from", categories[category])
unit_to = st.selectbox("🎯 Convert to", categories[category])
input_value = st.text_input("✏️ Enter value to convert")

# 🔘 Convert Button
if st.button("🔄 Convert"):
    if input_value:
        try:
            value = float(input_value)
            result = convert_units(value, unit_from, unit_to)
            if result:
                st.success(f"✅ Converted Value: {result} {unit_to}")
                st.sidebar.markdown(f"💡 **Fun Fact:** {get_conversion_fact(unit_from)}")
            else:
                st.error("❌ Invalid conversion format. Try again!")
        except ValueError:
            st.error("⚠️ Please enter a valid number.")
    else:
        st.warning("⚠️ Please enter a value before converting!")

