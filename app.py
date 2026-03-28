import streamlit as st
import requests
import os
import random

# Configuration
API_URL = "https://openrouter.ai/api/v1/chat/completions"
API_KEY = os.environ.get("OPENROUTER_API_KEY")
MODEL = "qwen/qwen-2.5-72b-instruct"

# 📚 COMPREHENSIVE KNOWLEDGE BASE
KB = """
================================================================================
SAP S/4HANA FICO COMPREHENSIVE KNOWLEDGE BASE
================================================================================

## SECTION 1: FOR COMMERCE STUDENTS

### 1.1 Introduction to ERP & SAP
- What is ERP and why businesses need integrated systems
- SAP evolution: R/1 (1972) → R/2 (1979) → R/3 (1992) → ECC (2004) → S/4HANA (2015)
- Core philosophy: Best practices vs. customization (80/20 rule)
- SAP modules: FI, CO, SD, MM, HR, PP, QM, PM, PS
- Integration: How all business functions connect in one system
- Deployment: On-premise vs. Cloud vs. Hybrid
- SAP Landscapes: DEV → QAS → PRD (Transport Management)
- Digital Transformation role of SAP
- Industry solutions: Retail, Banking, Manufacturing, Healthcare
- Licensing models and implementation methodologies (ASAP, Activate)

### 1.2 SAP in Accounting & Finance
- SAP FI (Financial Accounting) module overview
- General Ledger (GL) accounting: Chart of accounts, posting, reconciliation
- Accounts Payable (AP): Vendor invoices, payment runs, dunning
- Accounts Receivable (AR): Customer invoices, incoming payments, credit management
- Asset Accounting (AA): Acquisition, depreciation, retirement, transfers
- Bank Accounting: Electronic bank statements, reconciliation, cash management
- SAP CO (Controlling) module overview
- Cost Center Accounting: Planning, actual posting, assessments
- Profit Center Accounting: Revenue, costs, profitability by business unit
- Internal Orders: Tracking costs for specific projects/events
- Profitability Analysis (CO-PA): Market segment profitability
- FI-CO Integration: Real-time reconciliation through Universal Journal

### 1.3 SAP in Sales & Distribution (SD-FICO Integration)
- Order-to-Cash (O2C) complete process flow
- Sales order processing and revenue recognition
- Pricing procedures and condition technique
- Customer master data and credit management
- Delivery processing and goods issue (inventory impact)
- Billing and invoicing (FI document posting)
- SD-FI integration: Account determination
- Returns processing and credit/debit memos
- Sales information system and reporting
- Availability check and ATP (Available to Promise)

### 1.4 SAP in Procurement & Supply Chain (MM-FICO Integration)
- Procure-to-Pay (P2P) complete process flow
- Purchase requisition to purchase order
- Vendor master data and evaluation
- Goods receipt and inventory valuation (BSX, WRX accounts)
- Invoice verification (MIRO) and GR/IR clearing
- Physical inventory process
- Outline agreements: Contracts and scheduling agreements
- Material Requirement Planning (MRP) basics
- MM-FI integration: Automatic account determination
- Consignment and subcontracting processes

### 1.5 SAP in Human Resources (HCM-FICO Integration)
- SAP HCM module overview
- Organizational Management (OM): Structures, positions, jobs
- Personnel Administration (PA): Employee master data
- Time Management: Attendance, absences, quotas
- Payroll processing and posting to FI
- Recruitment and talent management
- Performance management and appraisals
- Employee Self-Service (ESS) and Manager Self-Service (MSS)
- SuccessFactors: SAP's cloud HR solution
- HCM-FI integration: Payroll accounting, cost allocation

================================================================================

## SECTION 2: FOR COMPUTER SCIENCE STUDENTS

### 2.1 SAP Technical Architecture
- Three-tier architecture: Presentation, Application, Database
- SAP NetWeaver platform components
- ABAP (Advanced Business Application Programming) overview
- SAP Fiori and UX architecture (SAPUI5, Gateway)
- Database concepts: HANA, Oracle, SQL Server
- Application server and work processes (DIA, BTC, SPO, etc.)
- System landscape and transport management (STMS)
- Web Dispatcher and message server
- RFC (Remote Function Call) and BAPI
- ABAP Workbench: SE80, SE11, SE38, SE24

### 2.2 ABAP Programming for FICO
- ABAP data types, variables, structures, internal tables
- Open SQL vs. Native SQL for FICO tables
- Modularization: Subroutines, Function Modules, Methods
- ABAP Object-Oriented Programming (classes, interfaces)
- Reports: Classical, ALV (ABAP List Viewer), Interactive
- Dialog Programming: Screens, Module Pool, Dynpros
- SmartForms and Adobe Forms for financial documents
- BDC (Batch Data Communication) for mass uploads
- BAPI for financial transactions
- Debugging and performance tuning (ST05, SAT)

### 2.3 SAP HANA & Advanced Technologies
- SAP HANA: In-memory database concept
- HANA architecture: Index server, Name server, Preprocessor
- HANA Studio vs. HANA Cockpit
- Native HANA development: Calculation views, CDS views
- SQL Script and stored procedures
- HANA Cloud Platform
- HANA XS (XSA) application development
- Data provisioning: SLT, BODS, SDI
- HANA data modeling and optimization
- Migration to S/4HANA: Technical considerations

### 2.4 SAP Integration Technologies
- SAP Process Integration (PI/PO) overview
- SAP Cloud Platform Integration (CPI)
- SAP API Management
- RFC, IDoc, and Web Services
- SAP OData services and Gateway (SEGW)
- Event-driven architecture in SAP
- SAP Integration Suite components
- SOA (Service-Oriented Architecture)
- Messaging protocols: SOAP, REST, AMQP
- Error handling and monitoring

### 2.5 SAP Development & Operations
- Software Development Lifecycle (SDLC) in SAP
- SAP Solution Manager functionalities
- Transport Management System (TMS)
- Change and Release Management
- DevOps and CI/CD in SAP (ChaRM, CTS+)
- SAP Cloud Platform and extension development
- AI and Machine Learning in SAP (Leonardo, AI Business Services)
- SAP Analytics Cloud (SAC) and embedded analytics
- Security: Authorization, Roles, Profiles (PFCG)
- Code quality, testing, automation (ABAP Test Cockpit)

================================================================================

## SECTION 3: FOR MBA FINANCE STUDENTS

### 3.1 SAP FICO for Finance Professionals
- Organizational structure: Client, Company Code, Business Area
- Chart of Accounts: Operational, Country-specific, Group
- Financial Statement Versions (FSV)
- Document types, posting keys, number ranges
- Cross-company code transactions
- Intercompany accounting and reconciliation
- Parallel accounting: Multiple GAAP (IFRS, Local, US GAAP)
- Foreign currency valuation and translation
- Closing operations: Month-end, quarter-end, year-end
- S/4HANA Finance innovations

### 3.2 Controlling & Managerial Accounting
- Overhead cost controlling
- Cost element accounting: Primary and secondary
- Activity-based costing (ABC)
- Product cost planning (CO-PC): Standard cost estimates
- Actual costing and Material Ledger
- Profitability Analysis (CO-PA): Account-based vs. Costing-based
- Profit Center Accounting and Transfer Pricing
- Variance analysis: Price, quantity, mix, rate
- Internal Orders and project cost controlling
- CO integration with FI, SD, MM, PP

### 3.3 SAP Treasury & Cash Management
- Treasury and Risk Management (TRM) overview
- Cash management and liquidity forecasting
- Bank account management (BAM)
- Electronic bank statement (EBS) processing
- Debt and investment management
- Risk management: FX, Interest Rate, Commodity
- Hedge management and hedge accounting
- In-house cash and payment factory
- Cash flow analysis and reporting
- Integration with FI, CO, SD, MM

### 3.4 SAP Financial Reporting & Analytics
- SAP Fiori Financial Applications
- SAP Analytics Cloud (SAC) integration
- Embedded analytics in S/4HANA Finance
- Financial drill-down reporting
- Management reporting and KPIs
- Balance Sheet and P&L analysis
- Cash Flow Statement generation
- Segment reporting (IFRS 8)
- Data extraction: SAP Query, Report Painter, Report Writer
- SAP BusinessObjects and BI integration

### 3.5 Finance Strategy & Governance
- Finance transformation using SAP
- Central Finance (CFIN): Concept and benefits
- Financial shared services design
- Compliance and internal controls (SOX)
- SAP GRC (Governance, Risk, Compliance)
- Audit Management and audit trails
- Finance process automation and RPA
- SAP in M&A (finance integration)
- Risk management and fraud detection
- Digital boardroom and CFO dashboard

================================================================================

## SECTION 4: FOR SAP ASPIRANTS/STUDENTS

### 4.1 SAP Learning Path & Certification
- Certification tracks: Associate, Professional, Specialist
- Associate vs. Professional certification differences
- SAP Learning Hub: Benefits and subscription
- OpenSAP: Free courses for beginners
- Choosing the right module for career goals
- Self-study resources: SAP Help, Community, Blogs
- Certification exam pattern (80 questions, 60% passing)
- Practice and demo systems access
- SAP Partners in training and certification
- Career paths after certification

### 4.2 Getting Started with SAP
- SAP GUI and logon process
- User navigation: Transaction codes, menus, favorites
- Creating and managing user profiles
- Working with reports and variants
- Printing and spool management
- Authorization and role concepts
- SAP documentation and help functions (F1, F4)
- Table browsing and data viewing (SE16, SE16N)
- Transport requests and change management
- Common T-Codes: F-02, FB03, FBL1N, FBL5N, FS10N, OB52

### 4.3 SAP Implementation & Project Lifecycle
- SAP Activate methodology (Discover, Prepare, Explore, Realize, Deploy, Run)
- ASAP methodology phases (legacy)
- Project preparation and team roles
- Business blueprint and requirement gathering
- Realization and configuration phase
- Testing: Unit, Integration, UAT
- Data migration strategies and tools (LTMC, Migration Cockpit)
- Go-live and cutover activities
- Hypercare and post-implementation support
- Agile vs. Waterfall in SAP projects

### 4.4 SAP Functional Modules Overview
- FI: Financial Accounting capabilities
- CO: Controlling capabilities
- SD: Sales and Distribution (Order-to-Cash)
- MM: Materials Management (Procure-to-Pay)
- PP: Production Planning
- QM: Quality Management
- PM: Plant Maintenance
- HR/HCM: Human Capital Management
- SCM: Supply Chain Management
- CRM: Customer Relationship Management

### 4.5 SAP Career Guidance
- Functional vs. Technical consultant roles and skills
- High-demand SAP modules
- Fresher vs. experienced entry points
- Building SAP skills: Internships, projects, freelancing
- Global vs. domestic market opportunities
- Remote SAP job opportunities
- Resume building for SAP roles
- SAP interviews: Common questions and preparation
- Salary expectations and growth trajectory
- Continuous learning in SAP ecosystem

================================================================================

## SECTION 5: FOR SAP PROFESSIONALS

### 5.1 SAP S/4HANA & Innovation
- S/4HANA architecture and innovations
- Simplification list: ECC to S/4HANA changes
- Universal Journal (ACDOCA) concept
- Embedded analytics and CDS views
- SAP Fiori: Design, development, deployment
- S/4HANA migration paths (Greenfield, Brownfield, Bluefield)
- Cloud vs. On-premise decision factors
- S/4HANA Private Cloud vs. Public Cloud
- Industry 4.0 and SAP IoT integration
- SAP roadmap and future releases

### 5.2 SAP Fiori & UX Excellence
- Fiori design principles and UX guidelines
- Fiori apps: Transactional, Analytical, Fact Sheet
- Fiori Launchpad and roles
- Fiori application types: SAPUI5, Web Dynpro, SAP GUI
- Fiori architecture: Gateway, Front-end server
- Fiori customization and extension
- SAP Screen Personas for legacy GUI
- Fiori implementation methodologies
- Performance optimization for Fiori apps
- User adoption and training best practices

### 5.3 SAP Advanced Technical Topics
- ABAP on HANA: Code pushdown and optimization
- CDS (Core Data Services) views development
- AMDP (ABAP Managed Database Procedures)
- OData services development and management
- SAP Cloud Application Programming Model (CAP)
- SAP Business Technology Platform (BTP)
- Integration with non-SAP systems
- SAP AI Business Services
- SAP Edge Services and Edge Computing
- Performance analysis and tuning tools

### 5.4 SAP Security & GRC
- Security concepts: Users, roles, profiles
- Authorization objects and checks
- SAP GRC overview
- Access Control (GRC AC) components
- Role design and Segregation of Duties (SoD)
- SAP Identity Management
- SAP Cloud Identity Services
- Secure coding practices in ABAP
- Vulnerability management
- Audit logging and security monitoring

### 5.5 SAP Data Management & Analytics
- SAP Data Warehouse Cloud
- SAP HANA as data platform
- Data archiving and ILM (Information Lifecycle Management)
- SAP Master Data Governance (MDG)
- SAP Analytics Cloud advanced topics
- Predictive analytics and machine learning
- SAP BusinessObjects reporting
- SAP Data Intelligence and orchestration
- Data migration: LTMC, Migration Cockpit, BODS
- Big data integration with SAP

### 5.6 SAP Migration & Conversion
- Migration paths: System Conversion, Landscape Transformation, New Implementation
- System Conversion approach (Brownfield)
- Landscape Transformation (Selective Data Migration)
- New Implementation (Greenfield)
- SAP Readiness Check
- Simplification List analysis
- Pre-migration activities and checks
- Migration Cockpit and LTMC
- Custom code handling during migration
- Post-migration testing and validation

### 5.7 SAP Operations & Support
- SAP Solution Manager 7.2 advanced features
- Focused Insights and Focused Build
- Application Lifecycle Management (ALM)
- System monitoring and alerting
- Job scheduling and background processing
- Performance analysis and tuning
- SAP EarlyWatch Alert and Managed Services
- Root cause analysis for production issues
- Service desk and incident management
- Change management and release cycles

================================================================================

## SECTION 6: END-TO-END BUSINESS PROCESSES

### 6.1 Order-to-Cash (O2C)
- Customer master creation
- Sales order processing
- Credit management
- Delivery and goods issue
- Billing and invoicing
- Incoming payment processing
- Dunning and collections
- Account reconciliation
- Integration points: SD-FI-CO
- Key T-Codes: VA01, VL01N, VF01, F-28, FBL5N

### 6.2 Procure-to-Pay (P2P)
- Vendor master creation
- Purchase requisition
- Purchase order
- Goods receipt
- Invoice verification (MIRO)
- GR/IR clearing
- Automatic payment run (F110)
- Vendor reconciliation
- Integration points: MM-FI-CO
- Key T-Codes: ME21N, MIGO, MIRO, F110, FBL1N

### 6.3 Record-to-Report (R2R)
- Transaction capture in sub-ledgers
- General Ledger posting
- Periodic closing activities
- Accruals and deferrals
- Foreign currency valuation
- Asset depreciation
- Financial statement generation
- Consolidation
- Integration: FI-CO-AA
- Key T-Codes: F-02, FAGLL03, F.13, AJAB, F.01

### 6.4 Asset Lifecycle Management
- Asset master creation
- Asset acquisition
- Asset under construction (AUC)
- Capitalization
- Depreciation run
- Asset transfer
- Asset retirement/scrapping
- Asset impairment
- Integration with FI
- Key T-Codes: AS01, ABZON, ABAA, ABAON, AJAB, ABAVN

### 6.5 Intercompany & Consolidation
- Intercompany sales/purchases
- Intercompany invoicing
- Intercompany reconciliation
- Intercompany elimination
- Group reporting consolidation
- Parallel accounting
- Currency translation
- Investment consolidation
- Segment reporting
- Key T-Codes: F.07, F.80, F.81, F.82, F.83

================================================================================

## SECTION 7: KEY CONFIGURATION TOPICS

### 7.1 Enterprise Structure
- Define Company
- Define Company Code
- Define Business Area
- Define Functional Area
- Define Profit Center
- Define Segment
- Assign Company Code to Company
- Assign Business Area to Company Code
- Fiscal Year Variant configuration
- Posting Period Variant (OB52)

### 7.2 General Ledger Configuration
- Chart of Accounts definition
- G/L Account creation (FS00)
- Account Groups
- Field Status Variants
- Document Types and Number Ranges
- Posting Keys
- Tolerance Groups
- Exchange Rate Types
- Financial Statement Version
- Key T-Codes: OBYC, OB13, OB52, FS00, OB53

### 7.3 Accounts Payable Configuration
- Vendor Account Groups
- Vendor Master (XK01/XK02)
- Payment Terms
- Payment Methods
- Automatic Payment Program (F110)
- Dunning Configuration
- Tax Configuration
- Withholding Tax
- Key T-Codes: XK01, FB60, F110, FBL1N, FK10N

### 7.4 Accounts Receivable Configuration
- Customer Account Groups
- Customer Master (XD01/XD02)
- Credit Management
- Dunning Configuration
- Payment Cards
- Special G/L Transactions
- Down Payment Configuration
- Key T-Codes: XD01, FB70, F-28, FBL5N, FD10N

### 7.5 Asset Accounting Configuration
- Chart of Depreciation
- Asset Classes
- Depreciation Areas
- Depreciation Keys
- Asset Number Ranges
- Screen Layout Rules
- Account Determination
- Key T-Codes: OAOA, AS01, AO90, AJAB, ABAON

### 7.6 Controlling Configuration
- Controlling Area
- Cost Element Categories
- Cost Center Standard Hierarchy
- Profit Center Standard Hierarchy
- Assessment Cycles
- Distribution Cycles
- Internal Order Types
- CO-PA Operating Concern
- Key T-Codes: OKKS, KA01, KS01, KE51, KSV1, KSU1

================================================================================

## SECTION 8: COMMON T-CODES REFERENCE

### Financial Accounting (FI)
- F-02: Post General Document
- FB03: Display Document
- FB50: Enter G/L Account Document
- FB60: Enter Incoming Invoice
- FB70: Enter Outgoing Invoice
- F-28: Post Incoming Payments
- F-53: Post Outgoing Payments
- F110: Automatic Payment Run
- FBIC01: Create Intercompany Document
- F.13: Clear G/L Accounts
- FAGLL03: G/L Line Items
- FS10N: G/L Account Balance
- FBL1N: Vendor Line Items
- FBL5N: Customer Line Items
- FK10N: Vendor Balance Display
- FD10N: Customer Balance Display

### Controlling (CO)
- KS01: Create Cost Center
- KS03: Display Cost Center
- KSB1: Cost Center Line Items
- KSH1: Create Cost Center Group
- KE51: Create Profit Center
- KE53: Display Profit Center
- KE5Z: Profit Center Line Items
- KSV1: Create Assessment Cycle
- KSU1: Create Distribution Cycle
- KKO1: Create Internal Order
- KO88: Settlement Internal Order
- KE24: Profitability Analysis Report

### Asset Accounting (AA)
- AS01: Create Asset Master
- AS03: Display Asset Master
- ABZON: Asset Acquisition
- ABAA: Unplanned Depreciation
- ABAON: Asset Retirement
- AJAB: Run Depreciation
- AB08: Display Asset Values
- S_ALR_87011963: Asset History Sheet

### General
- SE16/SE16N: Table Browser
- SE11: ABAP Dictionary
- SE80: Object Navigator
- SM37: Job Overview
- ST05: SQL Trace
- SAT: ABAP Runtime Analysis
- SU53: Authorization Check
- WE02: IDoc Display

================================================================================

## SECTION 9: MONTH-END CLOSING ACTIVITIES

### FI Closing
- Foreign Currency Valuation (F.05)
- GR/IR Clearing (F.13)
- Accruals and Deferrals
- Recurring Entries (F.14)
- Bank Reconciliation
- Intercompany Reconciliation
- Tax Returns Preparation
- Financial Statements (F.01)

### CO Closing
- Overhead Assessment/Distribution
- Activity Price Calculation (KP26, KPII)
- Work in Process Calculation (KKA0)
- Variance Calculation (KKS1)
- Settlement (KO88, CO88)
- Profitability Analysis Update
- Cost Center Reports
- Profit Center Reports

### AA Closing
- Depreciation Run (AJAB)
- Asset Reconciliation
- Asset Reports
- Year-End Closing (AJRW)

================================================================================

## SECTION 10: TROUBLESHOOTING & BEST PRACTICES

### Common Issues & Solutions
- Document posting errors: Check posting periods (OB52)
- Payment run failures: Check payment methods, house banks
- Reconciliation differences: Check sub-ledger vs. GL
- Currency valuation errors: Check exchange rates (OB08)
- Depreciation errors: Check asset classes, depreciation keys
- Authorization errors: Check roles (SU53, PFCG)

### Best Practices
- Regular backup of configuration
- Documentation of all changes
- Testing in QAS before PRD
- Regular user training
- Monitoring system performance
- Regular security reviews
- Following SAP notes and updates
- Using standard functionality before customization
- Regular data archiving
- Continuous improvement mindset

================================================================================
"""

