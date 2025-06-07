import streamlit as st
from pathlib import Path

def education_page():
    st.markdown("""
        <style>
        .education-container {
            background-color: #ffffff;
            padding: 25px;
            border-radius: 12px;
            margin: 15px 0;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            display: flex;
            align-items: flex-start;
        }
        .education-content {
            flex: 1;
            padding-right: 20px;
        }
        .school-logo {
            width: 150px;
            height: auto;
            object-fit: contain;
        }
        .degree-title {
            color: #1a73e8;
            font-size: 1.4em;
            font-weight: 600;
            margin-bottom: 8px;
        }
        .school-name {
            color: #202124;
            font-size: 1.2em;
            font-weight: 500;
        }
        .date {
            color: #5f6368;
            font-style: italic;
            margin: 5px 0;
        }
        .courses-container {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin-top: 10px;
        }
        .course-item {
            background-color: #f1f3f4;
            padding: 5px 12px;
            border-radius: 15px;
            font-size: 0.9em;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<h2 style='text-align: center;'>🎓 Education</h2>", unsafe_allow_html=True)

    # CUHK
    st.markdown("""
        <div class="education-container">
            <div class="education-content">
                <div class="degree-title">Master of Science in Marketing</div>
                <div class="school-name">The Chinese University of Hong Kong</div>
                <div class="date">September 2024 - July 2025</div>
                <div>📊 <strong>Big Data Marketing concentration</strong></div>
                <div style="margin-top: 10px">📚 Relevant Coursework: 
                    <span class="courses-container">
                        <span class="course-item">💻 Digital Marketing</span>
                        <span class="course-item">📱 Social Media Analytics</span>
                        <span class="course-item">👥 Customer Analytics</span>
                        <span class="course-item">💰 Pricing Analytics</span>
                        <span class="course-item">🤖 Machine Learning</span>
                        <span class="course-item">📈 Big Data Strategy</span>
                    </span>
                </div>
            </div>
            <img src="https://www.cuhk.edu.hk/english/images/cuhk_logo_2x.png" class="school-logo">
        </div>
    """, unsafe_allow_html=True)
    st.markdown("""
        <div class="education-container">
            <div class="education-content">
                <div class="degree-title">Bachelor of Arts in German</div>
                <div class="school-name">Shanghai International Studies University</div>
                <div class="date">September 2020 - July 2024</div>
                <div>🌐 <strong>Minor: International Economics and Trade</strong></div>
                <div>🗣️ Focus on German language and culture</div>
                <div>📊 Combined with business and economic studies</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="education-container">
            <div class="education-content">
                <div class="degree-title">Bachelor of Science in Business Administration - Dual Degree</div>
                <div class="school-name">University of Bayreuth</div>
                <div class="date">September 2021 - July 2024</div>
                <div>🤝 Joint program with Shanghai International Studies University</div>
                <div>🇩🇪 Study period in Germany: July 2023 - March 2024</div>
                <div>💼 Focus on international business management</div>
            </div>
        </div>
    """, unsafe_allow_html=True)
