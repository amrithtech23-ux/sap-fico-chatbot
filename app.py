import streamlit as st
import requests
import os
import random

# Configuration
API_URL = "https://openrouter.ai/api/v1/chat/completions"
API_KEY = os.environ.get("OPENROUTER_API_KEY")
MODEL = "qwen/qwen-2.5-72b-instruct"

# Knowledge Base
KB = """
SAP S/4HANA FICO Knowledge Base

FOR COMMERCE STUDENTS:
1. ERP basics and business needs
2. SAP evolution from R/1 to S/4HANA
3. SAP modules: FI, CO, SD, MM, HR, PP
4. On-premise vs cloud deployment
5. SAP landscapes: DEV, QAS, PRD
6. Digital transformation with SAP
7. Industry-specific solutions
8. SAP licensing models
9. Implementation methodologies
10. Business process integration

FOR COMPUTER SCIENCE STUDENTS:
11. S/4HANA technical architecture
12. Universal Journal ACDOCA data modeling
13. HANA database in-memory computing
14. Deployment options technical details
15. ABAP development environment
16. CDS Views and data modeling
17. Multi-tenancy cloud architecture
18. Fiori architecture and gateway
19. Extensibility options
20. Performance optimization

FOR MBA FINANCE STUDENTS:
21. Universal Journal ACDOCA significance
22. Single source of truth benefits
23. Multiple accounting principles support
24. Real-time reconciliation FI-CO
25. Segment reporting and compliance
26. Financial reporting impact
27. Closing processes improvement
28. Parallel valuation approaches
29. Currency management
30. Regulatory compliance support

FOR SAP ASPIRANTS:
31. Prerequisites for learning SAP
32. Certification tracks and levels
33. SAP Learning Hub access
34. OpenSAP free courses
35. Module selection for career
36. Self-study resources
37. Certification exam pattern
38. Demo systems access
39. Cloud vs On-Prem learning
40. Career paths after certification

FOR SAP PROFESSIONALS:
41. Migration paths to S/4HANA
42. System Conversion approach
43. Landscape Transformation
44. New Implementation greenfield
45. SAP Readiness Check
46. Simplification List analysis
47. Pre-migration activities
48. Migration Cockpit LTMC
49. Custom code handling
50. Post-migration testing

ADDITIONAL TOPICS:
51. FI vs CO difference and integration
52. General Ledger accounting
53. Accounts Payable and Receivable
54. Asset Accounting
55. Cost Center Accounting
56. Profit Center Accounting
57. Internal Orders
58. Product Costing
59. Profitability Analysis CO-PA
60. Material Ledger
61. Bank Accounting
62. Travel Management
63. Treasury Management
64. Risk Management
65. Compliance Management
66. Financial Closing Cockpit
67. Group Reporting
68. Cash Management
69. Credit Management
70. Collections Management
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

# Enhanced Custom CSS Styling
st.markdown("""
<style>
/* Main Title Styling */
.main-title {
    font-size: 2.5rem !important;
    font-weight: bold !important;
    color: #003366 !important;
    text-align: center !important;
    margin-bottom: 20px !important;
}

/* Subtitle/Caption Styling */
.subtitle {
    font-size: 1.1rem !important;
    color: #666 !important;
    text-align: center !important;
    margin-bottom: 30px !important;
}

/* Input Text Area - Blue background, white bold text, bold border */
.stTextArea label {
    font-weight: bold !important;
    font-size: 1.2rem !important;
    color: #00008B !important;
    margin-bottom: 10px !important;
}
.stTextArea textarea {
    background-color: #003366 !important;
    color: white !important;
    font-weight: bold !important;
    font-size: 1.1rem !important;
    border: 3px solid #00008B !important;
    border-radius: 8px !important;
    padding: 15px !important;
    min-height: 120px !important;
}
.stTextArea textarea:focus {
    border-color: #0000CD !important;
    box-shadow: 0 0 10px rgba(0, 0, 139, 0.3) !important;
}

/* Result Display Box - Blue background, white bold text, bold border */
.result-box {
    background-color: #003366 !important;
    color: white !important;
    font-weight: bold !important;
    font-size: 1.1rem !important;
    border: 3px solid #00008B !important;
    border-radius: 8px !important;
    padding: 25px !important;
    margin-top: 20px !important;
    margin-bottom: 20px !important;
    white-space: pre-wrap !important;
    line-height: 1.6 !important;
}

