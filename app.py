import streamlit as st
import pickle
import numpy as np

# Load the trained model
model = pickle.load(open('milkpred.pkl', 'rb'))

st.title('Milk Quality Prediction App')

# Input fields with proper ranges and types
ph = st.number_input('pH', min_value=3.0, max_value=10.0, value=6.6, format="%.2f")
temperature = st.number_input('Temperature (°C)', min_value=30, max_value=100, value=35, step=1)
taste = st.radio('Taste (0 = No, 1 = Yes)', options=[0, 1], index=1)
odor = st.radio('Odor (0 = No, 1 = Yes)', options=[0, 1], index=0)
fat = st.radio('Fat (0 = No, 1 = Yes)', options=[0, 1], index=1)
turbidity = st.radio('Turbidity (0 = No, 1 = Yes)', options=[0, 1], index=0)
colour = st.number_input('Colour Value', min_value=240, max_value=260, value=254, step=1)

if st.button('Predict'):
    features = np.array([[ph, temperature, taste, odor, fat, turbidity, colour]])
    prediction = model.predict(features)
    predicted_label_num = prediction[0]

    # Map integers back to grade strings
    label_map = {0: 'low', 1: 'medium', 2: 'high'}
    grade = label_map.get(predicted_label_num, 'Unknown')

    if grade == 'high':
        st.success(f'Predicted Milk Grade: {grade.upper()} 🟢')
    elif grade == 'medium':
        st.warning(f'Predicted Milk Grade: {grade.upper()} 🟡')
    elif grade == 'low':
        st.error(f'Predicted Milk Grade: {grade.upper()} 🔴')
    else:
        st.info(f'Predicted Milk Grade: {grade}')

