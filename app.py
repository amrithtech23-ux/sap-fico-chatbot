import streamlit as st
import requests
import os
import random

# Configuration
API_URL = "https://openrouter.ai/api/v1/chat/completions"
API_KEY = os.environ.get("OPENROUTER_API_KEY")
MODEL = "qwen/qwen-2.5-72b-instruct"

# Knowledge Base from demo.txt
KB = """
## FOR COMMERCE STUDENTS
### Introduction to ERP & SAP
1.1 What is ERP and why do businesses need it?
1.2 History and evolution of SAP – from R/1 to S/4HANA
1.3 Core philosophy of SAP: Best practices vs. customization
1.4 SAP modules overview: FI, CO, SD, MM, HR, PP, etc.
1.5 How SAP integrates different business functions into one system
1.6 On-premise vs. cloud deployment in SAP
1.7 Understanding SAP landscapes: Development, Quality, Production
1.8 Role of SAP in digital transformation of businesses
1.9 Industry-specific solutions in SAP (SAP for Retail, Banking, etc.)
1.10 SAP licensing models and implementation methodologies

### Introduction to SAP S/4HANA
1.1 What is SAP S/4HANA and how does it differ from traditional SAP ERP?
1.2 What does the "S/4" and "HANA" stand for in SAP S/4HANA?
1.3 What are the key benefits of SAP S/4HANA for businesses?
1.4 What are the deployment options for SAP S/4HANA?
1.5 How does SAP S/4HANA support digital transformation?
1.6 What is the Universal Journal (ACDOCA) in SAP S/4HANA?
1.7 What is the difference between SAP S/4HANA Cloud and On-Premise?
1.8 What is SAP Fiori and how does it enhance user experience?
1.9 What are the key modules in SAP S/4HANA?
1.10 How does SAP S/4HANA integrate different business functions?

### Introduction to SAP S/4HANA FICO
1.1 What is SAP S/4HANA FICO and why is it important for businesses?
1.2 What are the core components of SAP S/4HANA FICO?
1.3 How does SAP S/4HANA FICO differ from traditional accounting software?
1.4 What is the role of FICO in the overall SAP S/4HANA system?
1.5 What are the key business benefits of implementing SAP S/4HANA FICO?
1.6 How does SAP S/4HANA FICO support real-time financial reporting?
1.7 What is the difference between Financial Accounting (FI) and Controlling (CO)?
1.8 How does SAP S/4HANA FICO integrate with other SAP modules?
1.9 What is the significance of the Universal Journal in S/4HANA FICO?
1.10 How does SAP S/4HANA FICO support compliance with accounting standards?

## FOR COMPUTER SCIENCE STUDENTS
### SAP S/4HANA Technical Architecture
6.1 What is the architecture of SAP S/4HANA?
6.2 How does the Universal Journal (ACDOCA) simplify data modeling?
6.3 What is the role of the SAP HANA database in S/4HANA?
6.4 What are the different deployment options for SAP S/4HANA?
6.5 How does SAP S/4HANA leverage in-memory computing?
6.6 What is the ABAP Development environment in S/4HANA?
6.7 What are CDS (Core Data Services) views in S/4HANA?
6.8 How does S/4HANA handle multi-tenancy in cloud deployments?
6.9 What is the SAP Fiori architecture in S/4HANA?
6.10 How does SAP S/4HANA support extensibility?

## FOR MBA FINANCE STUDENTS
### SAP S/4HANA Finance – Universal Journal
11.1 What is the Universal Journal (ACDOCA) and its significance?
11.2 How does the Universal Journal replace separate GL, AP, AR, AA tables?
11.3 What are the benefits of single source of truth for finance?
11.4 How does the Universal Journal support multiple accounting principles?
11.5 What is the impact of Universal Journal on financial reporting?
11.6 How does Universal Journal enable real-time reconciliation?
11.7 What is the structure of the Universal Journal (ACDOCA) table?
11.8 How does Universal Journal support segment reporting?
11.9 What is the relationship between Universal Journal and CO tables?
11.10 How does Universal Journal improve closing processes?

## FOR SAP S/4HANA ASPIRANTS/STUDENTS
### SAP S/4HANA Learning Path
16.1 What are the prerequisites for learning SAP S/4HANA?
16.2 What are the different SAP S/4HANA certification tracks?
16.3 What is the SAP Learning Hub and how to access it?
16.4 What are the free resources on OpenSAP for S/4HANA?
16.5 How to choose the right S/4HANA module for career goals?
16.6 What are the self-study resources for S/4HANA?
16.7 What is the SAP S/4HANA certification exam pattern?
16.8 How to get hands-on experience with S/4HANA demo systems?
16.9 What are the differences between S/4HANA Cloud and On-Premise learning?
16.10 What are the career paths after S/4HANA certification?

## FOR SAP S/4HANA PROFESSIONALS
### SAP S/4HANA Migration & Conversion
21.1 What are the different migration paths to SAP S/4HANA?
21.2 What is the "System Conversion" approach and when to use it?
21.3 What is the "Landscape Transformation" approach?
21.4 What is the "New Implementation" approach?
21.5 What is the SAP Readiness Check for S/4HANA?
21.6 What is the Simplification List and how to analyze it?
21.7 What are the pre-migration activities and checks?
21.8 What is the role of the Migration Cockpit and LTMC?
21.9 How to handle custom code during migration?
21.10 What are the post-migration testing and validation strategies?
"""