/* Suggestion Buttons - Royal blue text, bold, bigger font */
.stButton > button {
    color: #00008B !important;
    font-weight: bold !important;
    font-size: 1.05rem !important;
    border: 2px solid #00008B !important;
    background-color: white !important;
    padding: 12px 18px !important;
    border-radius: 8px !important;
    cursor: pointer !important;
    transition: all 0.3s ease !important;
    height: auto !important;
    min-height: 60px !important;
}
.stButton > button:hover {
    background-color: #00008B !important;
    color: white !important;
    border-color: #00008B !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 4px 8px rgba(0, 0, 139, 0.3) !important;
}

/* Submit Button Styling */
.submit-btn > button {
    background-color: #003366 !important;
    color: white !important;
    font-weight: bold !important;
    font-size: 1.2rem !important;
    border: 3px solid #00008B !important;
    border-radius: 8px !important;
    padding: 15px 30px !important;
    cursor: pointer !important;
    transition: all 0.3s ease !important;
}
.submit-btn > button:hover {
    background-color: #00008B !important;
    border-color: #0000CD !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 4px 12px rgba(0, 0, 139, 0.4) !important;
}

/* Reset Button Styling */
.reset-btn > button {
    background-color: #DC3545 !important;
    color: white !important;
    font-weight: bold !important;
    font-size: 1rem !important;
    border: 2px solid #C82333 !important;
    border-radius: 6px !important;
    padding: 10px 20px !important;
    cursor: pointer !important;
    transition: all 0.3s ease !important;
}
.reset-btn > button:hover {
    background-color: #C82333 !important;
    border-color: #BD2130 !important;
}

/* Sidebar Styling */
.css-1d391kg {
    background-color: #f8f9fa !important;
}

/* Section Headers */
.section-header {
    font-size: 1.3rem !important;
    font-weight: bold !important;
    color: #003366 !important;
    margin-top: 20px !important;
    margin-bottom: 15px !important;
    border-bottom: 2px solid #00008B !important;
    padding-bottom: 5px !important;
}

/* Info Boxes */
.stInfo {
    background-color: #e7f3ff !important;
    border-left: 4px solid #00008B !important;
    border-radius: 4px !important;
}

.stSuccess {
    background-color: #d4edda !important;
    border-left: 4px solid #28a745 !important;
    border-radius: 4px !important;
}

/* Footer */
.footer {
    text-align: center !important;
    color: #666 !important;
    font-size: 0.9rem !important;
    margin-top: 40px !important;
    padding-top: 20px !important;
    border-top: 1px solid #ddd !important;
}
</style>
""", unsafe_allow_html=True)

# Page Config
st.set_page_config(
    page_title="SAP FICO Chatbot",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Title
st.markdown('<h1 class="main-title">⚖️ SAP S/4HANA FICO Chatbot</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">70+ Topics | Powered by Qwen 2.5 72B | For Commerce, CS, MBA Finance & SAP Professionals</p>', unsafe_allow_html=True)

# Sidebar with Reset Button
with st.sidebar:
    st.markdown("### 🎯 Controls")
    
    # Reset Button
    st.markdown('<div class="reset-btn">', unsafe_allow_html=True)
    if st.button("🔄 Reset Chat", use_container_width=True, key="reset_btn"):
        st.session_state.clear()
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    st.info("🤖 **Model:** qwen-2.5-72b-instruct")
    st.success("📚 **Knowledge Base:** 70 Topics, 7 Categories")
    
    st.markdown("---")
    st.markdown("### 🎓 Target Audience:")
    st.markdown("- 📊 Commerce Students")
    st.markdown("- 💻 Computer Science Students")
    st.markdown("- 📈 MBA Finance Students")
    st.markdown("- 🚀 SAP Aspirants")
    st.markdown("- 👔 SAP Professionals")
    
    st.markdown("---")
    st.caption("📄 License: MIT | 🐙 GitHub + Streamlit Cloud")

# System Suggestion Prompts (10 random prompts)
st.markdown('<p class="section-header">💡 Try These Prompts:</p>', unsafe_allow_html=True)

# Display 10 prompts in 2 rows of 5 columns
cols_row1 = st.columns(5)
cols_row2 = st.columns(5)

# Shuffle and select prompts
display_prompts = random.sample(SUGGESTIONS, min(10, len(SUGGESTIONS)))

# First row (5 prompts)
for i, prompt in enumerate(display_prompts[:5]):
    with cols_row1[i]:
        if st.button(prompt, key=f"s1_{i}", use_container_width=True):
            st.session_state.selected_prompt = prompt
            st.rerun()

# Second row (5 prompts)
for i, prompt in enumerate(display_prompts[5:10]):
    with cols_row2[i]:
        if st.button(prompt, key=f"s2_{i}", use_container_width=True):
            st.session_state.selected_prompt = prompt
            st.rerun()

st.markdown("---")

# Text Field 1: User Query Input
st.markdown('<p class="section-header">📝 Enter Your SAP FICO Query:</p>', unsafe_allow_html=True)

user_query = st.text_area(
    label="Query Input",
    value=st.session_state.get("selected_prompt", ""),
    height=150,
    placeholder="e.g., Explain Universal Journal (ACDOCA) in SAP S/4HANA...",
    key="query_input",
    help="Type your SAP FICO question here. Be specific for better answers."
)

# Submit Button
st.markdown('<div class="submit-btn">', unsafe_allow_html=True)
submit_btn = st.button("🚀 Submit Query", type="primary", use_container_width=True, key="submit_btn")
st.markdown('</div>', unsafe_allow_html=True)

# Processing Logic
if submit_btn or st.session_state.get("selected_prompt"):
    if not user_query.strip():
        st.warning("⚠️ Please enter a question first.")
    elif not API_KEY:
        st.error("🔑 API Key 'OPENROUTER_API_KEY' not configured in Streamlit Cloud secrets!")
        st.info("Go to Settings → Secrets → Add OPENROUTER_API_KEY")
    else:
        with st.spinner("🔍 Consulting SAP Knowledge Base..."):
            try:
                # Prepare API request headers
                headers = {
                    "Authorization": f"Bearer {API_KEY}",
                    "Content-Type": "application/json",
                    "HTTP-Referer": "https://github.com/amrithtech23-ux/sap-fico-chatbot",
                    "X-Title": "SAP S/4HANA FICO Chatbot"
                }
                
                # System prompt with knowledge base
                system_prompt = f"""You are an expert SAP S/4HANA FICO consultant and educator.