# 10 Suggestion Prompts (Expanded)
SUGGESTIONS = [
    "What is Universal Journal (ACDOCA)?",
    "Order-to-Cash process flow?",
    "Procure-to-Pay process flow?",
    "Month-end closing activities in FICO?",
    "FI vs CO difference?",
    "S/4HANA migration paths?",
    "Asset Accounting configuration?",
    "Automatic Payment Program (F110)?",
    "Cost Center vs Profit Center?",
    "SAP FICO career paths?"
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
st.markdown('<h1 class="main-title">⚖️ SAP S/4HANA FICO Chatbot</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">70+ Topics | Powered by Qwen 2.5 72B | For Commerce, CS, MBA Finance & SAP Professionals</p>', unsafe_allow_html=True)

# Sidebar with Reset Button
with st.sidebar:
    st.markdown("### 🎯 Controls")
    if st.button("🔄 Reset Chat", use_container_width=True, key="reset_btn"):
        st.session_state.last_answer = ""
        st.session_state.reset_counter += 1
        st.rerun()
    st.info("🤖 Model: qwen-2.5-72b-instruct")
    st.success("📚 KB: 10 Sections, 70+ Topics")
    st.markdown("---")
    st.markdown("### 🎓 Target Audience:")
    st.markdown("- 📊 Commerce Students")
    st.markdown("- 💻 Computer Science Students")
    st.markdown("- 📈 MBA Finance Students")
    st.markdown("- 🚀 SAP Aspirants")
    st.markdown("- 👔 SAP Professionals")
    st.markdown("---")
    st.caption("📄 License: MIT | 🐙 GitHub + Streamlit Cloud")

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

# Query Input
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
        st.error("🔑 API Key 'OPENROUTER_API_KEY' not configured in Streamlit Cloud secrets!")
        st.info("Go to Settings → Secrets → Add OPENROUTER_API_KEY")
    else:
        with st.spinner("🔍 Consulting SAP Knowledge Base..."):
            try:
                headers = {
                    "Authorization": f"Bearer {API_KEY}",
                    "Content-Type": "application/json",
                    "HTTP-Referer": "https://github.com/amrithtech23-ux/sap-fico-chatbot",
                    "X-Title": "SAP S/4HANA FICO Chatbot"
                }
                
                system_prompt = f"""You are an expert SAP S/4HANA FICO consultant and educator.
Target: Commerce students, CS students, MBA Finance students, SAP aspirants and professionals.

Use this comprehensive knowledge base:
{KB}

Guidelines:
- Provide comprehensive, detailed answers (minimum 300 words)
- Use bullet points, numbered lists, and headings
- Reference specific topics from KB
- Include practical examples and T-Codes where relevant
- Explain concepts clearly for different audience levels
- If unsure, say 'Let me check SAP documentation'"""

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
                
            except requests.exceptions.Timeout:
                st.error("⏱️ Timeout: API request took too long. Please try again.")
            except requests.exceptions.HTTPError as e:
                if response.status_code == 401:
                    st.error("🔑 Authentication failed. Check your OpenRouter API key.")
                elif response.status_code == 429:
                    st.error("⚠️ Rate limit exceeded. Please wait and try again.")
                else:
                    st.error(f"❌ HTTP Error {response.status_code}: {str(e)}")
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")

# Display Result
if st.session_state.last_answer:
    st.markdown('<p class="section-header">📄 Result:</p>', unsafe_allow_html=True)
    st.markdown(f'<div class="result-box">{st.session_state.last_answer}</div>', unsafe_allow_html=True)
    st.caption("💡 **Tip:** Select and copy the answer above for your notes.")

# Footer
st.markdown("---")
st.caption("🎯 Target: Commerce | CS | MBA Finance | SAP Professionals | MIT License")
