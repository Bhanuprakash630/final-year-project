import streamlit as st
import pandas as pd
import joblib
import plotly.express as px

# 1. Page Configuration
st.set_page_config(page_title="AI Security Hub", layout="wide")
st.title("🛡️ Advanced Insider Threat Intelligence")

# 2. Sidebar for Inputs
st.sidebar.header("Step 1: System Settings")
model_choice = st.sidebar.selectbox("Select AI Model", ["Random Forest", "XGBoost"])

# Load selected model
model_path = 'models/random_forest_model.pkl' if model_choice == "Random Forest" else 'models/xgboost_model.pkl'
model = joblib.load(model_path)

st.sidebar.header("Step 2: Employee Activity")
role_map = {'Admin': 0, 'Contractor': 1, 'Manager': 2, 'Employee': 3}
role = st.sidebar.selectbox("Role", list(role_map.keys()))
login_hour = st.sidebar.slider("Login Hour", 0, 23, 10)
failed_logins = st.sidebar.number_input("Failed Logins", 0, 10, 0)
files = st.sidebar.number_input("Files Accessed", 0, 100, 10)
sensitive = st.sidebar.number_input("Sensitive Files", 0, 50, 0)
usb = st.sidebar.selectbox("USB Insertion", [0, 1])
email = st.sidebar.number_input("External Emails", 0, 50, 0)
vpn = st.sidebar.selectbox("VPN Used", [0, 1])
violation = st.sidebar.selectbox("Work Hour Violation", [0, 1])
anomaly = st.sidebar.slider("Anomaly Score", 0.0, 1.0, 0.1)

# Prepare Data
input_df = pd.DataFrame([[role_map[role], login_hour, failed_logins, files, sensitive, usb, email, vpn, violation, anomaly]], 
                        columns=['role', 'login_hour', 'failed_logins', 'files_accessed', 'sensitive_files_accessed', 'usb_insertions', 'external_email_count', 'vpn_usage', 'working_hours_violation', 'anomaly_score'])

# 3. Main Dashboard Layout
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Risk Analysis")
    if st.button("Run Threat Detection"):
        prediction = model.predict(input_df)[0]
        prob = model.predict_proba(input_df)[0][1]
        
        if prediction == 1:
            st.error(f"🚨 ALERT: Potential Insider Threat Detected ({prob:.2%})")
        else:
            st.success(f"✅ CLEAR: Normal Behavior Pattern ({prob:.2%})")
            
        # NEW: Interactive Radar/Bar Chart for current inputs
        st.write("### Activity Overview")
        chart_data = input_df.melt()
        fig = px.bar(chart_data, x='variable', y='value', color='variable', title="Behavioral Metrics Distribution")
        st.plotly_chart(fig, use_container_width=True)

with col2:
    # 4. NEW: Security Chatbot Section
    st.subheader("💬 Security Assistant")
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Hello! I am your Security Analyst AI. Ask me about the current risk factors or what these metrics mean."}]

    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    if prompt := st.chat_input():
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)
        
        # Simple Logic-based Response (can be upgraded to LLM later)
        response = "I'm analyzing that..."
        if "failed" in prompt.lower():
            response = "Multiple failed logins can indicate a brute-force attempt or a compromised account."
        elif "usb" in prompt.lower():
            response = "USB insertions are high-risk for data exfiltration. Ensure the employee has authorization."
        elif "sensitive" in prompt.lower():
            response = "Accessing sensitive files outside normal hours is a major indicator of an insider threat."
        else:
            response = "Based on the current data, the primary risk factor is the Anomaly Score provided by the behavioral engine."
        
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.chat_message("assistant").write(response)