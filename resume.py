import streamlit as st

# Custom CSS to style the resume
st.markdown("""
    <style>
    body {
        background-color: #f5f5f5;
        font-family: 'Arial', sans-serif;
    }
    .header {
        text-align: center;
        color: #4CAF50;
        font-size: 36px;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .sub-header {
        font-size: 28px;
        color: #333;
        border-bottom: 2px solid #4CAF50;
        padding-bottom: 5px;
        margin-top: 20px;
    }
    .info-box {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 15px;
        box-shadow: 0px 2px 10px rgba(0, 0, 0, 0.1);
        transition: transform 0.2s;
    }
    .info-box:hover {
        transform: scale(1.02);
        box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.15);
    }
    .info-text {
        color: #333;
        font-size: 18px;
        line-height: 1.6;
    }
    .footer {
        text-align: center;
        color: #666;
        font-size: 14px;
        margin-top: 20px;
    }
    .link {
        color: #4CAF50;
        text-decoration: none;
    }
    .link:hover {
        text-decoration: underline;
    }
    </style>
    """, unsafe_allow_html=True)

# Title of the resume
st.markdown('<h1 class="header">Syed Bilal Ahmed</h1>', unsafe_allow_html=True)

# Personal information with columns for better layout
st.markdown('<h2 class="sub-header">Personal Information</h2>', unsafe_allow_html=True)
col1, col2 = st.columns([1, 2])
with col1:
    st.image("./bilal.jpg", width=150)  # Ensure the correct path to your image
with col2:
    st.markdown("""
    <div class="info-box">
    <p class="info-text">
    - **Name:** Syed Bilal Ahmed<br>
    - **Email:** <a href="mailto:syedbilalahmed5292@gmail.com" class="link">syedbilalahmed5292@gmail.com</a><br>
    - **Phone:** +9200000000000<br>
    - **Location:** Kohat, Pakistan
    </p>
    </div>
    """, unsafe_allow_html=True)

# Work experience section
st.markdown('<h2 class="sub-header">Work Experience</h2>', unsafe_allow_html=True)
st.markdown("""
<div class="info-box">
    <p class="info-text">
    1. **Software Developer at ABC Company (2021 - Present)**<br>
    Developed and maintained web applications using Python and JavaScript. Improved system performance by 20%.<br><br>
    2. **Junior Developer at XYZ Ltd. (2019 - 2021)**<br>
    Assisted in the design and implementation of backend systems. Created automation scripts for deployment.
    </p>
</div>
""", unsafe_allow_html=True)

# Education section
st.markdown('<h2 class="sub-header">Education</h2>', unsafe_allow_html=True)
st.markdown("""
<div class="info-box">
    <p class="info-text">
    - **Bachelor's in Computer Science**<br>
    *University Name*<br>
    2022 - 2026
    </p>
</div>
""", unsafe_allow_html=True)

# Skills section
st.markdown('<h2 class="sub-header">Skills</h2>', unsafe_allow_html=True)
st.markdown("""
<div class="info-box">
    <p class="info-text">
    - **Languages:** Python, JavaScript, HTML, CSS<br>
    - **Databases:** SQL, MongoDB<br>
    - **Tools:** Git, Docker, Jenkins
    </p>
</div>
""", unsafe_allow_html=True)

# Projects section
st.markdown('<h2 class="sub-header">Projects</h2>', unsafe_allow_html=True)
st.markdown("""
<div class="info-box">
    <p class="info-text">
    1. **[E-commerce Web Application](#)**<br>
    A full-stack e-commerce platform built with Django and React.<br>
    Technologies: *Django, React, PostgreSQL*<br><br>
    2. **[Data Visualization Tool](#)**<br>
    A Python-based tool to visualize large datasets using Streamlit and Plotly.<br>
    Technologies: *Streamlit, Plotly, Pandas*
    </p>
</div>
""", unsafe_allow_html=True)

# Contact/Download Section
st.markdown('<h2 class="sub-header">Download Resume</h2>', unsafe_allow_html=True)
if st.button('Download Resume'):
    st.write("Downloading Resume... (Coming Soon!)")

# Footer Section with links
st.markdown("""
<div class="footer">
    <p>
    *This resume was built with [Streamlit](https://streamlit.io).*<br>
    Find me on <a href="https://www.linkedin.com/in/syed-bilalahmed/" class="link">LinkedIn</a> | <a href="https://github.com/syed-bilalahmed" class="link">GitHub</a>
    </p>
</div>
""", unsafe_allow_html=True)