# 10 Suggestion Prompts
SUGGESTIONS = [
    "What is Universal Journal (ACDOCA)?",
    "S/4HANA vs traditional SAP ERP?",
    "FI vs CO in FICO module?",
    "S/4HANA migration paths explained?",
    "Career path after SAP FICO certification?",
    "How does HANA DB enable real-time reporting?",
    "What is SAP Fiori and its benefits?",
    "System Conversion vs New Implementation?",
    "Prerequisites for learning SAP S/4HANA?",
    "How FICO integrates with SD/MM modules?"
]

# Custom CSS Styling
st.markdown("""
<style>
.stTextArea label {
    font-weight: bold !important;
    font-size: 1.15rem !important;
    color: #00008B !important;
}
.stTextArea textarea {
    background-color: #003366 !important;
    color: white !important;
    font-weight: bold !important;
    font-size: 1.1rem !important;
    border: 3px solid #00008B !important;
    border-radius: 8px;
}
.result-box {
    background-color: #003366 !important;
    color: white !important;
    font-weight: bold !important;
    font-size: 1.1rem !important;
    border: 3px solid #00008B !important;
    border-radius: 8px;
    padding: 20px;
    margin-top: 15px;
    white-space: pre-wrap;
}
.suggestion-btn {
    color: #00008B !important;
    font-weight: bold !important;
    font-size: 1.1rem !important;
    border: 2px solid #00008B !important;
    background-color: white !important;
    padding: 8px 12px !important;
    border-radius: 6px;
    cursor: pointer;
}
.suggestion-btn:hover {
    background-color: #00008B !important;
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

# Page Config
st.set_page_config(page_title="SAP FICO Chatbot", page_icon="⚖️", layout="centered")

# Title
st.title("⚖️ SAP S/4HANA FICO Chatbot")
st.caption("70+ Topics | Powered by Qwen 2.5 72B")

# Sidebar
with st.sidebar:
    st.header("🎯 Controls")
    if st.button("🔄 Reset Chat", use_container_width=True):
        st.session_state.clear()
        st.rerun()
    st.info("🤖 Model: qwen-2.5-72b-instruct")
    st.success("📚 KB: 7 Categories, 70 Topics")

# Suggestions
st.markdown("### 💡 Try These Prompts:")
cols_row1 = st.columns(5)
cols_row2 = st.columns(5)
display_prompts = random.sample(SUGGESTIONS, 10)

for i, prompt in enumerate(display_prompts[:5]):
    with cols_row1[i]:
        if st.button(prompt, key=f"s1_{i}", use_container_width=True):
            st.session_state.selected_prompt = prompt

for i, prompt in enumerate(display_prompts[5:10]):
    with cols_row2[i]:
        if st.button(prompt, key=f"s2_{i}", use_container_width=True):
            st.session_state.selected_prompt = prompt

# Input Field
st.markdown("### 📝 Enter Your SAP FICO Query:")
user_query = st.text_area(
    "Query Input",
    value=st.session_state.get("selected_prompt", ""),
    height=120,
    placeholder="e.g., Explain Universal Journal (ACDOCA)..."
)

# Submit Button
if st.button("🚀 Submit", type="primary", use_container_width=True):
    if not user_query.strip():
        st.warning("⚠️ Please enter a question.")
    elif not API_KEY:
        st.error("🔑 API Key 'OPENROUTER_API_KEY' not configured!")
    else:
        with st.spinner("🔍 Consulting SAP Knowledge Base..."):
            try:
                headers = {
                    "Authorization": f"Bearer {API_KEY}",
                    "Content-Type": "application/json"
                }
                
                system_prompt = f"""You are an expert SAP S/4HANA FICO consultant.
Target: Commerce students, CS students, MBA Finance, SAP aspirants, professionals.

Use this knowledge base:
{KB}

Guidelines:
- Clear, structured, professional answers
- Use bullet points and lists
- Reference specific topics from KB"""

                payload = {
                    "model": MODEL,
                    "messages": [
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_query}
                    ],
                    "max_tokens": 800,
                    "temperature": 0.3
                }
                
                response = requests.post(API_URL, headers=headers, json=payload, timeout=45)
                response.raise_for_status()
                answer = response.json()['choices'][0]['message']['content']
                
                st.session_state.last_answer = answer
                
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")

# Result Display
if st.session_state.get("last_answer"):
    st.markdown("### 📄 Result")
    st.markdown(f'<div class="result-box">{st.session_state.last_answer}</div>', unsafe_allow_html=True)

st.markdown("---")
st.caption("🎯 Target: Commerce | CS | MBA Finance | SAP Professionals | MIT License")
