# **City Paint Chatbot with Gemini**

#### Link: https://paint-chatbot-gemini.streamlit.app/
---

## **Project structure**
- `main.py`: main Streamlit python script for the Chatbot
- `response_handler.py`: processes user input, generates AI responses using Gemini, manages conversation context, and triggers paint estimation
- `.env`: contains Google API Key
- `config.py`: loads .env, configures API key and initilizes the model
- `conversation.py`: manages recent chat history (last 5 messages) for context retention
- `paint_estimator`: calculates required paint buckets based on user inputs
- `requirements.txt`: a list of all packages required to run the project
- `README.md`: markdown file
<br>

## **Set up and Installation**
1. Install Git: If Git is not already installed on your system, download and install it from [Git's official website](https://git-scm.com/). Follow the installation instructions for your operating system.
  
2. Clone the repository:
- Open a terminal or command prompt and navigate to the directory where you want to download the project.
- Type the following command to clone the repository from GitHub

```
git clone https://github.com/phuonganh-38/chatbot-gemini.git
cd chatbot-gemini
```

3. Add your Google API Key:

In the downnloaded folder, add a new file called `.env`.
In `.env`:
```
GOOGLE_API_KEY=your_api_key_here
```

4. Start the streamlit app by running:
```
streamlit run main.py
```
<br>
