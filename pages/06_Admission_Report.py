import streamlit as st
from fpdf import FPDF

# Function to generate PDF
def create_pdf():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Your Admission Letter", ln=True, align='C')
    # Add more content to your PDF here
    # ...
    pdf.output("/mnt/data/admission_letter.pdf")

# Start of Streamlit page
st.write("# University of California San Diego")
st.write("## Admission Decision for Fall 2024")

st.write("Dear xxx,")
st.write("""
Congratulations! We’re pleased to inform you that you are likely to be admitted to University of California San Diego for Fall 2024.
Your selection for the Class of 2027 is an extraordinary accomplishment, given that UC San Diego received more than 150,000 applications! We believe you have the talent, skills, knowledge, and passion to be a powerful contributing member of the UC San Diego. Please accept my personal congratulations on your outstanding achievement.
""")
st.write("## Decision Process")
st.write("Below are the reasons we believe you are a promising candidate for admission:")

col1, col2 = st.columns([1,3])
with col1:
    st.metric("GPA", "3.85")
with col2:
    st.markdown("""
    You have a weighted GPA of 3.85 in your sophomore and junior years, which is higher than 79,831 applicants in UC Simulator, and at the 17th percentile.
    """)

col1, col2 = st.columns([1,3])
with col1:
    st.metric("Avg 10th/11th Courses", 12)
with col2:
    st.markdown("""
    You have taken an average of 12 semester courses in your sophomore and junior years, which is 2 courses more than the other applicants and demonstrates your higher difficulties and effort in schoolwork, which increase your competency and add points to your JPA and J-Score.
    """)

col1, col2 = st.columns([1,3])
with col1:
    st.metric("AP", "3.5", "2 exams taken")
with col2:
    st.markdown("""
    You have taken 2 AP exams with an average score of 3.5, which increases your competency and adds points to your JPA and J-score.
    """)

col1, col2 = st.columns([1,3])
with col1:
    st.metric("Extracurricular Activity", "Debate team", "& 2 more")
with col2:
    st.markdown("""
    You have participated in 3 extracurricular activities, where 2 of them are higher than average achievement compared to other applicants, which increases your chance of admission.
    """)

st.write("Now, please download this report and bring it to your counselor, family, or friends, and continue to prepare and refine your application with our full-capability simulation.")

if st.button('Download as PDF'):
    create_pdf()
    st.write('Download your Admission Letter [here](/mnt/data/admission_letter.pdf)')

if st.button('Import to full-capability UC simulator'):
    st.write('Feature to import to the UC simulator is not yet implemented.')

st.write("## Additional Information")
col1, col2, col3 = st.columns(3)
with col1:
    st.subheader("Ranking among 150,000 applicants")
    st.markdown("""
    Real-time ranking and admission chance among other UC Candidates.
    """)
with col2:
    st.subheader("Score your PIQ and Activity Writing")
    st.markdown("""
    Instant writing ranking and professional’s feedback for refinement.
    """)
with col3:
    st.subheader("One click export to UC System")
    st.markdown("""
    Prepare and store your best version. When the application opens, export to UC application system with one click.
    """)


st.write(st.session_state.user_data.to_dict())