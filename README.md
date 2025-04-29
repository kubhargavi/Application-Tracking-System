
# Application Tracking System 

---

## 1. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 2. Set up API Key
- Google MakerSuite.

---

## 3. Run the Application
```bash
streamlit run app.py
```
The app will open automatically in your browser at:
```
http://localhost:8501
```

---

## 4. How It Works
- Upload your Resume (PDF)
- Paste the Job Description (JD)
- Click **Submit**
- The app will:
  - Extract text from your resume
  - Send a prompt to the Gemini 1.5 Pro model
  - Display:
    - JD Match Percentage
    - Missing Keywords
    - Profile Summary

---

## 5. Tech Stack
- Python 3.10+
- Streamlit
- Google Generative AI (Gemini 1.5 Pro)
- PyPDF2
- python-dotenv

