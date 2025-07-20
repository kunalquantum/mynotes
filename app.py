import streamlit as st
import base64
import os

# --- Page Configuration ---
st.set_page_config(
    page_title="Dark Learn | Cloud & DevOps Notes",
    page_icon="☁️",
    layout="wide",
    initial_sidebar_state="auto"
)

# --- Global Variables / Company Info ---
MY_NAME = "Kunal Sharma"
COMPANY_NAME = "Dark Learn"
RESUME_PDF_PATH = "Kunal_Sharma_Resume.pdf" # Path to your original resume PDF for download
LOGO_PATH = "logo4.png" # Path to your company logo file
PROFILE_PIC_PATH = "me.jpg" # <--- IMPORTANT: Path to your profile picture

# --- Your Resume/Contact Information (extracted from PDF content) ---
CONTACT_INFO = {
    "Name": MY_NAME,
    "Phone": "9892768818",
    "Email": "kunal.lalbahdur.sharma05@gmail.com",
    "LinkedIn": "https://www.linkedin.com/in/kunal-sharma-601812247/",
    "GitHub": "https://github.com/kunalquantum"
}

OBJECTIVE = """
I am a technophile who easily identifies problems and enjoys solving them. I love learning about new concepts
and applying them, often making personal modifications to address daily life challenges with innovative solutions.
While I primarily enjoy coding in Java, I also appreciate Python, particularly in the realms of data science and machine learning.
Additionally, I believe that strong management and leadership skills are essential for effectively driving projects to completion—the ultimate objective.
"""

EDUCATION = [
    {"institution": "Saraswati College of Engineering", "degree": "Computer Engineering", "years": "2021-present", "score": "8.5 CGPA"},
    {"institution": "Jai Hind College", "degree": "HSC", "years": "2019-2021", "score": "84%"},
    {"institution": "Dr Antonio Da Silva Technical High School", "degree": "SSC", "years": "2007-2019", "score": "83%"}
]

TECHNICAL_SKILLS = {
    "Machine Learning & Data Science": ["Machine learning", "Data Science", "Python", "Scikit learn", "Tensorflow", "Exploratory data Analysis", "Data Cleaning", "Data Insights", "Deep learning"],
    "Java Technologies": ["Java/core/Advanced", "JDBC", "Servlet/JSP"],
    "Web Development": ["HTML", "Css", "Javascript"],
    "Databases": ["SQL"],
    "Version Control": ["Github"]
}

CERTIFICATIONS_TRAINING = [
    "Microsoft Azure Certification in entry level A1-900",
    "Acmegrade Training in Data Science",
    "Python Workshop",
    "AI Workshop",
    "UI designing",
    "Cyber Security"
]

INTERNSHIP = {
    "company": "S.P.R.K Technologies",
    "role": "Java backend developer intern",
    "duration": "1 month"
}

HACKATHONS = [
    "Smart India Hackathons (2022-23), (2023-24)",
    "Nasa Space App Challenge (2022-23), (2023-24)",
    "Avishkar National Hackathon (2022-23) [Winner]",
    "Hack2Crack Hackathon at Amity University"
]

PROJECTS = [
    {
        "name": "Samarthya (Data Structure Visualizer)",
        "year": "2024 - Current",
        "description": "1st Ranked in Avishkar National level Project Competition.",
        "github_link": "https://github.com/kunalquantum/samarthya20.git",
        "live_link": "https://lucent-rolypoly-d1748b.netlify.app/"
    },
    {
        "name": "Block-Banking",
        "year": "2024-2024",
        "description": "Blockchain-based banking system that securely performs transactions between two customers using personalized credentials.",
        "github_link": None,
        "live_link": None
    },
    {
        "name": "SmartData Hub",
        "year": "2023-2024",
        "description": "National Level Qualified for Nasa Space App Hackathon. Automation for Data Cleaning, Preprocessing, Visualization, Model Training, Advanced Data Cleaning.",
        "github_link": "https://github.com/kunalquantum/SmartData-Hub.git",
        "live_link": "https://kunalapp-epbvq9icbenpksr8pj8krx.streamlit.app/SmartData Hub"
    },
    {
        "name": "Health Mate",
        "year": "2022-2023",
        "description": "Digital health examiner and cure recommender for critical and noncritical diseases.",
        "github_link": None,
        "live_link": None
    },
    {
        "name": "InstaMate 1 and 2.0",
        "year": "2022-2023",
        "description": "Automating Instagram using Deep Learning and Natural Language Processing.",
        "github_link": "https://github.com/kunalquantum/Insta-Mate.git",
        "live_link": None
    }
]

