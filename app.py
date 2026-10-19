import streamlit as st
from analyzer import analyze_logs

st.set_page_config(
    page_title="Cybersecurity Log Analyst",
    page_icon="🔐",
    layout="wide"
)

st.title("🔐 Cybersecurity Log Analyst")

st.write(
    "Paste server or security logs below and the AI will identify "
    "suspicious activity, explain the risk, and recommend investigation steps."
)

logs = st.text_area(
    "Security Logs",
    height=350,
    placeholder="Paste security logs here..."
)

analyze_button = st.button(
    "Analyze Logs",
    type="primary",
    use_container_width=True
)

if analyze_button:

    if not logs.strip():
        st.warning("Please paste some security logs first.")

    else:
        with st.spinner("Analyzing logs..."):

            try:
                result = analyze_logs(logs)

                st.subheader("Risk Report")
                st.markdown(result)

            except Exception as e:
                st.error(f"Analysis failed: {e}")