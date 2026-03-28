import streamlit as st
import requests
import os

st.set_page_config(page_title="SAP FICO Test", page_icon="✅")
st.title("✅ SAP FICO Chatbot - Test")

st.success("🎉 Streamlit is working!")

API_KEY = os.environ.get("OPENROUTER_API_KEY")

if API_KEY:
    st.success(f"✅ API Key configured: {API_KEY[:15]}...")
else:
    st.error("❌ API Key NOT found in Secrets!")
    st.info("Go to Settings → Secrets → Add OPENROUTER_API_KEY")

st.markdown("---")
st.write("This is a test page. If you see this, deployment is successful!")

query = st.text_area("Test Question:", height=80, placeholder="Type something...")

if st.button("Submit"):
    if query:
        st.success(f"✅ You asked: {query}")
        st.info("Full chatbot will be enabled after testing!")