INTERESTS = ["Data Science", "Automation", "Software development", "Deep learning", "Machine learning", "Leadership and team building"]

EXTRA_CURRICULAR = [
    "General Advisor - Student council",
    "Vice president - Computer Department student associations",
    "Head-boy - School",
    "Participated in 5+ hackathons (Won 1)"
]


# --- Section Definitions (for Home Page Cards) ---
SECTIONS = [
    {
        "title": "Section 1: Cloud Concepts",
        "icon": "☁️",
        "insight": "Explore the fundamentals of cloud computing, including benefits, key terminology, and service models (IaaS, PaaS, SaaS) across 20 detailed lessons.",
        "pdf_path": "notes/section1_cloud_concepts.pdf",
        "lessons": [
            "Lesson 1: Introduction", "Lesson 2: What is Cloud Computing (6 mins)",
            "Lesson 3: What is CC (6 mins)", "Lesson 4: Benefits of Cloud Computing (10 mins)",
            "Lesson 5: Key Concepts and Terminology (6 mins)", "Lesson 6: Economies of Scale (2 mins)",
            "Lesson 7: Capex vs Opex (3 mins)", "Lesson 8: Public Cloud (2 mins)",
            "Lesson 9: Characteristics of Public Cloud (2 mins)", "Lesson 10: Private Cloud (2 mins)",
            "Lesson 11: Characteristics of Private Cloud (2 mins)", "Lesson 12: Hybrid Cloud (2 mins)",
            "Lesson 13: Characteristics of Hybrid Cloud (2 mins)", "Lesson 14: Review and What Next (1 min)",
            "Lesson 15: IaaS (4 mins)", "Lesson 16: Use Cases of IaaS (2 mins)",
            "Lesson 17: What is PaaS (3 mins)", "Lesson 18: Common Scenarios PaaS (4 mins)",
            "Lesson 19: What is SaaS (3 mins)", "Lesson 20: Share Responsibility Model (10 mins)"
        ]
    },
    {
        "title": "Section 2: Core Azure Services",
        "icon": "🔵",
        "insight": "Dive deep into Azure's foundational services like Regions, Availability Zones, VMs, Containers, Networking, Storage, and various specialized services across 48 lessons.",
        "pdf_path": "notes/section2_core_azure_services.pdf",
        "lessons": [
            "Lesson 1: Introduction (1 min)", "Lesson 2: Azure Regions (2 mins)",
            "Lesson 3: Special Azure Regions (2 mins)", "Lesson 4: Region Pairs (2 mins)",
            "Lesson 5: Feature Availability Region Wise (2 mins)", "Lesson 6: Availability Zones (2 mins)",
            "Lesson 7: Availability Sets (3 mins)", "Lesson 8: What are Resource Groups (2 mins)",
            "Lesson 9: Azure Resource Manager (2 mins)", "Lesson 10: Azure Core Services and Products (3 mins)",
            "Lesson 11: What is Azure Compute (1 min)", "Lesson 12: Azure Virtual Machines Audio Cast Only (2 mins)",
            "Lesson 13: Virtual Machines Lab", "Lesson 14: Virtual Machines II Lab",
            "Lesson 15: Virtual Machines III Lab", "Lesson 16: Virtual Machines IV Lab",
            "Lesson 17: Virtual Machines V Lab", "Lesson 18: Virtual Machine VI Lab",
            "Lesson 19: What are Containers", "Lesson 20: Containers (Lab Activity)",
            "Lesson 21: What Are Virtual Networks", "Lesson 22: Virtual Networks Lab",
            "Lesson 23: Azure Load Balancer", "Lesson 24: VPN Gateway",
            "Lesson 25: Azure Application Gateway I", "Lesson 26: Azure Content Delivery Networks (CDN's)",
            "Lesson 27: Azure Storage Services", "Lesson 28: Structured Data",
            "Lesson 29: Semi-Structured Data", "Lesson 30: Unstructured Data",
            "Lesson 31: Azure Database Services", "Lesson 32: Azure SQL Lab Demo",
            "Lesson 33: Azure Marketplace", "Lesson 34: What is Internet of Things (IoT) Intro",
            "Lesson 35: IoT Hub", "Lesson 36: Azure Big Data and Analytics",
            "Lesson 37: Azure SQL Data Warehouse", "Lesson 38: Azure HDInsights",
            "Lesson 39: Azure Data Lake Analytics", "Lesson 40: Machine Learning",
            "Lesson 41: What is Serverless Computing", "Lesson 42: The Concept of DevOps",
            "Lesson 43: Azure Management Tools", "Lesson 44: Creating Resources with PowerShell Lab Activity",
            "Lesson 45: Creating Resources with Azure CLI Lab Activity", "Lesson 46: Provision Resources using Cloud Shell Lab Activity",
            "Lesson 47: Azure Advisor", "Lesson 48: What Did We Learn"
        ]
    },
    {
        "title": "Section 3: Security, Privacy, Compliance, and Trust",
        "icon": "🔒",
        "insight": "Understand the critical aspects of security, data privacy, regulatory compliance, and building trust in cloud environments. (Details to be provided in the PDF).",
        "pdf_path": "notes/section3_security_privacy_compliance_trust.pdf",
        "lessons": ["Details available in PDF"]
    },
    {
        "title": "Section 4: Azure Pricing and Support",
        "icon": "💲",
        "insight": "Learn about Azure subscriptions, cost management strategies, pricing calculators, support plans, and Service Level Agreements (SLAs) across 21 lessons.",
        "pdf_path": "notes/section4_azure_pricing_support.pdf",
        "lessons": [
            "Lesson 1: Module 4 Introduction - What to Expect in This Module", "Lesson 2: Azure Subscriptions",
            "Lesson 3: What are Management Groups", "Lesson 4: Purchase Azure Products & Services - Available Options",
            "Lesson 5: Usage Metrics", "Lesson 6: Factors Affecting Costs",
            "Lesson 7: The Concept of Zones for Billing", "Lesson 8: Azure Pricing Calculator",
            "Lesson 9: Azure Total Cost of Ownership (TCO)", "Lesson 10: Ways to Minimize Costs in Azure",
            "Lesson 11: Azure Cost Management", "Lesson 12: Azure Support Plans (4 mins)",
            "Lesson 13: Alternative Support Options", "Lesson 14: Service Level Agreements (SLA's)",
            "Lesson 15: Composite SLA's", "Lesson 16: Improving Application SLA's",
            "Lesson 17: Public and Features", "Lesson 18: Providing Feedback",
            "Lesson 19: General Availability", "Lesson 20: Azure Updates, Announcements, and Roadmaps",
            "Lesson 21: Conclusion (1 min)"
        ]
    }
]

