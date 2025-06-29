# import sys
# import streamlit as st
# st.write("Python version:", sys.version)

import streamlit as st
import numpy as np
import pickle


# Load the model using pickle
with open('xgb_energy_model.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("Household Energy Usage Predictor")

# Input fields
reactive_power = st.number_input("Global Reactive Power", value=0.2)
voltage = st.number_input("Voltage", value=235.0)
intensity = st.number_input("Global Intensity", value=5.0)
sub1 = st.number_input("Sub Metering 1", value=1.0)
sub2 = st.number_input("Sub Metering 2", value=1.0)
sub3 = st.number_input("Sub Metering 3", value=2.0)
hour = st.slider("Hour", 0, 23, 18)
day = st.slider("Day", 1, 31, 15)
weekday = st.slider("Weekday (0=Mon, 6=Sun)", 0, 6, 2)
month = st.slider("Month", 1, 12, 6)

# Predict button
if st.button("Predict Power Usage"):
    input_array = np.array([[reactive_power, voltage, intensity,
                             sub1, sub2, sub3, hour, day, weekday, month]])
    prediction = model.predict(input_array)[0]
    st.success(f"🔋 Predicted Global Active Power: {prediction:.4f} kW")
