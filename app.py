
**Conclusion:**

The Universal Journal (ACDOCA) is the **foundation of SAP S/4HANA Finance** and represents a **revolutionary simplification** of financial data management. It eliminates the complexity of traditional ERP systems by providing:

✅ **Single source of truth** - No reconciliation
✅ **Real-time processing** - Instant reporting
✅ **Simplified architecture** - 1 table vs 500+
✅ **Multi-dimensional reporting** - Unlimited analysis
✅ **Parallel accounting** - Multiple principles simultaneously
✅ **Faster closing** - 70-80% time reduction
✅ **Better performance** - 10-100x faster
✅ **Lower TCO** - Reduced storage and maintenance

This is the **single most important innovation** in SAP S/4HANA Finance and the key differentiator from traditional ERP systems.

---

[Continue with detailed content for remaining topics...]
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
                
                system_prompt = f"""You are an expert SAP S/4HANA FICO consultant and educator.
Target: Commerce students, CS students, MBA Finance, SAP aspirants, professionals.

Use this knowledge base for accurate answers:
{KB}

Guidelines:
- Provide COMPREHENSIVE, detailed answers
- Use bullet points, numbered lists, and examples
- Reference specific topics from KB
- Explain concepts clearly for different audiences
- If unsure, say 'Let me check SAP documentation'"""

                payload = {
                    "model": MODEL,
                    "messages": [
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_query}
                    ],
                    "max_tokens": 1500,  # Increased for complete answers
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
