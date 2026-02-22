# ================= IMPORT LIBRARIES =================
import streamlit as st
import PyPDF2
import docx2txt
import plotly.graph_objects as go
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Smart Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

# ================= HEADER =================

st.markdown("""
<div style="
    background:#87CEEB;
    padding:20px;
    border-radius:12px;
    text-align:center;
    color:black;
    margin-bottom:25px;
    box-shadow:2px 2px 10px rgba(0,0,0,0.2);
">
    <h1>📄 Smart Resume Analyzer</h1>
    <p>AI-Powered ATS & Skill Analysis System</p>
</div>
""", unsafe_allow_html=True)


# ================= TEXT EXTRACTION =================
def extract_text(file):

    if file.name.endswith(".pdf"):
        pdf = PyPDF2.PdfReader(file)
        text = ""

        for page in pdf.pages:
            if page.extract_text():
                text += page.extract_text()

        return text

    elif file.name.endswith(".docx"):
        return docx2txt.process(file)


# ================= SKILL DATABASE =================
skills_db = [
    "python","java","sql","machine learning",
    "data analysis","deep learning","aws",
    "cloud","git","nlp","html","css",
    "javascript","android","flutter",
    "kotlin","firebase","react"
]


# ================= SKILL EXTRACTION =================
def extract_skills(text):
    text = text.lower()
    return [skill for skill in skills_db if skill in text]


# ================= ATS SCORE =================
def ats_score(resume, jd):

    cv = CountVectorizer()
    matrix = cv.fit_transform([resume, jd])
    score = cosine_similarity(matrix)[0][1]

    return round(score * 100, 2)


# ================= RESUME RANKING =================
def resume_ranking(score):

    if score >= 85:
        return "⭐⭐⭐⭐⭐", "A+", "Excellent Resume"

    elif score >= 70:
        return "⭐⭐⭐⭐", "A", "Very Good Resume"

    elif score >= 55:
        return "⭐⭐⭐", "B", "Good Resume"

    elif score >= 40:
        return "⭐⭐", "C", "Average Resume"

    else:
        return "⭐", "D", "Needs Improvement"


# ================= GAUGE =================
def show_gauge(score):

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=score,
        title={"text": "ATS Score"},
        gauge={
            "axis": {"range": [0, 100]},
            "bar": {"color": "#28a745"},
            "steps": [
                {"range": [0, 50], "color": "#ff4d4d"},
                {"range": [50, 75], "color": "#ffa500"},
                {"range": [75, 100], "color": "#90ee90"},
            ],
        }
    ))

    st.plotly_chart(fig, use_container_width=True)


# ================= TAG STYLE =================
def show_skill_tags(title, skills, color):

    st.subheader(title)

    if not skills:
        st.info("No skills found")
        return

    tags = ""

    for skill in skills:
        tags += f"""
        <span style="
            background:{color};
            padding:10px 22px;
            border-radius:30px;
            margin:10px;
            display:inline-block;
            color:white;
            font-weight:bold;
            font-size:18px;
            box-shadow:2px 2px 8px rgba(0,0,0,0.3);
        ">
        ✍️ {skill}
        </span>
        """

    st.markdown(tags, unsafe_allow_html=True)


# ================= DOMAIN + RECOMMEND =================
domain_skills = {
    "data science": ["Python","Pandas","NumPy","TensorFlow"],
    "android": ["Kotlin","Flutter","Firebase"],
    "web": ["React","Node.js","MongoDB"]
}


def detect_domain(skills):

    if "machine learning" in skills:
        return "Data Science"

    elif "android" in skills:
        return "Android Development"

    elif "html" in skills:
        return "Web Development"

    return "General"


def recommend_skills(domain, user_skills):

    for key, value in domain_skills.items():
        if key in domain.lower():
            return list(set(value) - set(user_skills))

    return []


# ================= UI =================
resume_file = st.file_uploader(
    "Upload Resume (PDF / DOCX)",
    type=["pdf","docx"]
)

job_desc = st.text_area(
    "Paste Job Description",
    height=180
)


# ================= PROCESS =================
if resume_file and job_desc:

    resume_text = extract_text(resume_file)

    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(job_desc)

    missing_skills = list(set(jd_skills) - set(resume_skills))
    score = ats_score(resume_text, job_desc)

    # -------- SKILLS --------
    show_skill_tags(
        "✅ Resume Skills",
        resume_skills,
        "#28a745"
    )

    show_skill_tags(
        "❌ Missing Skills",
        missing_skills,
        "#ff5733"
    )

    # -------- ATS --------
    st.subheader("📊 ATS Score")
    show_gauge(score)
    st.success(f"{score}% Resume Match")

    # -------- RANKING --------
    stars, grade, status = resume_ranking(score)

    st.subheader("🏆 Resume Ranking")

    st.markdown(
        f"""
        <div style="
            background:#e9ecef;
            padding:30px;
            border-radius:15px;
            text-align:center;
            font-size:22px;
            box-shadow:2px 2px 8px rgba(0,0,0,0.2);
            margin-bottom:20px;
        ">
            <p><b>Rank:</b> {stars}</p>
            <p><b>Grade:</b> {grade}</p>
            <p><b>Status:</b> {status}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # -------- RECOMMENDATION --------
    st.subheader("💡 Skills Recommendation")

    domain = detect_domain(resume_skills)

    st.info(
        f"Our analysis says you are looking for **{domain} Jobs**"
    )

    recommended = recommend_skills(
        domain,
        resume_skills
    )

    show_skill_tags(
        "Recommended Skills For You",
        recommended,
        "#ff7043"
    )

# ================= FOOTER =================
st.markdown("""
<style>
.footer {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    background: #87CEEB;
    text-align: center;
    padding: 12px;
    font-size: 14px;
    color: black;
    border-radius: 10px 10px 0px 0px;
}
</style>

<div class="footer">
    © 2026 Smart Resume Analyzer | Developed by Debankur Sen 🚀
</div>
""", unsafe_allow_html=True)