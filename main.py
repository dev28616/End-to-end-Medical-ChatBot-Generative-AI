import os
import time
import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain_core.prompts import ChatPromptTemplate
from src.prompt import system_prompt

# ======================
# 🔐 Load environment
# ======================
load_dotenv()
<<<<<<< HEAD
os.environ["PINECONE_API_KEY"] = os.getenv("PINECONE_API_KEY")
os.environ["GOOGLE_API_KEY"] = os.getenv("GEMINI_API_KEY")
=======
os.environ["PINECONE_API_KEY"] = st.secrets["PINECONE_API_KEY"]
os.environ["GOOGLE_API_KEY"] = st.secrets["GEMINI_API_KEY"]
>>>>>>> 7f3566545d2d6284dd7bb07e675ecb0e082149ee

# ======================
# 📦 Setup embeddings & retrievers
# ======================
embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

docsearch = PineconeVectorStore.from_existing_index(
    embedding=embedding,
    index_name="medicalbot"
)
retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k": 3})

# ======================
# 🤖 Setup Gemini LLM
# ======================
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash-latest",
    temperature=0.4,
    max_output_tokens=500
)

prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "{input}")
])

stuff_chain = create_stuff_documents_chain(llm=llm, prompt=prompt)
rag_chain = create_retrieval_chain(retriever=retriever, combine_docs_chain=stuff_chain)

# ======================
# 🎨 Streamlit UI Setup
# ======================
st.set_page_config(page_title="MedBot", page_icon="🩺", layout="centered")

st.markdown("""
<style>
    .block-container {
        padding-top: 2rem;
    }
    .stChatMessage {
        padding: 1rem;
        border-radius: 12px;
        margin: 0.5rem 0;
    }
    .stChatMessage.user {
        background-color: #d1e7dd;
        color: #0f5132;
        align-self: flex-start;
    }
    .stChatMessage.bot {
        background-color: #e2e3e5;
        color: #212529;
        align-self: flex-end;
    }
    .stTextInput>div>div>input {
        font-size: 1.1rem;
        height: 50px;
    }
</style>
""", unsafe_allow_html=True)

st.title("🩺 MedBot - Your Medical AI Assistant")
st.markdown("💬 _Ask about symptoms, conditions, or general health info. MedBot responds based on verified medical knowledge._")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ✅ Input and live response typing
if user_input := st.chat_input("Type your question..."):
    st.session_state.chat_history.append(("user", user_input))
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("bot"):
        placeholder = st.empty()
        placeholder.markdown("🧠 _Thinking..._")

        try:
            result = rag_chain.invoke({"input": user_input})
            response = result["answer"]
        except Exception as e:
            response = f"❌ Error: {str(e)}"

        # Simulate typing
        bot_text = ""
        for char in response:
            bot_text += char
            placeholder.markdown(bot_text + "▌")
            time.sleep(0.01)
        placeholder.markdown(bot_text)

    st.session_state.chat_history.append(("bot", response))

# Display chat history
for role, message in st.session_state.chat_history:
    with st.chat_message(role):
        st.markdown(message)

st.warning("⚠️ MedBot is an AI assistant. Always consult a licensed medical professional for diagnosis or treatment.")

st.markdown("---")

# 💬 Chat Utilities: Clear & Save
col1, col2 = st.columns([1, 1])

with col1:
    if st.button("🧹 Clear Chat"):
        st.session_state.chat_history = []
        st.rerun()

with col2:
    if st.button("💾 Save Chat"):
        chat_log = ""
        for role, msg in st.session_state.chat_history:
            prefix = "You" if role == "user" else "MedBot"
            chat_log += f"{prefix}: {msg}\n\n"

        st.download_button(
            label="📥 Export Chat History",
            data=chat_log,
            file_name="medbot_chat_history.txt",
            mime="text/plain"
        )

st.markdown("""
---  
💻 Developed by Debojyoti Mondal.
""", unsafe_allow_html=True)
