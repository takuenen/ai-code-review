# CodeSensei AI Code Review Tool (English)

Let AI help you identify code issues and improve code quality!  
Supports both Python and Java. Built using LangChain and Azure OpenAI.

---

## ✨ Features

* ✅ AI-powered code review suggestions (bilingual: Chinese & Japanese)
* ✅ Automatic comment generation
* ✅ Naming conventions and style checks (PEP8 / Java naming rules)
* ✅ Similar code recommendation (via RAG)
* ✅ Beginner learning mode (reference links + small exercises)

---

## 🚀 Quick Start Guide

### 1️⃣ Install Dependencies

Make sure you're using Python version **3.11 or higher**.

```bash
pip install -r requirements.txt
```

---

### 2️⃣ Configure `.env` File

Copy `.env.example` to `.env` and fill in the following fields:

```env
AZURE_OPENAI_API_KEY=Your API key
AZURE_OPENAI_ENDPOINT=https://xxx.openai.azure.com/
AZURE_OPENAI_DEPLOYMENT_CHAT=Deployment name
AZURE_OPENAI_DEPLOYMENT_EMBEDDING=Deployment name
AZURE_OPENAI_API_VERSION=2024-02-15-preview
```

---

### 3️⃣ Run the App

```bash
streamlit run main.py
```

Then open your browser and go to `http://localhost:8501` to start using the tool.

---

## 🗂️ Project Structure

```plaintext
code-review-app/
├── main.py              # Streamlit entry point
├── utils.py             # Utility functions
├── review.py            # AI review logic
├── comment_gen.py       # Comment generation logic
├── similar_code.py      # Similar code recommendation
├── vector_db.py         # Vector database management
├── requirements.txt     # Dependency list
├── README.md            # Project instructions
├── .env.example         # Environment variable sample
├── revision_embedder.py # Embedding script
└── style_check.py       # Style & naming rule checker
```

---

## 📚 References

* [LangChain Documentation](https://python.langchain.com/)
* [Azure OpenAI Documentation](https://learn.microsoft.com/azure/cognitive-services/openai/)
* [Streamlit Documentation](https://docs.streamlit.io/)

---

## 🙋 Author

Project lead: juanjuan.zhai
