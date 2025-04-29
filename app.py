import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
import json

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get Gemini model response
def get_gemini_response(input_text):
    model = genai.GenerativeModel('models/gemini-1.5-pro')
    response = model.generate_content(input_text)
    return response.text

# Function to read uploaded PDF file
def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += str(page.extract_text())
    return text

# Prompt Template
input_prompt_template = """
Hey Act Like a skilled or very experienced ATS (Application Tracking System)
with a deep understanding of tech fields: software engineering, data science, data analysis, full stack engineering, backend engineering, frontend engineering,
DevOps engineering, machine learning engineering, and big data engineering. Your task is to evaluate the resume based on the given job description.

You must consider that the job market is very competitive and you should provide the best assistance for improving the resumes. Assign a percentage match
based on the JD and list the missing keywords with high accuracy.

Resume: {resume_text}
Job Description: {job_description}

I want the response in one single string having the structure:
{{"JD Match":"%","MissingKeywords":[],"Profile Summary":""}}
"""

# Streamlit App
st.title("📝 Smart ATS - Resume Evaluator")
st.text("Improve your resume with ATS insights!")

# Input fields
job_description = st.text_area("Paste the Job Description here:")
uploaded_file = st.file_uploader("Upload Your Resume (PDF format only)", type="pdf", help="Please upload a PDF file.")

submit = st.button("Submit")

if submit:
    if uploaded_file is not None and job_description.strip() != "":
        resume_text = input_pdf_text(uploaded_file)
        
        # Fill the input prompt
        input_prompt = input_prompt_template.format(resume_text=resume_text, job_description=job_description)
        
        # Get response from Gemini
        try:
            output = get_gemini_response(input_prompt)
            st.subheader("📄 ATS Evaluation Result")
            st.write(output)
        except Exception as e:
            st.error(f"Error generating response: {e}")
    else:
        st.warning("⚠️ Please upload a resume and enter a job description before submitting.")
