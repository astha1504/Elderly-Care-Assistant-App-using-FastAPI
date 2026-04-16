import streamlit as st

# Title of the app
st.title("Elderly Care Assistant App")

# Introduction
st.write("Welcome to the Elderly Care Assistant App! This app is designed to assist elderly individuals with their daily tasks and provide useful resources.")

# User Input Section
st.header("User Information")
name = st.text_input("Enter your name:")
age = st.number_input("Enter your age:", min_value=0)

# Services Section
st.header("Available Services")
services = ["Medication Reminder", "Emergency Contact", "Daily Check-in", "Meal Suggestions", "Transportation Assistance"]
selected_service = st.selectbox("Select a service to get more information:", services)

# Display information based on selected service
if selected_service == "Medication Reminder":
    st.write("This feature will remind you to take your medications at the scheduled times. You can also add your medication details.")
elif selected_service == "Emergency Contact":
    st.write("In case of an emergency, this feature allows you to contact your loved ones or caregivers quickly.")
elif selected_service == "Daily Check-in":
    st.write("This feature allows caregivers to check in on you daily to ensure your well-being.")
elif selected_service == "Meal Suggestions":
    st.write("Get meal suggestions based on your dietary preferences and health requirements.")
elif selected_service == "Transportation Assistance":
    st.write("This feature can help you arrange transportation for medical appointments or social events.")

# Footer
st.write("Thank you for using the Elderly Care Assistant App!")