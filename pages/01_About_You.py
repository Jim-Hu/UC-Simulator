import streamlit as st
import pandas as pd
import numpy as np
from streamlit_extras.switch_page_button import switch_page

# Set page configuration
st.set_page_config(page_title="UC Simulator", page_icon="🚀", layout="wide",initial_sidebar_state='collapsed')


import streamlit as st


# About You
st.header("About You",divider='rainbow')

# First and Last Name in a two-column layout
col1, col2, col3 = st.columns(3)
with col1:
    first_name = st.text_input("First Name", "", help="Enter your first name")
with col2:
    last_name = st.text_input("Last Name", "", help="Enter your last name")


# ========================================
# Load the data only once using st.cache
@st.cache_data
def load_data():
    data = pd.read_csv('Data/DIM_School_UCSD_APP.csv')
    return data

DIM_School_UCSD_APP = load_data()

# High School Type Radio Buttons
school_type = st.radio("High School Type",
                       options=["High School in California", "High School out of California", "International High School"],
                       index=1)  # Default to second option

# ... previous code ...

# Initialize selected_school_code as None before the if block
selected_school_code = None

# If High School in California is selected, show the search section
if school_type == "High School in California":
    # Search box for the user to type the school name
    user_input = st.text_input("School Name")

    # Filter the DataFrame based on user input
    filtered_df = DIM_School_UCSD_APP[DIM_School_UCSD_APP['School'].str.contains(user_input, case=False, na=False)]

    # Function to format school information
    def format_school_info(school_row):
        return f"{school_row['School']}, {school_row['City']}, {school_row['County/State/Country']}"

    # Initialize school_info_list as an empty list before the if block
    school_info_list = []
    
    # Create a selectbox with the filtered options
    if not filtered_df.empty and user_input:  # Check if there is user input
        # Using a tuple (school_info, school_code) as selectbox option
        selectbox_options = [
            (format_school_info(row), row['School Code']) for _, row in filtered_df.iterrows()
        ]

        # Create a list of formatted school information for display in the selectbox
        school_info_list = [info for info, _ in selectbox_options]

        # User selects based on school information
        selected_school_info = st.selectbox(
            "Select a school",
            options=school_info_list
        )

        # Find the corresponding school code for the selected school information
        # Provide a default value to next() to avoid StopIteration
        selected_school_code = next((code for info, code in selectbox_options if info == selected_school_info), None)

    # Now, you can check if selected_school_code is not None and proceed
    if selected_school_code is not None:
        # Display the selected school information
        st.write("School Information:")
        st.write(selected_school_info)

        # Store the school code in session state for other pages to use
        st.session_state['selected_school_code'] = selected_school_code
    elif user_input:  # User has typed something but no school was selected or list is empty
        st.write("No matching school found or no school selected.")
        st.session_state['selected_school_code'] = None



# =========================
st.divider()
# Campuses & Majors
st.markdown("#### Campuses & Majors 🏛️")

# Intended UC Campus for Admission Simulation
st.multiselect("Intended UC Campus for Admission Simulation",
               options=["UC Berkeley", "UC Davis", "UC Irvine", "UCLA", "UC Merced",
                        "UC Riverside", "UC San Diego", "UC Santa Barbara", "UC Santa Cruz"])

# Intended Major
st.text_input("Intended major", "", help="i.e. Chemistry or Undeclared")

# Academic
st.markdown("#### GPA 💯")

# Weighted GPA in 10th and 11th Grade (Sophomore & Junior)
col1, col2, col3 = st.columns([3, 1, 1])  # Adjust the middle column width as needed
with col1:  # This places the slider in the middle column, effectively controlling its width
    GPA = st.slider("Weighted GPA in 10th and 11th Grade (Sophomore & Junior)",
              min_value=2.6, max_value=5.0, value=5.0, step=0.01)

st.divider()

## Start button
col1, col2,col3 = st.columns([2,1,2])
with col2:
    if st.button('Save and Continue', type='primary'):
        switch_page("What is JPA?")

