import streamlit as st
import pickle
import numpy as np

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

st.title("Turning Point Prediction App")

st.write("Enter match details to check whether it is a Turning Point or No Turning Point.")

# Input fields
over_number = st.number_input("Over Number", min_value=0, max_value=50, value=1)
ball_number = st.number_input("Ball Number", min_value=0, max_value=6, value=1)
cumulative_runs = st.number_input("Cumulative Runs", min_value=0, value=0)
cumulative_wickets = st.number_input("Cumulative Wickets", min_value=0, max_value=10, value=0)
current_run_rate = st.number_input("Current Run Rate", min_value=0.0, value=0.0)
wickets_in_hand = st.number_input("Wickets in Hand", min_value=0, max_value=10, value=10)

# Prediction
if st.button("Predict"):
    input_data = np.array([[over_number,
                            ball_number,
                            cumulative_runs,
                            cumulative_wickets,
                            current_run_rate,
                            wickets_in_hand]])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("Turning Point")
    else:
        st.error("No Turning Point")
