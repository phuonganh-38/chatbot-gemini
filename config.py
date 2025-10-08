import os
from dotenv import load_dotenv
import streamlit as st
import google.generativeai as gen_ai

# --- Load environment variables ---
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# --- Initialize model ---
if not GOOGLE_API_KEY:
  st.error("Missing API Key. Please set API key in your environment.")
else:
  gen_ai.configure(api_key=GOOGLE_API_KEY)
  model=gen_ai.GenerativeModel("gemini-2.0-flash")