import streamlit as st
from resume_parser import extract_text_from_resume
from evaluator import calculate_similarity

st.set_page_config(page_title="AI Resume Evaluator", layout="centered")

st.title("🧠 AI Resume Evaluator")
st.write("Upload your resume and paste a job description to get feedback!")

resume_file = st.file_uploader("📄 Upload your resume", type=["pdf", "docx"])
job_description = st.text_area("📝 Paste the Job Description")

resume_text = ""
if resume_file:
    resume_text = extract_text_from_resume(resume_file)

if st.button("Evaluate"):
    if resume_text and job_description:
        st.success("✅ Resume processed!")
        similarity = calculate_similarity(resume_text, job_description)

        if isinstance(similarity, str) and similarity.startswith("Error"):
            st.error(similarity)
        else:
            st.subheader(f"🔍 Match Score: {similarity}%")
            if similarity >= 70:
                st.success("✅ Great Match! Your resume aligns well with the job.")
            elif similarity >= 40:
                st.warning("⚠️ Partial Match. Consider improving your resume.")
            else:
                st.error("❌ Low Match. Your resume may not be well suited.")
    else:
        st.warning("Please upload a resume and paste a job description.")