Target audience: Commerce students, Computer Science students, MBA Finance students, 
SAP ERP aspirants, job seekers in SAP FICO, and SAP professionals.

Use this knowledge base for accurate, domain-specific answers:
{KB}

Guidelines:
- Provide COMPREHENSIVE, detailed answers (minimum 300 words)
- Use bullet points, numbered lists, and headings where appropriate
- Reference specific topics from the knowledge base when relevant
- Explain concepts clearly tailored to the user's likely background
- Include practical examples and real-world scenarios
- If unsure about a detail, say "Let me check the SAP documentation" rather than guessing
- Structure answers with: Overview, Key Points, Benefits/Challenges, Examples
"""
                
                # Prepare API payload
                payload = {
                    "model": MODEL,
                    "messages": [
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_query}
                    ],
                    "max_tokens": 1500,
                    "temperature": 0.3
                }
                
                # Call OpenRouter API
                response = requests.post(API_URL, headers=headers, json=payload, timeout=60)
                response.raise_for_status()
                
                # Extract answer
                result_data = response.json()
                bot_answer = result_data['choices'][0]['message']['content']
                
                # Store in session state
                st.session_state.last_query = user_query
                st.session_state.last_answer = bot_answer
                st.session_state.selected_prompt = None  # Clear after use
                
            except requests.exceptions.Timeout:
                st.error("⏱️ Timeout: API request took too long. Please try again.")
            except requests.exceptions.HTTPError as e:
                if response.status_code == 401:
                    st.error("🔑 Authentication failed. Check your OpenRouter API key.")
                elif response.status_code == 429:
                    st.error("⚠️ Rate limit exceeded. Please wait a moment and try again.")
                else:
                    st.error(f"❌ HTTP Error {response.status_code}: {str(e)}")
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")

# Text Field 2: Result Display (Multi-line)
if st.session_state.get("last_answer"):
    st.markdown('<p class="section-header">📄 Result:</p>', unsafe_allow_html=True)
    # Display with custom styling (blue background, white bold text, bold border)
    st.markdown(f'<div class="result-box">{st.session_state.last_answer}</div>', unsafe_allow_html=True)
    
    # Optional: Copy button for result
    st.caption("💡 **Tip:** Select and copy the answer above for your notes or documentation.")

# Footer
st.markdown("---")
st.markdown('<p class="footer">🎯 Target: Commerce | CS | MBA Finance | SAP Aspirants | SAP Professionals | 📄 MIT License | 🚀 Powered by Qwen 2.5 72B via OpenRouter</p>', unsafe_allow_html=True)
