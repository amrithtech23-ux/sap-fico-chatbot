import streamlit as st
import requests
import os
import random

# Configuration
API_URL = "https://openrouter.ai/api/v1/chat/completions"
API_KEY = os.environ.get("OPENROUTER_API_KEY")
MODEL = "qwen/qwen-2.5-72b-instruct"

# 📚 KNOWLEDGE BASE
KB = """
SAP S/4HANA FICO Complete Knowledge Base

FOR COMMERCE STUDENTS:
1. What is ERP and why do businesses need it?
   - ERP integrates all business functions into one system
   - Eliminates data silos and redundancy
   - Provides real-time visibility across the organization
   - Improves efficiency and decision-making

2. History and evolution of SAP - from R/1 to S/4HANA
   - 1972: SAP R/1 (Real-time data processing)
   - 1979: SAP R/2 (Client-server architecture)
   - 1992: SAP R/3 (3-tier architecture)
   - 2004: SAP ECC 6.0 (Enhanced functionality)
   - 2015: SAP S/4HANA (Next-generation ERP on HANA)

3. SAP modules overview: FI, CO, SD, MM, HR, PP
   - FI: Financial Accounting (GL, AP, AR, Assets)
   - CO: Controlling (Cost centers, Profit centers)
   - SD: Sales and Distribution
   - MM: Materials Management
   - HR: Human Resources
   - PP: Production Planning

4. On-premise vs cloud deployment
   - On-premise: Installed on company servers, full control
   - Cloud: Hosted by SAP, subscription-based, faster deployment
   - Hybrid: Combination of both

5. SAP landscapes: Development, Quality, Production
   - DEV: For development and configuration
   - QAS: For testing and validation
   - PRD: Live production system

FOR COMPUTER SCIENCE STUDENTS:
6. SAP S/4HANA Technical Architecture
   - Three-tier architecture: Presentation, Application, Database
   - SAP Fiori: Modern web-based user interface
   - ABAP Application Server: Business logic execution
   - SAP HANA Database: In-memory, column-oriented database

7. Universal Journal (ACDOCA) data modeling
   - Single table replaces 500+ tables
   - Combines FI and CO data
   - Real-time reporting and analytics
   - Simplified data structure

8. HANA Database features
   - In-memory computing (data in RAM)
   - Column-based storage
   - 10,000x faster than traditional databases
   - Real-time data processing

9. ABAP development environment
   - ABAP Workbench
   - Eclipse-based ADT (ABAP Development Tools)
   - CDS Views (Core Data Services)
   - AMDP (ABAP Managed Database Procedures)

10. Fiori architecture
    - Role-based, personalized interface
    - Responsive design (works on any device)
    - Tile-based launchpad
    - RESTful APIs

FOR MBA FINANCE STUDENTS:
11. Universal Journal (ACDOCA) significance
    - Single source of truth for finance
    - Combines General Ledger, AP, AR, Assets, Controlling
    - Eliminates reconciliation between FI and CO
    - Real-time financial reporting
    - Multi-currency and parallel accounting support

12. Benefits of single source of truth
    - No data redundancy
    - Consistent numbers across all reports
    - Instant financial statements
    - Faster month-end closing (70-80% time reduction)

13. Multiple accounting principles
    - Support IFRS and Local GAAP simultaneously
    - Parallel valuation approaches
    - Different ledgers for different principles
    - Automatic currency conversion

14. Real-time reconciliation
    - FI and CO always in sync
    - No batch jobs needed
    - Instant balance sheet and P&L
    - Live cash flow reporting

15. Segment reporting
    - Automatic segment derivation
    - IFRS 8 compliance
    - Profit center and segment reporting
    - Real-time segment profitability

FOR SAP ASPIRANTS:
16. Prerequisites for learning SAP S/4HANA
    - Basic understanding of business processes
    - For FICO: Accounting fundamentals
    - For technical: Programming basics helpful
    - Willingness to learn continuously

17. Certification tracks
    - Associate Level: Entry-level certification
    - Professional Level: Advanced certification
    - Specialized certifications (FICO, MM, SD, etc.)
    - SAP Learning Hub access required

18. SAP Learning Hub
    - Online learning platform
    - Access to training materials
    - Practice systems
    - Certification preparation
    - Subscription-based

19. OpenSAP free courses
    - Free MOOCs on SAP topics
    - Self-paced learning
    - Certificates of completion
    - Regular new courses

20. Career paths after certification
    - Functional Consultant
    - Technical Consultant (ABAP)
    - Business Analyst
    - Project Manager
    - Solution Architect

FOR SAP PROFESSIONALS:
21. Migration paths to S/4HANA
    - System Conversion: Technical upgrade of existing system
    - Landscape Transformation: Selective data migration
    - New Implementation: Greenfield implementation

22. System Conversion approach
    - Brownfield approach
    - Existing processes and customizations retained
    - Technical upgrade to S/4HANA
    - Faster than new implementation

23. Landscape Transformation
    - Selective data migration
    - Merge multiple systems into one
    - Data archiving and cleansing
    - Complex but flexible

24. New Implementation
    - Greenfield approach
    - Start fresh with S/4HANA
    - Process redesign opportunity
    - Cleanest approach but most time-consuming

25. SAP Readiness Check
    - Analyze current system
    - Identify custom code issues
    - Check add-on compatibility
    - Preparation for migration

26. Simplification List
    - Documents all changes in S/4HANA
    - Removed or changed functionalities
    - New features and capabilities
    - Essential for migration planning

27. Migration Cockpit and LTMC
    - Migration Cockpit: Data migration tool
    - LTMC: Legacy Transfer Migration Cockpit
    - Pre-defined migration objects
    - Guided data migration process

28. Custom code handling
    - Custom code analysis
    - Adaptation or optimization
    - Use standard functionality where possible
    - Performance optimization

29. Post-migration testing
    - Unit testing
    - Integration testing
    - User Acceptance Testing (UAT)
    - Performance testing
    - Regression testing

30. Key Tools and Resources
    - SAP Help Portal
    - SAP Community
    - SAP Notes
    - SAP Service Marketplace
    - SAP Support Portal
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
- Provide comprehensive, detailed answers
- Use bullet points and examples
- Reference specific topics from KB
- Explain clearly for different audiences"""

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

# Result Display
if st.session_state.get("last_answer"):
    st.markdown("### 📄 Result")
    st.markdown(f'<div class="result-box">{st.session_state.last_answer}</div>', unsafe_allow_html=True)

st.markdown("---")
st.caption("🎯 Target: Commerce | CS | MBA Finance | SAP Professionals | MIT License")
