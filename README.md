# Docuchat Gemini Chatbot

A Streamlit-based chatbot that can answer questions from uploaded PDF, DOCX, or TXT documents using **Google Gemini API**.

## Features

- Upload any document and ask unlimited questions.
- Chat-like interface similar to ChatGPT.
- Stores chat history in session.
- Uses `.env` for secure API key storage.

## Setup

1. Clone the repo:

```bash
git clone git@github.com:kunj2803/Docuchat-Chatbot.git
cd docuchat-gemini
```

2. Install dependencies:

```pip install -r requirements.txt```


3. Create a .env file with your Gemini API key:

```GEMINI_API_KEY=your_gemini_api_key_here```


4. Run the app:

```streamlit run chatbot.py```
