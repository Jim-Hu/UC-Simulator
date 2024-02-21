import streamlit as st

st.set_page_config(
    page_title="About You",
    page_icon="👋",
)

import streamlit as st


# About You
st.title("About You")

# First and Last Name in a two-column layout
col1, col2 = st.columns(2)
with col1:
    first_name = st.text_input("First Name", "", help="Enter your first name")
with col2:
    last_name = st.text_input("Last Name", "", help="Enter your last name")

# High School Type Radio Buttons
st.radio("High School Type",
         options=["High School in California", "High School out of California", "International High School"],
         index=1)  # Default to second option

# School Name (in California) Select box
st.selectbox("School Name (in California)",
             options=["Option 1", "Option 2", "Option 3"])

# Campuses & Majors
st.text("Campuses & Majors")

# Intended UC Campus for Admission Simulation
st.multiselect("Intended UC Campus for Admission Simulation",
               options=["UC Berkeley", "UC Davis", "UC Irvine", "UCLA", "UC Merced",
                        "UC Riverside", "UC San Diego", "UC Santa Barbara", "UC Santa Cruz"])

# Intended Major
st.text_input("Intended major", "", help="i.e. Chemistry or Undeclared")

# Academic
st.text("Academic")

# Weighted GPA in 10th and 11th Grade (Sophomore & Junior)
col1, col2, col3 = st.columns([3, 1, 1])  # Adjust the middle column width as needed
with col1:  # This places the slider in the middle column, effectively controlling its width
    GPA = st.slider("Weighted GPA in 10th and 11th Grade (Sophomore & Junior)",
              min_value=2.6, max_value=5.0, value=5.0, step=0.01)

# Next: Courses Taken
st.text("Next: Courses Taken")
