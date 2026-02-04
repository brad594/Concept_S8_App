import streamlit as st
import requests
import google.generativeai as genai

# 1. SETUP INTERFACE
st.set_page_config(page_title="Concept Electrical", page_icon="⚡")
st.title("⚡ Concept Job Finder")

# 2. LOAD SECRETS (From Streamlit Dashboard)
try:
    S8_API_KEY = st.secrets["S8_API_KEY"]
    GEMINI_KEY = st.secrets["GEMINI_KEY"]
except:
    st.error("Missing API Keys! Please add them to the Streamlit Secrets dashboard.")
    st.stop()

# 3. TOOLS
def search_job(query: str):
    url = "https://api.servicem8.com/api_1.0/search.json"
    headers = {"X-Api-Key": S8_API_KEY}
    r = requests.get(url, headers=headers, params={'q': query})
    return r.json()

def get_job_info(job_uuid: str):
    url = f"https://api.servicem8.com/api_1.0/job/{job_uuid}.json"
    headers = {"X-Api-Key": S8_API_KEY}
    r = requests.get(url, headers=headers)
    return r.json()

# 4. AI CONFIG
genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel(
    model_name='gemini-2.0-flash', 
    tools=[search_job, get_job_info]
)

# 5. CHAT LOGIC (With Safety Switch)
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(enable_automatic_function_calling=True)

user_input = st.text_input("Ask about an address or job:", placeholder="e.g. Status of 3 Bullock Ct?")

if user_input:
    with st.spinner('Checking ServiceM8...'):
        try:
            response = st.session_state.chat.send_message(user_input)
            st.markdown(response.text)
        except Exception as e:
            if "429" in str(e) or "ResourceExhausted" in str(e):
                st.error("🚦 **Rate Limit Hit:** The AI is cooling down. Please wait 60 seconds and try again.")
            else:
                st.error(f"⚠️ **Connection Error:** {str(e)}")
