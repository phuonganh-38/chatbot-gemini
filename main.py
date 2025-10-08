import streamlit as st
from response_handle import get_response

# --- Streamlit page setup ---
st.set_page_config(
  page_title="City Paint Estimator",
  page_icon='🏗️',
  layout="centered"
)

st.title("City Paint Estimator with Gemini")
st.caption("Your smart assistant to estimate how many paint buckets are needed for the entire city.")

# Initialize chat history
if "messages" not in st.session_state:
  st.session_state.messages = []

# Display chat history
for role, msg in st.session_state.messages:
  with st.chat_message(role):
    st.markdown(msg)

# User input
if prompt := st.chat_input("Ask anything"):
  # Append user message
  st.session_state.messages.append(("user", prompt))
  with st.chat_message("user"):
    st.markdown(prompt)

  # Get response from chatbot
  response = get_response(prompt)
  st.session_state.messages.append(("assistant", response))

  with st.chat_message("assistant"):
    st.markdown(response)