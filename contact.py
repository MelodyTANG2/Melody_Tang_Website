import streamlit as st
from streamlit_lottie import st_lottie
import requests
import json
def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def contact_page():
    # 添加创意标题和动画
    st.markdown("<h1 style='text-align: center; color: #FF69B4;'>✨ Let's Connect! ✨</h1>", unsafe_allow_html=True)
    
    # 添加Lottie动画
    lottie_contact = load_lottie_url("https://assets5.lottiefiles.com/packages/lf20_u25cckyh.json")
    st_lottie(lottie_contact, height=200)
    
    # 创建两列布局展示联系方式
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style='padding: 15px; background-color: #FFE4E1; border-radius: 10px;'>
        <h4 style='color: #FF1493;'>📧 Email</h4>
        <p><a href='mailto:melodytang1203@gmail.com'>melodytang1203@gmail.com</a></p>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
        <div style='padding: 15px; background-color: #E6E6FA; border-radius: 10px;'>
        <h4 style='color: #4169E1;'>💼 LinkedIn</h4>
        <p><a href='https://www.linkedin.com/in/yajing-melody-tang' target='_blank'>Connect with me</a></p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style='padding: 15px; background-color: #F0FFF0; border-radius: 10px; margin: 20px 0;'>
    <h4 style='color: #2E8B57;'>📱 Phone/WhatsApp</h4>
    <p>+852 59581326</p>
    </div>
    """, unsafe_allow_html=True)
    
    # 创意联系表单
    st.markdown("<h3 style='text-align: center; color: #9370DB;'>💌 Send Me a Message!</h3>", unsafe_allow_html=True)
    
    with st.form("contact_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        
        with col1:
            name = st.text_input("✨ Your Name")
            email = st.text_input("📧 Your Email")
            
        with col2:
            subject = st.text_input("💭 Subject")
            
        message = st.text_area("🎨 Your Message", height=150,
                             placeholder="Share your thoughts, ideas, or just say hi!")
        
        submitted = st.form_submit_button("✉️ Send Message", 
                                        help="Click to send your message!",
                                        type="primary")
        
        if submitted:
            st.balloons()
            st.success("🎉 Thanks for reaching out! I'll get back to you with creative ideas soon! 🌟")
            # In a real application, you would process the form data here
            # For example, send an email or store in a database
