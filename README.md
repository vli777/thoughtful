# Thoughtful AI Support Agent

A simple AI-powered customer support chatbot built with **Streamlit** and **OpenAI**, designed to answer common questions about Thoughtful AI using a predefined knowledge base, with GPT-4 fallback for anything else.

---

## Features

- Hardcoded responses for Thoughtful AI FAQs (from `kb.json`)
- Semantic classifier to match user queries to known questions
- gpt-o4-mini fallback for unknown questions
- Web-based UI using Streamlit
- Environment-based API key management

---

## Setup Instructions

### 1. Clone the Repository

```
git clone https://github.com/vli777/thoughtful-support-agent.git
cd thoughtful-support-agent
```

### 2. Create & Activate Venv

```
python -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows
.venv\Scripts\activate
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

### 4. Add OpenAI API Key

```
Required:
    OPENAI_API_KEY=your-api-key-here
    
Optional:
    OPENAI_MODEL=gpt-4o-mini
    KB_PATH=data/kb.json
```

### 5. Run the App

```
streamlit run app/main.py
```