# --- Function to display PDF (still used for notes) ---
def display_pdf(file_path):
    if not os.path.exists(file_path):
        st.error(f"File not found: {file_path}. Please ensure it's in the correct directory and spelled correctly.")
        return

    try:
        with open(file_path, "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')

        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="800px" type="application/pdf" style="border: none;"></iframe>'
        st.markdown(pdf_display, unsafe_allow_html=True)
    except Exception as e:
        st.error(f"Error displaying PDF: {e}")
        st.info("Consider trying the download button instead if embedding fails.")

# --- Header with Logo, Main Title, and Buttons ---
header_col1, header_col2, header_col3 = st.columns([1, 4, 1])

with header_col1:
    if os.path.exists(LOGO_PATH):
        st.image(LOGO_PATH, width=80) # Adjust width as needed for your logo
    else:
        st.write("*(Logo file not found)*") # Placeholder if logo file is missing

with header_col2:
    st.markdown(f"<h1 style='text-align: center; color: #FF4B4B; margin-bottom: 0px;'>{COMPANY_NAME}</h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center; font-size: 14px; color: grey; margin-top: 0px;'>Developed by {MY_NAME}</p>", unsafe_allow_html=True)

with header_col3:
    btn_col1, btn_col2 = st.columns(2)
    with btn_col1:
        if st.button("Home 🏠", use_container_width=True, type="primary"):
            st.session_state.page = "Home"
            st.session_state.viewing_pdf = None # Reset any active PDF view
    with btn_col2:
        if st.button("Resume 🧑‍💻", use_container_width=True):
            st.session_state.page = "Resume"
            st.session_state.viewing_pdf = None # Reset any active PDF view

st.markdown("---") # Horizontal line below the header

# --- Initialize session state for page navigation and PDF display ---
if 'page' not in st.session_state:
    st.session_state.page = "Home" # Default to Home page
if 'viewing_pdf' not in st.session_state:
    st.session_state.viewing_pdf = None # Stores the path of the PDF currently being viewed


# --- Main Content Area ---

if st.session_state.page == "Home":
    st.header("Cloud Learning and DevOps Notes", divider='rainbow')
    st.markdown("Welcome to your centralized hub for Cloud and DevOps learning modules. Click on any section card to view its detailed notes.")

    # Display Sections in a Grid
    cols_per_row = 2 # Display 2 cards per row for better readability with longer insights
    rows = [st.columns(cols_per_row) for _ in range((len(SECTIONS) + cols_per_row - 1) // cols_per_row)]

    for i, section in enumerate(SECTIONS):
        row_idx = i // cols_per_row
        col_idx = i % cols_per_row
        with rows[row_idx][col_idx]:
            with st.container(border=True): # Card-like appearance
                st.subheader(f"{section['icon']} {section['title']}")
                st.write(f"*{section['insight']}*")
                st.markdown("---")
                if st.button(f"View Notes PDF for {section['title']}", key=f"view_pdf_{i}", use_container_width=True, type="secondary"):
                    st.session_state.viewing_pdf = section['pdf_path']

    # --- Display PDF if one is selected ---
    if st.session_state.viewing_pdf:
        st.markdown("---")
        # Extract just the filename for display, e.g., "section1_cloud_concepts.pdf"
        st.subheader(f"Viewing: {os.path.basename(st.session_state.viewing_pdf).replace('.pdf', '').replace('_', ' ').title()}")
        display_pdf(st.session_state.viewing_pdf)
        st.markdown("---")
        if st.button("Hide PDF", type="secondary"):
            st.session_state.viewing_pdf = None
            st.experimental_rerun() # Rerun to hide immediately

    st.markdown("---") # Separator before "Explore More" section
    st.header("What's Next for Dark Learn?", divider='blue')
    st.write("We are continuously expanding our content to bring you more in-depth knowledge and practical guides on advanced Cloud technologies, DevOps practices, and emerging tech trends.")
    st.info("Stay tuned for new modules, interactive labs, and community features!")
    # You could add a button here that links to a 'Coming Soon' page or your social media
    if st.button("Explore More Resources & Updates 🚀", use_container_width=True, type="secondary"):
        st.write("*(This button would typically navigate to a 'Coming Soon' page, blog, or contact form.)*")
        # Example: st.markdown("[Visit our Blog for Updates!](https://your-blog-link.com)")


elif st.session_state.page == "Resume":
    st.markdown(f"<h1 style='text-align: center; color: #FF4B4B;'>{MY_NAME}</h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center; font-size: 16px; color: grey;'>{CONTACT_INFO['Phone']} | {CONTACT_INFO['Email']} | <a href='{CONTACT_INFO['LinkedIn']}' target='_blank'>LinkedIn</a> | <a href='{CONTACT_INFO['GitHub']}' target='_blank'>GitHub</a></p>", unsafe_allow_html=True)
    st.markdown("---")

    # --- Profile Image and Objective ---
    col_img, col_objective = st.columns([1, 4]) # Adjust ratio as needed

    with col_img:
        st.markdown("") # Add a little space
        if os.path.exists(PROFILE_PIC_PATH):
            # FIX: Changed use_column_width=False to use_container_width=False to remove deprecation warning
            st.image(PROFILE_PIC_PATH, caption="Your Photo", width=150, use_container_width=False)
        else:
            st.warning("Profile image 'profile_pic.png' not found. Please add it to your project directory.")

    with col_objective:
        st.subheader("Objective")
        st.write(OBJECTIVE)

    st.markdown("---") # Horizontal line after objective

    # --- Technical Skills ---
    st.subheader("Technical Skills")
    skills_cols = st.columns(3) # Display skills in 3 columns
    skill_categories = list(TECHNICAL_SKILLS.keys())
    for i, category in enumerate(skill_categories):
        with skills_cols[i % 3]: # Cycle through columns
            st.markdown(f"**{category}:**")
            for skill in TECHNICAL_SKILLS[category]:
                st.markdown(f"- {skill}")
    st.markdown("---")

    # --- Education ---
    st.subheader("Education")
    for edu in EDUCATION:
        col_edu_left, col_edu_right = st.columns([3, 1])
        with col_edu_left:
            st.markdown(f"**{edu['institution']}**")
            st.markdown(f"*{edu['degree']}*")
        with col_edu_right:
            st.markdown(f"*{edu['years']}*")
            st.markdown(f"*{edu['score']}*")
        st.markdown("") # Small gap
    st.markdown("---")

    # --- Certifications & Training ---
    st.subheader("Certifications & Training")
    cert_cols = st.columns(3) # Arrange certifications in columns
    for i, cert in enumerate(CERTIFICATIONS_TRAINING):
        with cert_cols[i % 3]:
            st.markdown(f"- {cert}")
    st.markdown("---")

    # --- Internship ---
    st.subheader("Internship")
    st.markdown(f"**{INTERNSHIP['company']}** - *{INTERNSHIP['role']}*")
    st.markdown(f"Duration: {INTERNSHIP['duration']}")
    st.markdown("---")

    # --- Projects ---
    st.subheader("Projects")
    for project in PROJECTS:
        st.markdown(f"**{project['name']}** ({project['year']})")
        st.write(project['description'])
        project_links = []
        if project['github_link']:
            project_links.append(f"[GitHub]({project['github_link']})")
        if project['live_link']:
            project_links.append(f"[Live Demo]({project['live_link']})")
        if project_links:
            st.markdown(" | ".join(project_links))
        st.markdown("---") # Separator for projects

    # --- Hackathons ---
    st.subheader("Hackathons")
    for hackathon in HACKATHONS:
        st.markdown(f"- {hackathon}")
    st.markdown("---")

    # --- Extra Curricular ---
    st.subheader("Extra-Curricular Activities")
    for activity in EXTRA_CURRICULAR:
        st.markdown(f"- {activity}")
    st.markdown("---")

    # --- Interests ---
    st.subheader("Interests")
    st.write(", ".join(INTERESTS))
    st.markdown("---")

    # --- Option to download original PDF resume ---
    st.subheader("Download Full Resume (PDF)")
    try:
        with open(RESUME_PDF_PATH, "rb") as pdf_file:
            st.download_button(
                label="Download Resume ⬇️",
                data=pdf_file.read(),
                file_name="Kunal_Sharma_Resume.pdf",
                mime="application/pdf",
                use_container_width=True,
                type="primary"
            )
    except FileNotFoundError:
        st.warning(f"Resume PDF not found at {RESUME_PDF_PATH}. Download option unavailable.")
    except Exception as e:
        st.error(f"Error preparing resume for download: {e}")

    st.caption(f"© 2025 {MY_NAME} for {COMPANY_NAME}. All rights reserved.")