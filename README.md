<img width="967" height="107" alt="image" src="https://github.com/user-attachments/assets/cb193b1d-8a0f-4529-a3a6-c17b208b2635" /><img width="392" height="53" alt="image" src="https://github.com/user-attachments/assets/e979d5dc-fd8e-4e8a-a126-548b9275721d" /><img width="297" height="53" alt="image" src="https://github.com/user-attachments/assets/de6a25d0-d73c-46d3-8b1a-fa0638687b7e" /><img width="297" height="53" alt="image" src="https://github.com/user-attachments/assets/94658b63-0aa1-4a70-978f-b6daf124480b" /># smart-resume-analyzer
Smart Resume Analyzer is an AI-powered web application built using Python and Streamlit that analyzes resumes against job descriptions. It calculates ATS score, identifies matching and missing skills, provides domain-based skill recommendations, and ranks resumes with grades and stars. Designed to help job seekers improve resume quality .

<img width="1855" height="826" alt="Screenshot 2026-05-25 220858" src="https://github.com/user-attachments/assets/5fe374c8-71e9-4097-8458-6fc5bdc2c3df" />


# Problem Statement
Recruiters receive thousands of resumes for job openings, making manual screening time-consuming and inefficient. Many qualified candidates get rejected due to low ATS compatibility. There is a need for an automated system that evaluates resumes, detects skill gaps, and ranks candidates accurately .

# Proposed Solution
The proposed system aims to address the challenge of manual resume screening by automating the analysis process using Artificial Intelligence.  It predicts resume suitability  for a  job role by comparing resumes with job descriptions and identifying skill gaps. The solution consists of the following components:                                                                                                                                                                                    
* Data Collection:                                                                                                                                                 
* Gather resume data in PDF/DOCX format uploaded by users.                                                                                               
* Collect job description text provided by recruiters or job portals.                                                                                              
* Maintain a predefined skill keywords database for analysis.                                                                                                                                                                                                                     
* Data Preprocessing:
* Extract text from resumes using PDF/DOCX parsers.
* Clean and preprocess text by converting to lowercase and removing noise.
* Perform keyword matching to standardize skill identification.                                                                                                          
* Machine Learning Algorithm:
* Implement Cosine Similarity algorithm to compare resume text with job description.  Use CountVectorizer to convert textual data into numerical vectors. Calculate ATS score based on similarity percentage.

