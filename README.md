1.Install Dependencies:-
pip install -r requirements.txt

2.Set up API Key:-
-Google MakerSuite.

3.Run the Application:-
streamlit run app.py
The app will open automatically in your browser at: http://localhost:8501

4.How It Works:-
-Upload your Resume (PDF)
-Paste the Job Description (JD)
-Click Submit
-The app will extract text from your resume, sends a prompt to the Gemini 1.5 Pro model
-Displays: JD Match Percentage, Missing Keywords, Profile Summary

5.Tech Stack:-
-Python 3.10+
-Streamlit
-Google Generative AI (Gemini 1.5 Pro)
-PyPDF2
-python-dotenv
