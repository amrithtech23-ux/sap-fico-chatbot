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

# Custom CSS
st.markdown("""
<style>
.main-title {
    font-size: 2.5rem !important;
    font-weight: bold !important;
    color: #003366 !important;
    text-align: center !important;
    margin-bottom: 20px !important;
}
.subtitle {
    font-size: 1.1rem !important;
    color: #666 !important;
    text-align: center !important;
    margin-bottom: 30px !important;
}
.stTextArea label {
    font-weight: bold !important;
    font-size: 1.2rem !important;
    color: #00008B !important;
}
.stTextArea textarea {
    background-color: #003366 !important;
    color: white !important;
    font-weight: bold !important;
    font-size: 1.1rem !important;
    border: 3px solid #00008B !important;
    border-radius: 8px !important;
    padding: 15px !important;
}
.result-box {
    background-color: #003366 !important;
    color: white !important;
    font-weight: bold !important;
    font-size: 1.1rem !important;
    border: 3px solid #00008B !important;
    border-radius: 8px !important;
    padding: 25px !important;
    margin-top: 20px !important;
    white-space: pre-wrap !important;
    line-height: 1.6 !important;
}
.suggestion-box {
    background-color: white !important;
    border: 2px solid #00008B !important;
    border-radius: 8px !important;
    padding: 20px !important;
    margin: 5px !important;
    text-align: center !important;
    cursor: text !important;
}
.suggestion-text {
    color: #00008B !important;
    font-weight: bold !important;
    font-size: 1.05rem !important;
    margin: 0 !important;
    user-select: text !important;
}
.submit-btn > button {
    background-color: #003366 !important;
    color: white !important;
    font-weight: bold !important;
    font-size: 1.2rem !important;
    border: 3px solid #00008B !important;
    padding: 15px 30px !important;
}
.section-header {
    font-size: 1.3rem !important;
    font-weight: bold !important;
    color: #003366 !important;
    margin-top: 20px !important;
    margin-bottom: 15px !important;
    border-bottom: 2px solid #00008B !important;
    padding-bottom: 5px !important;
}
</style>
""", unsafe_allow_html=True)

# Page Config
st.set_page_config(page_title="SAP FICO Chatbot", page_icon="⚖️", layout="wide")

# Initialize session states
if 'last_answer' not in st.session_state:
    st.session_state.last_answer = ""
if 'reset_counter' not in st.session_state:
    st.session_state.reset_counter = 0

# Title
st.markdown('<h1 class="main-title">⚖️ SAP S/4 HANA FICO Chatbot</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">70+ Topics | Powered by Qwen 2.5 72B</p>', unsafe_allow_html=True)

# Sidebar with Reset Button
with st.sidebar:
    st.markdown("### 🎯 Controls")
    if st.button("🔄 Reset Chat", use_container_width=True, key="reset_btn"):
        # Clear session states
        st.session_state.last_answer = ""
        st.session_state.reset_counter += 1  # Increment to force widget refresh
        st.rerun()
    st.info("🤖 Model: qwen-2.5-72b-instruct")
    st.success("📚 KB: 70 Topics")

# Suggestion Prompts
st.markdown('<p class="section-header">💡 Suggestion Prompts (Select text → Right-click → Copy):</p>', unsafe_allow_html=True)

cols_row1 = st.columns(5)
cols_row2 = st.columns(5)
display_prompts = random.sample(SUGGESTIONS, 10)

# First row
for i, prompt in enumerate(display_prompts[:5]):
    with cols_row1[i]:
        st.markdown(f"""
        <div class="suggestion-box">
            <p class="suggestion-text">{prompt}</p>
        </div>
        """, unsafe_allow_html=True)

# Second row
for i, prompt in enumerate(display_prompts[5:10]):
    with cols_row2[i]:
        st.markdown(f"""
        <div class="suggestion-box">
            <p class="suggestion-text">{prompt}</p>
        </div>
        """, unsafe_allow_html=True)

# Instructions
st.info("💡 **How to use:** Select any suggestion text above → Right-click → Copy → Paste in query box below → Click Submit")

st.markdown("---")

# Query Input - Use reset_counter as part of key to force refresh on reset
st.markdown('<p class="section-header">📝 Enter Your SAP FICO Query:</p>', unsafe_allow_html=True)

user_query = st.text_area(
    label="Query Input",
    value="",
    height=150,
    placeholder="📋 Copy a suggestion above (right-click) and paste here, or type your own question...",
    key=f"query_input_{st.session_state.reset_counter}"
)

# Submit Button
st.markdown('<div class="submit-btn">', unsafe_allow_html=True)
submit_btn = st.button("🚀 Submit Query", type="primary", use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# Process query
if submit_btn:
    if not user_query.strip():
        st.warning("⚠️ Please copy a suggestion or type a question first.")
    elif not API_KEY:
        st.error("🔑 API Key not configured!")
    else:
        with st.spinner("🔍 Consulting SAP Knowledge Base..."):
            try:
                headers = {
                    "Authorization": f"Bearer {API_KEY}",
                    "Content-Type": "application/json"
                }
                
                system_prompt = f"""You are an expert SAP S/4HANA FICO consultant.
Target: Commerce, CS, MBA Finance students, SAP aspirants and professionals.

Use this knowledge base:
{KB}

Guidelines:
- Provide comprehensive, detailed answers
- Use bullet points and examples
- Reference specific topics from KB"""

                payload = {
                    "model": MODEL,
                    "messages": [
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_query}
                    ],
                    "max_tokens": 1500,
                    "temperature": 0.3
                }
                
                response = requests.post(API_URL, headers=headers, json=payload, timeout=60)
                response.raise_for_status()
                
                answer = response.json()['choices'][0]['message']['content']
                st.session_state.last_answer = answer
                
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")

# Display Result
if st.session_state.last_answer:
    st.markdown('<p class="section-header">📄 Result:</p>', unsafe_allow_html=True)
    st.markdown(f'<div class="result-box">{st.session_state.last_answer}</div>', unsafe_allow_html=True)

st.markdown("---")
st.caption("🎯 Target: Commerce | CS | MBA Finance | SAP Professionals | MIT License")
