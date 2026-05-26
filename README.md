# Smart-Resume-Analyzer
Smart Resume Analyzer is an AI-powered web application built using Python and Streamlit that analyzes resumes against job descriptions. It calculates ATS score, identifies matching and missing skills, provides domain-based skill recommendations, and ranks resumes with grades and stars. Designed to help job seekers improve resume quality .

<img width="1855" height="826" alt="Screenshot 2026-05-25 220858" src="https://github.com/user-attachments/assets/5fe374c8-71e9-4097-8458-6fc5bdc2c3df" />


# Problem Statement
Recruiters receive thousands of resumes for job openings, making manual screening time-consuming and inefficient. Many qualified candidates get rejected due to low ATS compatibility. There is a need for an automated system that evaluates resumes, detects skill gaps, and ranks candidates accurately .

# Proposed Solution
The proposed system aims to address the challenge of manual resume screening by automating the analysis process using Artificial Intelligence.  It predicts resume suitability  for a  job role by comparing resumes with job descriptions and identifying skill gaps. The solution consists of the following components:                                                                                                                                                                                    
* Data Collection:                                                                                                                                                 
  Gather resume data in PDF/DOCX format uploaded by users.                                                                                               
  Collect job description text provided by recruiters or job portals.                                                                                              
  Maintain a predefined skill keywords database for analysis.                                                                                                                                                                                                                     
* Data Preprocessing:
  Extract text from resumes using PDF/DOCX parsers. Clean and preprocess text by converting to lowercase and removing noise. Perform keyword matching to             standardize skill identification.
* Machine Learning Algorithm:
  Implement Cosine Similarity algorithm to compare resume text with job description.  Use CountVectorizer to convert textual data into numerical vectors.            Calculate ATS score based on similarity percentage.
* Deployment:
 Develop a user-friendly web application using Streamlit.Provide real-time resume analysis, ATS score, ranking, and recommendations.Deploy the system on Streamlit  Cloud for online accessibility.
* Evaluation:
  Evaluate system performance based on ATS score accuracy and skill detection. Validate recommendations by comparing missing skills with job requirements.           Continuously improve skill database and matching logic.
* Result:
 The system successfully analyzes resumes, detects skills, identifies missing competencies, calculates ATS score, ranks resumes, and provides skill improvement     recommendations through an interactive web interface.
# System  Approach:
* Python: Used as the core programming language to build the resume analysis logic and backend processing.
* Natural Language Processing (NLP):Used to process and analyze resume text to identify relevant skills and keywords.
* Machine Learning: Applied cosine similarity algorithm to calculate ATS score by matching resume with job description.
* Streamlit Web Framework: Used to create an interactive and user-friendly web application interface.
* Plotly Visualization: Used to display ATS score using a dynamic and visual gauge meter chart.
* GitHub Deployment: Used to host and manage the project source code repository.
* Streamlit Cloud Hosting: Used to deploy and run the application online for public access.

# ALGORITHM & DEPLOYMENT: 
* Algorithm Selection
• Cosine Similarity is used to calculate ATS score by comparing resume text with job description.
* Data Input
• Resume text • Job description
• Skill keywords database
* Training / Processing
• Text vectorization using CountVectorizer • Similarity calculation
* Deployment
• Deployed using Streamlit Cloud integrated with GitHub repository

# CONCLUSION:
The Smart Resume Analyzer automates resume screening, improves ATS 
compatibility, and helps candidates enhance their resumes. It reduces recruiter 
workload and increases hiring efficiency using AI-based analysis.

# FUTURE SCOPE:
• Multi-resume ranking system

• Interview question prediction

• Resume improvement tips

• LinkedIn profile analysis

• AI resume rewriting

• Integration with job portals

# REFERENCES:
1. Streamlit Documentation

2. Scikit-learn Machine Learning Library

3. PyPDF2 Python Library

4. Plotly Visualization Library

5. Kaggle Job Description Dataset

GitHub Link: https://github.com/Debankursen/smart-resume-analyzer

Dataset Link : https://www.kaggle.com/datasets/ravindrasinghrana/job￾description-dataset
