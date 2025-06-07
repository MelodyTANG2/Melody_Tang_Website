import streamlit as st
from components.interactive import display_interactive_chart

def experience_page():
    st.markdown("<h2 style='text-align: center; color: #2E4057;'>🌟 Internship Experience 🌟</h2>", unsafe_allow_html=True)
    
    # 添加Colgate-Palmolive公司经历
    st.markdown("""
    <div style='background-color: #f8f9fa; padding: 20px; border-radius: 10px; margin: 10px 0;'>
        <img src='https://logos-world.net/wp-content/uploads/2020/09/Colgate-Logo.png' style='width: 150px; margin-bottom: 10px;'>
        <h3 style='color: #E3170A;'>Analytics & Insights Intern</h3>
        <p style='color: #666; font-style: italic;'>📍 <strong>Colgate Palmolive</strong> | February 2025 - June 2025 | <strong>Hong Kong</strong></p>
        <ul style='list-style-type: none;'>
            <li>📊 Extracted key information from data consulting company reports and developed <strong>"Analytics Guide"</strong> for the APAC team</li>
            <li>🔍 Actively involved in conducting quantitative and qualitative <strong>competitor analysis</strong> for more than 10 subbrands across the entire APAC</li>
            <li>💰 Conducted Colgate's promotion and <strong>pricing analysis</strong> for countries and regions in APAC</li>
            <li>🔄 Responsible for <strong>pre-processing</strong> tens of thousands of <strong>APAC POS data</strong>, providing critical support to the Customer Development team</li>
            <li>👥 <strong>Collaborated with agency</strong> to develop <strong>Python scripts</strong> to process Colgate's <strong>yearly promotional data</strong></li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # 添加FrieslandCampina公司经历
    st.markdown("""
    <div style='background-color: #f8f9fa; padding: 20px; border-radius: 10px; margin: 10px 0;'>
        <img src='https://logo.clearbit.com/frieslandcampina.com' style='width: 100px; margin-bottom: 10px;'>
        <h3 style='color: #F7B500;'>Marketing Intern</h3>
        <p style='color: #666; font-style: italic;'>📍 <strong>FrieslandCampina</strong> | May 2024 - August 2024</p>
        <ul style='list-style-type: none;'>
            <li>📈 Independently completed the product database of three major ecommerce platforms, did <strong>data analysis</strong> and came up with some findings which satisfied and inspired the marketing manager</li>
            <li>🎥 Assisted in writing FBIF (Food & Beverage Innovation Forum) speaker preview <strong>video copy, video filming, editing</strong> as well as creating the Forum presentation PowerPoint</li>
            <li>🎯 Participated in the entire FBIF exhibition from preparation to review, assisted the global marketing lead from headquarter with the market research, independently completed the <strong>competitor spotting</strong>, and assisted the manager in completing the <strong>trends spotting</strong></li>
            <li>🤝 <strong>Liaised with agencies</strong> to finalize <strong>promotional materials on social media platforms</strong> and <strong>FBIF exhibition venue details</strong></li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # 添加Avient Corporation公司经历
    st.markdown("""
    <div style='background-color: #f8f9fa; padding: 20px; border-radius: 10px; margin: 10px 0;'>
        <img src='https://logo.clearbit.com/avient.com' style='width: 100px; margin-bottom: 10px;'>
        <h3 style='color: #0066CC;'>Marketing Intern</h3>
        <p style='color: #666; font-style: italic;'>📍 <strong>Avient Corporation</strong> | July 2022 - September 2022</p>
        <ul style='list-style-type: none;'>
            <li>📱 Organized product selection guide of SEM BU in Asia and responsible for the update of the company's <strong>Wechat official account</strong></li>
            <li>🎨 Communicated with <strong>advertising agency</strong> to finalize the promotional materials, and followed up on the progress</li>
            <li>❤️ Collected and organized the company's charitable activities' documents in Asian countries, and <strong>contacted</strong> more than 10 local leaders to follow up the progress</li>
            <li>📝 Completed more than 20 English <strong>translations</strong> and proofreadings of the company's exhibition materials, such as product brochures</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("---")
    
    st.markdown("## 🎯 Professional Skills")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 💼 Technical Skills
        - 📊 **Business Analysis**
        - 📈 **Market Analysis** 
        - 🎯 **Marketing Communication** 
        - 📱 **Social Media Marketing** 
        - 📢 **Marketing Campaign Management**
        """)
        
    with col2:
        st.markdown("""
        ### 🌟 Soft Skills
        - 💬 **Communication** 
        - 👥 **Teamwork** 
        - ⏰ **Time Management** 
        - 👑 **Leadership** 
        - 🔄 **Adaptability** 
        """)
