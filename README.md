# Docuchat Gemini Chatbot

A Streamlit-based chatbot that can answer questions from uploaded PDF, DOCX, or TXT documents using **Google Gemini API**.

## Features

- Upload any document and ask unlimited questions.
- Chat-like interface similar to ChatGPT.
- Stores chat history in session.
- Uses `.env` for secure API key storage.

## Demo

- Live demo (if deployed on Streamlit Cloud): [Demo Link](#)
- Example screenshot:

![Chatbot Screenshot](assets/screenshot.png)

> Replace the link and screenshot with your actual demo and image.

## Setup

1. Clone the repo:

```bash
git clone git@github.com:kunj2803/Docuchat-Chatbot.git
cd docuchat-gemini

2. Install dependencies:

```bash
pip install -r requirements.txt

3. Create a `.env` file with your Gemini API key:

```dotenv
GEMINI_API_KEY=your_gemini_api_key_here

4. Run the app:

```bash
streamlit run chatbot.py

