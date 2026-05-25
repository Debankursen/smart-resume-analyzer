<img width="1026" height="175" alt="image" src="https://github.com/user-attachments/assets/bb4fff74-007b-4b63-9ff7-ef9c5d030bdf" /># smart-resume-analyzer
Smart Resume Analyzer is an AI-powered web application built using Python and Streamlit that analyzes resumes against job descriptions. It calculates ATS score, identifies matching and missing skills, provides domain-based skill recommendations, and ranks resumes with grades and stars. Designed to help job seekers improve resume quality .

# Problem Statement
Recruiters receive thousands of resumes for job openings, making manual screening time-consuming and inefficient. Many qualified candidates get rejected due to low ATS compatibility. There is a need for an automated system that evaluates resumes, detects skill gaps, and ranks candidates accurately .

# Proposed Solution
The proposed system aims to address the challenge of manual resume screening by automating the analysis process using Artificial Intelligence.  It predicts resume suitability  for a         job role by comparing resumes with job descriptions and identifying skill gaps. The solution consists of the following components:
Data Collection:
Gather resume data in PDF/DOCX format uploaded by users.Collect job description text provided by recruiters or job portals.Maintain a predefined skill keywords database for analysis.
Data Preprocessing:
Extract text from resumes using PDF/DOCX parsers.Clean and preprocess text by converting to lowercase and removing noise.Perform keyword matching to standardize skill identification.
Machine Learning Algorithm:
Implement Cosine Similarity algorithm to compare resume text with job description.Use CountVectorizer to convert textual data into numerical vectors.Calculate ATS score based on similarity percentage.
Deployment:
Develop a user-friendly web application using Streamlit.Provide real-time resume analysis, ATS score, ranking, and recommendations.Deploy the system on Streamlit Cloud for online accessibility.
Evaluation:
Evaluate system performance based on ATS score accuracy and skill detection.Validate recommendations by comparing missing skills with job requirements.Continuously improve skill database and matching logic.
Result: The system successfully analyzes resumes, detects skills, identifies missing competencies, calculates ATS score, ranks resumes, and provides skill improvement        recommendations through an interactive web interface.

