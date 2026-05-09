# 🧠 UX Research Agent

A multi-agent AI pipeline that automatically analyzes user feedback and generates structured UX reports.

## How it works
- 🕵️ **Agent 1 — Analyst**: Identifies recurring problems in user verbatims
- 📊 **Agent 2 — Categorizer**: Classifies issues by theme (navigation, performance, design, support)
- ✍️ **Agent 3 — Writer**: Generates a structured UX report with actionable recommendations

## Features
- 🤖 Multi-agent autonomous task delegation
- ⚡ Powered by Llama 3.1 via Groq API
- 🎨 Clean web interface with Streamlit

## Tech Stack
- Python
- Groq API (Llama 3.1)
- Streamlit

## Setup
1. Clone the repo
2. Install dependencies: `pip install -r requirements.txt`
3. Create a `.env` file with your Groq API key
4. Run: `streamlit run app.py`
