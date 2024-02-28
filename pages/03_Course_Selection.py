import streamlit as st
from streamlit_extras.switch_page_button import switch_page

# Set page configuration
st.set_page_config(page_title="UC Simulator", page_icon="🚀", layout="centered",initial_sidebar_state='expanded')

st.header("Course Selection",divider='rainbow')

st.markdown("description balbalbala")

# Use columns to layout the form for different academic years
col1, col2= st.columns(2)

# Freshmen Year
with col1:
    st.subheader("Freshmen Year")
    freshmen_courses = st.number_input("Number of Courses Taken", min_value=0, max_value=20, value=10, key="freshmen_courses")
    with st.expander("AP/IB/HL"):
        freshmen_ap_courses = st.number_input("Number of AP Courses Taken", min_value=0, max_value=20, value=0, key="freshmen_ap_courses")
        freshmen_honor_courses = st.number_input("Number of Honor Level Courses Taken", min_value=0, max_value=20, value=0, key="freshmen_honor_courses")
        freshmen_ib_courses = st.number_input("Number of IB Level Courses Taken", min_value=0, max_value=20, value=0, key="freshmen_ib_courses")

# Sophomore Year
with col2:
    st.subheader("Sophomore Year")
    sophomore_courses = st.number_input("Number of Courses Taken", min_value=0, max_value=20, value=10, key="sophomore_courses")
    with st.expander("AP/IB/HL"):
        sophomore_ap_courses = st.number_input("Number of AP Courses Taken", min_value=0, max_value=20, value=0, key="sophomore_ap_courses")
        sophomore_honor_courses = st.number_input("Number of Honor Level Courses Taken", min_value=0, max_value=20, value=0, key="sophomore_honor_courses")
        sophomore_ib_courses = st.number_input("Number of IB Level Courses Taken", min_value=0, max_value=20, value=0, key="sophomore_ib_courses")

col3, col4= st.columns(2)

# Junior Year
# Junior Year
with col3:
    st.subheader("Junior Year")
    junior_courses = st.number_input("Number of Courses Taken", min_value=0, max_value=20, value=10, key="junior_courses")
    with st.expander("AP/IB/HL"):
        junior_ap_courses = st.number_input("Number of AP Courses Taken", min_value=0, max_value=20, value=0, key="junior_ap_courses")
        junior_honor_courses = st.number_input("Number of Honor Level Courses Taken", min_value=0, max_value=20, value=0, key="junior_honor_courses")
        junior_ib_courses = st.number_input("Number of IB Level Courses Taken", min_value=0, max_value=20, value=0, key="junior_ib_courses")

# Senior Year
with col4:
    st.subheader("Senior Year (Planned)")
    senior_courses_planned = st.number_input("Number of Courses Planned", min_value=0, max_value=20, value=0, key="senior_courses_planned")
    with st.expander("AP/IB/HL"):
        senior_ap_courses_planned = st.number_input("Number of AP Courses Planned", min_value=0, max_value=20, value=0, key="senior_ap_courses_planned")
        senior_honor_courses_planned = st.number_input("Number of Honor Level Courses Planned", min_value=0, max_value=20, value=0, key="senior_honor_courses_planned")
        senior_ib_courses_planned = st.number_input("Number of IB Level Courses Planned", min_value=0, max_value=20, value=0, key="senior_ib_courses_planned")

# =====SIDEBAR===============
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
    switch_page('Test Score')
