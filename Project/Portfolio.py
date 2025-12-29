import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
import time
import os

# Page configuration with updated settings
st.set_page_config(
    page_title="My Portfolio",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Find the directory where THIS script (Portfolio.py) is located
current_dir = os.path.dirname(os.path.abspath(__file__))

# Define the paths based on that location
css_file = os.path.join(current_dir, "style.css")
img_file = os.path.join(current_dir, "Frontend.png")

# Custom CSS for better styling
def local_css(file_path):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css(css_file)

# Load Lottie animations
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
lottie_web = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_ikfdhz1h.json")
lottie_contact = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_3rwasyjy.json")

# Load image
img_cert = Image.open(img_file)

# Header with gradient text
st.markdown("""
    <div class="main-header">
        <h1>🌟 Welcome to My Digital Portfolio</h1>
        <p class="subtitle">Web Developer • Problem Solver • Creative Thinker</p>
    </div>
""", unsafe_allow_html=True)

# Create tabs with icons
tab1, tab2, tab3 = st.tabs(["🏠 Overview", "💻 Web Development", "📞 Connect"])

with tab1: 
    with st.container():
        st.write("##")
        left_column, right_column = st.columns([3, 2])
        with left_column:
            st.markdown("""
                <div class="card">
                    <h2>👨‍💻 About Me</h2>
                    <p>I'm a passionate developer and student at LNCT, constantly exploring the intersection of technology and creativity.</p>
                </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
                <div class="skills-container">
                    <h3>🎯 My Skills</h3>
                    <div class="skills-grid">
                        <span class="skill-tag">HTML/CSS</span>
                        <span class="skill-tag">JavaScript</span>
                        <span class="skill-tag">Python</span>
                        <span class="skill-tag">Streamlit</span>
                        <span class="skill-tag">Git/GitHub</span>
                        <span class="skill-tag">Data Science</span>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
                <div class="interests">
                    <h3>🎮 Interests</h3>
                    <ul>
                        <li>♟️ Competitive Chess Player</li>
                        <li>💡 Problem Solving & Algorithms</li>
                        <li>🎨 UI/UX Design</li>
                        <li>📊 Data Visualization</li>
                    </ul>
                </div>
            """, unsafe_allow_html=True)
            
            # GitHub button with better styling
            st.markdown("""
                <div style="text-align: center; margin-top: 30px;">
                    <a href="https://github.com/Mikky-mlh" target="_blank" class="github-button">
                        <span>📂 View My GitHub</span>
                    </a>
                </div>
            """, unsafe_allow_html=True)
            
        with right_column:
            if lottie_coding:
                st_lottie(lottie_coding, height=350, key="coding", speed=1)
            else:
                st.info("Animation loading...")
            st.markdown("""
                <div style="text-align: center; margin-top: 20px;">
                    <div class="stats">
                        <div class="stat-item">
                            <div class="stat-number">10+</div>
                            <div class="stat-label">Projects</div>
                        </div>
                        <div class="stat-item">
                            <div class="stat-number">5+</div>
                            <div class="stat-label">Certifications</div>
                        </div>
                        <div class="stat-item">
                            <div class="stat-number">100%</div>
                            <div class="stat-label">Passion</div>
                        </div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

    with st.container():
        st.markdown("---")
        st.markdown("""
            <div class="section-header">
                <h2>🏆 Certifications & Achievements</h2>
            </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns([1, 2])
        with col1:
            # Add shadow and border to image
            st.markdown("""
                <div class="certificate-container">
            """, unsafe_allow_html=True)
            st.image(img_cert)
            st.markdown("</div>", unsafe_allow_html=True)
        with col2:
            st.markdown("""
                <div class="certificate-details">
                    <h3>🎨 Frontend Development Certification</h3>
                    <p>Completed comprehensive frontend development course covering:</p>
                    <ul>
                        <li>Responsive Web Design</li>
                        <li>Modern CSS Techniques</li>
                        <li>JavaScript Fundamentals</li>
                        <li>UI/UX Principles</li>
                    </ul>
                    <div class="badge">Verified Certificate</div>
                </div>
            """, unsafe_allow_html=True)

with tab2:
    if lottie_web:
        st_lottie(lottie_web, height=200, key="web", speed=1)
    else:
        st.markdown("### 💻 Web Development Projects")
    
    projects = [
        {
            "title": "Technical Documentation Page",
            "status": "✅ Completed",
            "date": "Dec 15, 2025",
            "description": "A comprehensive technical documentation page serving as a complete portfolio showcase with interactive elements and smooth navigation.",
            "demo": "https://mikky-mlh.github.io/Web-Projects/Projects/Documentation%20Project/",
            "tech": ["HTML", "CSS", "JavaScript"]
        },
        {
            "title": "Survey Form",
            "status": "✅ Completed",
            "date": "Nov 29, 2025",
            "description": "Modern survey form with glassmorphism design, gradient backgrounds, and form validation.",
            "demo": "https://mikky-mlh.github.io/Web-Projects/Projects/Survey%20Form/",
            "tech": ["HTML", "CSS", "JavaScript"]
        },
        {
            "title": "Tribute Page",
            "status": "✅ Completed",
            "date": "Dec 8, 2025",
            "description": "Responsive tribute page honoring Terry A. Davis with timeline and interactive elements.",
            "demo": "https://mikky-mlh.github.io/Web-Projects/Projects/Tribute%20Page/",
            "tech": ["HTML", "CSS"]
        },
        {
            "title": "Product Landing Page",
            "status": "✅ Completed",
            "date": "Dec 24, 2025",
            "description": "Futuristic landing page for Zenith G1 quantum computer with email integration and animations.",
            "demo": "https://mikky-mlh.github.io/Web-Projects/Projects/Product%20Landing%20Page/",
            "tech": ["HTML", "CSS", "JavaScript"]
        }
    ]
    
    for i, project in enumerate(projects):
        with st.container():
            st.markdown(f"### {project['title']}")
            col1, col2 = st.columns([1, 2])
            with col1:
                st.markdown(f"""
                    <div class="project-meta">
                        <p><strong>Status:</strong> {project['status']}</p>
                        <p><strong>Date:</strong> {project['date']}</p>
                        <div class="tech-tags">
                            {" ".join([f'<span class="tech-tag">{tech}</span>' for tech in project["tech"]])}
                        </div>
                    </div>
                """, unsafe_allow_html=True)
            with col2:
                st.markdown(f"""
                    <div class="project-description">
                        <p>{project['description']}</p>
                        <a href="{project['demo']}" target="_blank" class="demo-button">
                            🔗 Live Demo
                        </a>
                    </div>
                """, unsafe_allow_html=True)
            
            if i < len(projects) - 1:
                st.markdown("<hr class='project-divider'>", unsafe_allow_html=True)

with tab3:
    with st.container():
        left_col, right_col = st.columns([1, 1])
        
        with left_col:
            if lottie_contact:
                st_lottie(lottie_contact, height=300, key="contact", speed=1)
            else:
                st.markdown("### 📞 Contact")
            
        with right_col:
            st.markdown("""
                <div style="background-color: #1E1E1E; border-radius: 10px; padding: 20px; font-family: 'Consolas', 'Monaco', monospace; box-shadow: 0 4px 6px rgba(0,0,0,0.3); border: 1px solid #333;">
                    <div style="display: flex; gap: 8px; margin-bottom: 15px; border-bottom: 1px solid #333; padding-bottom: 10px;">
                        <div style="width: 12px; height: 12px; border-radius: 50%; background-color: #FF5F56;"></div>
                        <div style="width: 12px; height: 12px; border-radius: 50%; background-color: #FFBD2E;"></div>
                        <div style="width: 12px; height: 12px; border-radius: 50%; background-color: #27C93F;"></div>
                        <span style="margin-left: 10px; color: #888; font-size: 12px;">contact.json</span>
                    </div>
                    <div style="color: #D4D4D4; line-height: 1.6;">
                        <span style="color: #C586C0;">{</span><br>
                        &nbsp;&nbsp;<span style="color: #9CDCFE;">"name"</span>: <span style="color: #CE9178;">"Yuvraj Sarathe"</span>,<br>
                        &nbsp;&nbsp;<span style="color: #9CDCFE;">"email"</span>: <span style="color: #CE9178;">"yuvrajsarathe07@gmail.com"</span>,<br>
                        &nbsp;&nbsp;<span style="color: #9CDCFE;">"phone"</span>: <span style="color: #CE9178;">"+91 8349498358"</span>,<br>
                        &nbsp;&nbsp;<span style="color: #9CDCFE;">"location"</span>: <span style="color: #CE9178;">"Bhopal, India"</span>,<br>
                        &nbsp;&nbsp;<span style="color: #9CDCFE;">"status"</span>: <span style="color: #CE9178;">"Open to Opportunities"</span><br>
                        <span style="color: #C586C0;">}</span>
                </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
            <div class="social-links">
                <h3>🌐 Connect With Me</h3>
                <a href="https://github.com/Mikky-mlh" target="_blank" class="social-button github">
                    <span>🐙 GitHub</span>
                </a>
                <a href="https://linkedin.com/in/yourprofile" target="_blank" class="social-button linkedin">
                    <span>💼 LinkedIn</span>
                </a>
                <a href="https://mikky-mlh.github.io/Portfolio/" target="_blank" class="social-button portfolio">
                    <span>🌐 Portfolio</span>
                </a>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div class="contact-form-container">
                <h3>✉️ Send a Message</h3>
        """, unsafe_allow_html=True)
        
        with st.form("contact_form", clear_on_submit=True):
            name = st.text_input("👤 Your Name", placeholder="Enter your name")
            email = st.text_input("📧 Your Email", placeholder="Enter your email")
            message = st.text_area("💭 Your Message", placeholder="Type your message here...", height=100)
            
            col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
            with col_btn2:
                submitted = st.form_submit_button("🚀 Send Message", use_container_width=True)
            
            if submitted:
                if name and email and message:
                    with st.spinner("📤 Sending your message..."):
                        time.sleep(1.5)
                    st.success("✅ Message sent successfully! I'll get back to you soon.")
                else:
                    st.warning("⚠️ Please fill all fields")

# Footer
st.markdown("""
    <div class="footer">
        <p>Made with ❤️ using Streamlit • Last Updated: December 2025</p>
    </div>
""", unsafe_allow_html=True)