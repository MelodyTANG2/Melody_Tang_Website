import warnings
import streamlit as st
import os
warnings.simplefilter(action="ignore", category=FutureWarning)

# Must be the first Streamlit command
st.set_page_config(
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items=None
)

# Import pages from the new directory
from page_content.home import home_page
from page_content.experience import experience_page
from page_content.education import education_page
from page_content.contact import contact_page

# Import components
from components.footer import display_footer #每页底部的字
from components.styles import load_css

def main():
    # Load custom CSS
    load_css()

    # 创建页面导航
    pages = {
        "🏠 Home": home_page,
        "📚 Education": education_page,
        "💼 Experience": experience_page,
        "📧 Contact": contact_page
    }
    
    # 设计侧边栏标题
    st.sidebar.markdown("""
        <h2 style='
            color: #2C3E50;
            margin: 0 0 10px 0;
            text-align: center;
            font-family: "Helvetica Neue", sans-serif;
            font-size: 1.5em;
            font-weight: 600;
        '>
            <span style='font-size: 24px;'>🎯</span> 
            Navigation
        </h2>
    """, unsafe_allow_html=True)
    
    # 添加简历下载按钮
    pdf_file_path = os.path.join("static", "docs", "resume.pdf")
    if os.path.exists(pdf_file_path):
        with open(pdf_file_path, "rb") as pdf_file:
            PDFbyte = pdf_file.read()
        
        # 美化下载按钮
        st.sidebar.markdown("""
            <style>
            div.stDownloadButton > button {
                background: linear-gradient(135deg, #2C3E50 0%, #3498DB 100%);
                color: white;
                font-size: 1.1em;
                font-weight: 500;
                border: none;
                padding: 8px 16px;
                border-radius: 8px;
                transition: all 0.3s ease;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);
                width: 100%;
                margin-bottom: -4px;
                position: relative;
                overflow: hidden;
            }
            div.stDownloadButton > button:before {
                content: '';
                position: absolute;
                top: 0;
                left: -100%;
                width: 100%;
                height: 100%;
                background: linear-gradient(135deg, rgba(255,255,255,0.2) 0%, rgba(255,255,255,0) 100%);
                transition: all 0.5s ease;
            }
            div.stDownloadButton > button:hover {
                transform: translateY(-2px);
                box-shadow: 0 6px 8px rgba(0,0,0,0.15);
            }
            div.stDownloadButton > button:hover:before {
                left: 100%;
            }
            </style>
        """, unsafe_allow_html=True)
        
        st.sidebar.download_button(
            label="📄 Download Resume",
            data=PDFbyte,
            file_name="Yajing(Melody)_Tang_Resume.pdf",
            mime='application/octet-stream',
        )
    else:
        st.sidebar.warning("Resume PDF file not found")

    # 美化导航菜单
    with st.sidebar.container():
        st.markdown("""
            <style>
            div.row-widget.stRadio > div {
                flex-direction: column;
                margin-top: -5px;
            }
            div.row-widget.stRadio > div[role="radiogroup"] {
                display: grid;
                grid-template-columns: 1fr;
                gap: 8px;
            }
            div.row-widget.stRadio > div[role="radiogroup"] > label {
                background: #ffffff;
                padding: 12px 16px;
                border-radius: 10px;
                border-left: 4px solid transparent;
                box-shadow: 0 2px 4px rgba(0,0,0,0.05);
                transition: all 0.3s ease;
                cursor: pointer;
                margin: 0;
                height: 45px;
                display: flex;
                align-items: center;
            }
            div.row-widget.stRadio > div[role="radiogroup"] > label:hover {
                border-left: 4px solid #4A90E2;
                background: linear-gradient(90deg, #f8f9fa 0%, #ffffff 100%);
                transform: translateX(5px);
            }
            div.row-widget.stRadio > div[role="radiogroup"] > label > div {
                font-size: 1.1em;
                font-weight: 600;
                color: #2C3E50;
                display: flex;
                align-items: center;
                gap: 10px;
            }
            /* 选中状态的样式 */
            div.row-widget.stRadio > div[role="radiogroup"] > label[data-checked="true"] {
                background: #f0f4f8;
                border-left: 4px solid #2C3E50;
            }
            div.row-widget.stRadio > div[role="radiogroup"] > label[data-checked="true"] > div {
                color: #1a1a1a;
            }
            </style>
        """, unsafe_allow_html=True)
        
        # 初始化默认页面
        if 'current_page' not in st.session_state:
            st.session_state['current_page'] = "🏠 Home"
        
        # 使用radio组件进行页面选择
        selection = st.sidebar.radio("", list(pages.keys()))
        st.session_state['current_page'] = selection
    
    # 运行选中的页面
    pages[selection]()
    
    # Display footer at the bottom of each page
    display_footer()

if __name__ == "__main__":
    main()
