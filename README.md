## 📊 MedBot – AI Medical Chatbot

![MedBot Banner](https://cdn.pixabay.com/photo/2017/06/08/01/06/medical-2389150_960_720.jpg)

**MedBot** is an AI-powered medical assistant built using [Streamlit](https://streamlit.io/), [Google Gemini](https://ai.google.dev/), and [LangChain](https://www.langchain.com/). Ask any health-related question and get responses grounded in medical knowledge.

---

### 🚀 Features

- 💬 ChatGPT-style real-time medical Q\&A
- 🧠 Powered by Google Gemini + LangChain
- 🔍 Contextual memory using Pinecone (optional)
- 🎨 Beautiful animated Streamlit UI
- 🐳 Dockerized for easy deployment

---

### 🗄️ Demo

> _“What are the symptoms of dengue?”_

![chatbot-demo](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbDZrbWYwbWttcTVkNzBkY3gyYTFjZnY4dTdrbDlwbHlwdzZzN3A3cCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/bGgsc5mWoryfgKBx1u/giphy.gif)

---

### 🧑‍💻 Tech Stack

- `streamlit` – Frontend
- `langchain` – Prompt handling
- `langchain-google-genai` – Gemini model
- `pinecone` (optional) – Vector retriever
- `docker` – Containerization

---

### 📦 Setup Instructions

#### Clone the repo

```bash
git clone https://github.com/dev28616/End-to-end-Medical-ChatBot-Generative-AI.git
cd medbot-ai
```

#### Install dependencies (Python 3.10+)

```bash
pip install -r requirements.txt
```

#### Set environment variables

Create a `.env` file or use Streamlit Cloud secrets:

```env
PINECONE_API_KEY=your-pinecone-key
GEMINI_API_KEY=your-gemini-key
```

#### Run locally

```bash
streamlit run main.py
```

---

### 🐳 Docker Setup

#### Build & run with Docker

```bash
docker build -t medbot-app .
docker run -p 8501:8501 medbot-app
```

---

### 🔐 Deployment (Streamlit Cloud)

1. Push to GitHub
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)
3. Link your repo & add secrets
4. Click **Deploy**

---

### 📁 Project Structure

```
🔹 main.py
🔹 Dockerfile
🔹 requirements.txt
🔹 .dockerignore
🔹 src/
├── prompt.py
└── helper.py
```
