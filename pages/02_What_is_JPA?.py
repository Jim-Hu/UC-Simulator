import streamlit as st
import pandas as pd
import numpy as np
from streamlit_extras.switch_page_button import switch_page

# Set page configuration
st.set_page_config(page_title="UC Simulator", page_icon="🚀", layout="wide",initial_sidebar_state="expanded" )

st.header("What is JPA?",divider='rainbow')

# Markdown message to hint users about metrics in the sidebar
st.markdown("""
    ### 👈 Check out your ranking on the left
    As you build you application, you will see your ranking evolving... ♠️♥️♠️♦️
    """)

st.markdown("Jim：我迟些再回来优化，我需要做两个col，左边放metric，右边展示解释，按钮也要改")
# Main page explanation
st.markdown("""
   ### Metrics Explained:
    
    - **JPA (Jommie Point Average)**: This represents a weighted score out of 5.0, factoring in your GPA, AP courses, extracurricular activities, essays, and more. It's converted into a J-Score for an overall impression of your application's strength.
    
    - **UC Applicant Rank**: This shows where you stand among all applicants to the UC system based on your JPA.
    
    - **Your School Rank**: Local context matters in UC admissions. This rank compares you to peers at your own school.
    
    - **UC Campus Acceptance Chance**: Your likelihood of admission at each UC campus, derived from your statewide and school-specific rankings.
    
    Ready to improve your application? Let's move on to detailing your coursework.

    **Proceed to the next step to enter your course selection details.**
    """)

# Initialize sidebar
sidebar = st.sidebar

# Sidebar header
sidebar.header("Your Current Ranking")

# Metrics in the sidebar
sidebar.metric("JPA", "3.85", "J-score: 87/100", delta_color='off')
sidebar.metric("UC Applicants", "Top 8%", "1,300/68,893")
sidebar.metric("Valley Christian High School", "Top 5%", "2/40 Applicants")

# Divider
sidebar.markdown("---")

# Sidebar subheader for UC campuses
sidebar.subheader("UC Campuses Acceptance Rates")

# Titles for each UC campus and their corresponding metrics
uc_campuses = {
    "Berkeley": "15%",
    "Davis": "12%",
    "Irvine": "10%",
    "UCLA": "18%",
    "Merced": "5%",
    "Riverside": "8%",
    "San Diego": "16%",
    "Santa Barbara": "14%",
    "Santa Cruz": "7%"
}

# Display each UC campus metric in the sidebar
for campus, percentage in uc_campuses.items():
    sidebar.metric(f"{campus}", f"{percentage}")

# Another divider
sidebar.markdown("---")

# Button to move to the Course Selection page
if st.button('Proceed to Course Selection',type='primary'):
    # Assuming 'switch_page' function exists and 'page' is a session state or parameter
    switch_page('Course Selection')


st.write(st.session_state.user_data.to_dict())