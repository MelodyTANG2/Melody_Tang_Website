import streamlit as st
from PIL import Image #PIL for loading images
import os

def home_page():
    # 创建优雅的两栏布局
    left_col, right_col = st.columns([3, 2])
    
    # 添加个人照片，使用圆形裁剪效果
    image_path = os.path.join("static", "images", "image_me.jpg") #这是照片的路径
    if os.path.exists(image_path):
        image = Image.open(image_path)
        # 调整图片大小为固定尺寸
        image = image.resize((300, 300))
        right_col.markdown(
            """
            <style>
            img {
                width: 250px;
                height: 250px;
                border-radius: 50%;
                object-fit: cover;
                box-shadow: 0 8px 16px rgba(0,0,0,0.15);
                display: block;
                margin: auto;
                transition: transform 0.3s ease;
            }
            img:hover {
                transform: scale(1.05);
                box-shadow: 0 12px 24px rgba(0,0,0,0.2);
            }
            </style>
            """,
            unsafe_allow_html=True
        )
        right_col.image(image, output_format='PNG', clamp=True, use_column_width=False, width=250)
    else:
        right_col.warning("Profile image not found")

    # 个人信息部分使用优雅的样式
    left_col.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');
        .name-header {
            font-family: 'Poppins', sans-serif;
            color: #2E4057;
            font-size: 2.5em;
            margin-bottom: 0.5em;
            font-weight: 600;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        .contact-info {
            color: #566573;
            font-size: 1.1em;
            line-height: 1.8;
            padding: 15px;

        }
        .contact-info a {
            color: #3498DB;
            text-decoration: none;
            transition: all 0.3s ease;
        }
        .contact-info a:hover {
            color: #2E4057;
            text-decoration: underline;
        }
        </style>
        <div class="name-header">Yajing (Melody) Tang</div>
        <div class="contact-info">
        ✨ Recent Master's Graduate in Marketing<br>
        🏛️ Chinese University of Hong Kong<br>
        📍 12 Hung Lok Rd., Hung Hom, HKSAR<br>
        📧 <a href="mailto:melodytang1203@gmail.com">melodytang1203@gmail.com</a>
        </div>
        """,
        unsafe_allow_html=True
    )

    # 关于我部分使用简洁现代的样式
    st.markdown(
        """
        <style>
        .about-section {
            background: linear-gradient(135deg, #ffffff, #f8f9fa);
            padding: 2em;
            border-radius: 20px;
            margin: 1.5em 0;
            box-shadow: 0 4px 15px rgba(0,0,0,0.08);
            border: 1px solid rgba(52, 152, 219, 0.1);
            transition: transform 0.3s ease;
        }
        .about-section:hover {
            transform: translateY(-5px);
            box-shadow: 0 6px 20px rgba(0,0,0,0.12);
        }
        .section-title {
            color: #2E4057;
            font-size: 1.6em;
            margin-bottom: 1em;
            font-weight: 600;
            position: relative;
            padding-bottom: 10px;
        }
        .section-title:after {
            content: '';
            position: absolute;
            bottom: 0;
            left: 0;
            width: 50px;
            height: 3px;
            background: linear-gradient(90deg, #3498DB, #2E4057);
            border-radius: 2px;
        }
        .about-content {
            color: #566573;
            line-height: 1.9;
            font-size: 1.15em;
            text-align: justify;
        }
        </style>
        <div class="about-section">
        <div class="section-title">✨ About Me</div>
        <div class="about-content">
        Hi, I'm Melody, a data-driven marketer with a passion for exploring the world. Armed with a Master's in Big Data Marketing and diverse internships at global brands like Colgate and FrieslandCampina, I thrive at the intersection of analytics and creativity. Fluent in four languages and a travel enthusiast, I love uncovering insights from cultures as much as from data. Let's connect!🌍✨
        </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # 技能和语言部分使用卡片式设计
    st.markdown(
        """
        <style>
        .skills-section {
            background: linear-gradient(135deg, #ffffff, #f8f9fa);
            padding: 2em;
            border-radius: 20px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.08);
            margin: 1.5em 0;
            border: 1px solid rgba(52, 152, 219, 0.1);
        }
        .skill-item {
            margin: 1em 0;
            color: #566573;
            padding: 12px 20px;
            background: white;
            border-radius: 10px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
            transition: all 0.3s ease;
        }
        .skill-item:hover {
            transform: translateX(10px);
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            background: linear-gradient(to right, rgba(52, 152, 219, 0.05), white);
        }
        .skill-icon {
            margin-right: 10px;
            color: #3498DB;
        }
        </style>
        <div class="skills-section">
        <div class="section-title">🚀 Skills & Languages</div>
        <div class="skill-item">
            <span class="skill-icon">💻</span> IT Skills: Office, Python (Points: 4/4), R, SQL, PS, PR
        </div>
        <div class="skill-item">
            <span class="skill-icon">🌐</span> Languages: English (TOEFL: 98), German (Fluent), Mandarin (Native), Cantonese (Basic)
        </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    # Interactive component has been moved to the experience page
