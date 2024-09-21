import streamlit as st

# Title of the resume
st.title("Syed Bilal Ahmed")

# Personal information with columns for better layout
st.header("Personal Information")
col1, col2 = st.columns([1, 2])
with col1:
    st.image("https://via.placeholder.com/150", width=150)  # Replace with your own image URL
with col2:
    st.markdown("""
    - **Name:** Syed Bilal Ahmed
    - **Email:** [syedbilalahmed5292@gmail.com](mailto:syedbilalahmed5292@gmail.com)  
    - **Phone:** +9200000000000  
    - **Location:** Kohat, Pakistan  
    """)

# Work experience section
st.header("Work Experience")
st.markdown("""
1. **Software Developer at ABC Company (2021 - Present)**  
   *Developed and maintained web applications using Python and JavaScript. Improved system performance by 20%.*

2. **Junior Developer at XYZ Ltd. (2019 - 2021)**  
   *Assisted in the design and implementation of backend systems. Created automation scripts for deployment.*
""")

# Education section
st.header("Education")
st.markdown("""
- **Bachelor's in Computer Science**  
  *University Name*  
  2022 - 2026
""")

# Skills section with bullet points
st.header("Skills")
st.markdown("""
- **Languages:** Python, JavaScript, HTML, CSS  
- **Databases:** SQL, MongoDB  
- **Tools:** Git, Docker, Jenkins
""")

# Projects section with links and descriptions
st.header("Projects")
st.markdown("""
1. **[E-commerce Web Application](#)**  
   A full-stack e-commerce platform built with Django and React.  
   Technologies: *Django, React, PostgreSQL*

2. **[Data Visualization Tool](#)**  
   A Python-based tool to visualize large datasets using Streamlit and Plotly.  
   Technologies: *Streamlit, Plotly, Pandas*
""")

# Contact/Download Section
st.header("Download Resume")
if st.button('Download Resume'):
    st.write("Downloading Resume... (Coming Soon!)")

# Footer Section with links
st.markdown("""
---
*This resume was built with [Streamlit](https://streamlit.io).*  
Find me on [LinkedIn](https://www.linkedin.com) | [GitHub](https://github.com)
""")
