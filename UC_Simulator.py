import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Set page configuration
st.set_page_config(page_title="UC Simulator", page_icon="🚀", layout="centered",initial_sidebar_state='collapsed')

# Main page content
st.title("UC Application Simulator 🚀")
st.caption("Discover your admission chances across the University of California's 8 campuses. Compare your application with over 15,000 applicants from the class of 2025.")

st.header("",divider='rainbow')

# Use columns for layout - First set for descriptive text
text_col1, text_col2, text_col3 = st.columns(3)

with text_col1:
    st.markdown("#### 🥇 Rank against 15,000+ UC applicants.")
    st.metric("UC Applicants", "Top 8%", "1,300/68,893 Applicants")
    
with text_col2:
    st.markdown("#### 🥈 Compare with fellow schoolmates.")
    st.metric("Palo Alto High School", "Top 5%", "2/42 Applicants")
    
with text_col3:
    st.markdown("#### 🥉 Instant feedback by AI counselor.")
    st.metric("UC Berkeley%", "76%", "1,168/8,984 Applicants")


st.divider(

)
# Real-time chances updates
st.markdown("### Real-time Admission Chances")
st.caption("###### Watch your admission probabilities evolve as you and other applicants update your applications.")
## Start button
if st.button('🚀 Get Started', type='primary'):
    switch_page("About_You")

# ==========
# Define the weights for each element of the UC application process
weights = {
    "Weighted GPA": 60,
    "AP": 60,
    "Honor": 58,
    "IB": 60,
    "Course Selection": 58,
    "Extracurricular Activities": 56,
    "PIQ": 54,
    "Research": 52,
    "Work Experience": 50,
    "Volunteer": 48,
    # Added elements based on importance for UC applications
    "Leadership": 46,
    "Community Service": 44
}

# Generate the word cloud with a transparent background
wordcloud = WordCloud(width=800, height=300, background_color=None, mode="RGBA").generate_from_frequencies(weights)

# Display the generated image with adjusted figure size and dark background
fig, ax = plt.subplots(figsize=(10, 4))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")

# Set the figure background color
fig.patch.set_facecolor('#0E1117')  # Adjust this color to match Streamlit's dark mode background or your preference
ax.set_facecolor('#0E1117')  # Ensure the axes background is also set if needed

wccol1, wccol2, wccol3 = st.columns([2,1,1])
with wccol1:
# Use st.pyplot() to display the matplotlib plot in Streamlit with the adjusted background
    st.pyplot(fig)
