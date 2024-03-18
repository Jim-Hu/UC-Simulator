import streamlit as st
import pandas as pd
from streamlit_extras.switch_page_button import switch_page

st.cache_data()
# Load the mapping table
mapping_table = pd.read_csv("Data/DIM_Activity_Mapping.csv")

st.markdown("这里有个问题卡壳了，如何让学生在搜不到activity的时候自行customize，checkbox不work")

# Placeholder for the list of activities
if 'activities' not in st.session_state:
    st.session_state.activities = []

# Initialize customize_activity_type checkbox
if 'customize_activity_type' not in st.session_state:
    st.session_state.customize_activity_type = False

# Function to remove an activity based on its index
def remove_activity(index):
    st.session_state.activities.pop(index)
    st.experimental_rerun()

# Function to map activity name to its type
def map_activity(activity_name):
    activity_name = activity_name.strip().lower()  # Convert to lowercase and remove leading/trailing spaces
    if activity_name in mapping_table['Activity Name'].str.strip().str.lower().values:
        activity_type = mapping_table.loc[mapping_table['Activity Name'].str.strip().str.lower() == activity_name, 'Activity Type'].iloc[0]
        return activity_type
    else:
        return None

# Display header
st.header("Extracurricular Activities")

# Form for input
with st.form("my_form"):
    st.markdown('Add Your Extracurricular Activity')
    
    # Checkbox for customizing activity type
    st.session_state.customize_activity_type = st.checkbox("Customize Activity Type", st.session_state.customize_activity_type)
    
    if st.session_state.customize_activity_type:
        # Input for custom activity name
        activity_name = st.text_input("Custom Activity Name")
        
        # Selectbox for activity type
        activity_type = st.selectbox("Activity Type", ["Sports", "Arts", "Academic", "Community Service"])
    else:
        # Selectbox for activity name
        activity_name = st.selectbox("Select your Activity", [""] + mapping_table['Activity Name'].tolist(), placeholder="Select or type in your activity name", help="Select or type in your activity name", key="activity_name_selectbox")
        
        # Check if activity name exists in mapping table
        activity_type = map_activity(activity_name)
        if not activity_type:
            activity_type = ""

    achievement_tier = st.selectbox("Achievement Tier", ["Local", "Regional", "National", "International"])
    submitted = st.form_submit_button("Add Activity")
    
    if submitted and activity_name:
        st.session_state.activities.append((activity_name, activity_type, achievement_tier))

# Display the activities
st.subheader("Your Extracurricular Activities")
for i, (name, act_type, tier) in enumerate(st.session_state.activities):
    cols = st.columns([3, 2, 2, 2])
    cols[0].write(name)
    cols[1].write(act_type)
    cols[2].write(tier)
    # Add a 'Remove' button for each activity
    if cols[3].button("Remove", key=f"remove_{i}"):
        remove_activity(i)

# Button to proceed to the next page
st.markdown("### Ready to Proceed?")
if st.button("Generate Admission Report"):
    st.session_state.user_data['Activity_List'] =  st.session_state.activities
    switch_page("06_Admission_Report")
