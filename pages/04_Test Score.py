
import streamlit as st
from streamlit_extras.switch_page_button import switch_page
# Set page configuration
st.set_page_config(page_title="UC Simulator", page_icon="🚀", layout="centered",initial_sidebar_state='expanded')

# Function to remove an AP based on its index
def remove_AP(index):
    st.session_state.AP_Exam_List.pop(index)

# Initialize the session state for the list of AP exams if not already present
if 'AP_Exam_List' not in st.session_state:
    st.session_state.AP_Exam_List = []
#==========================================
# Header for the Streamlit app
st.header("AP Test Score",divider='rainbow')
st.markdown("""
    🚨 As UC schools are no longer considering SAT or ACT scores, your AP Test scores have become a **crucial** component 
    to demonstrate your academic competency.

    ✏️ Please enter your AP Test Scores below to enable the model to calculate your ranking among other students.
""")

# List of AP Tests
AP_Test_list = [
    '2-D Art and Design (formerly Studio Art 2D Design)',
    '3-D Art and Design (formerly Studio Art 3D Design)',
    'African American Studies',
    'Art History',
    'Biology',
    'Calculus AB',
    'Calculus AB Subscore (from the BC sitting)',
    'Calculus BC',
    'Chemistry',
    'Chinese Language and Culture',
    'Comparative Government and Politics',
    'Computer Science A',
    'Computer Science Principles',
    'Drawing (formerly Studio Art - Drawing)',
    'Economics: Macroeconomics',
    'Economics: Microeconomics',
    'English Language and Composition',
    'English Literature and Composition',
    'Environmental Science',
    'European History',
    'French Language/Language and Culture',
    'German Language/Language and Culture',
    'Human Geography',
    'Italian Language and Culture',
    'Japanese Language and Culture',
    'Latin (formerly Latin:Vergil)',
    'Music Theory',
    'Physics B (discontinued 2014)',
    'Physics C: Electricity and Magnetism',
    'Physics C: Mechanics',
    'Physics 1',
    'Physics 2',
    'Precalculus',
    'Psychology',
    'Research',
    'Seminar',
    'Spanish Language/Language and Culture',
    'Spanish Literature/Literature and Culture',
    'Statistics',
    'U.S. Government and Politics',
    'U.S. History',
    'World History: Modern (formerly World History)'
]


# Form for input
with st.form("my_form", clear_on_submit=True):
    st.markdown('Add AP Test Score')
    AP_Exam = st.selectbox("AP Exam", AP_Test_list, index=5)
    AP_Test_Score =  st.number_input("Test Score", min_value=1, max_value=5, value=4)
    # AP_Test_Score = st.slider("Test Score", min_value=1, max_value=5, value=5, step=1)
    submitted = st.form_submit_button("Add Test Score",type='primary')

# Add an AP test score to the list
if submitted:
    st.session_state.AP_Exam_List.append((AP_Exam, AP_Test_Score))
    st.subheader("Your AP Exams")

# Display the list of AP Exams and scores



for i, (AP_Exam, AP_Test_Score) in enumerate(st.session_state.AP_Exam_List):
    cols = st.columns([3, 1, 1,1])
    cols[0].markdown(AP_Exam)
    cols[1].markdown(f"Score: {AP_Test_Score}")
    # Add a 'Remove' button for each AP Exam
    if cols[2].button("Remove", key=f"remove_{i}"):
        remove_AP(i)
        # Rerun the app to update the display
        st.experimental_rerun()


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
st.divider()
st.markdown("👇When you complete, let's generate your preliminary ranking...")

if st.session_state.AP_Exam_List:
    # If AP scores have been added, show the button to generate the ranking report
    if st.button('Generate My Ranking Report',type='primary'):
        switch_page('AP Scores')
else:
    # If no AP scores have been added (or if 'No' was selected for AP exams taken),
    # you can still show the button or perhaps disable it or change its message
    if st.button('Proceed without AP Scores'):
        switch_page('AP Scores')