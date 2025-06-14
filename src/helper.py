from langchain.document_loaders import PyMuPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings

def load_pdf_file(data):
    loader = DirectoryLoader(data, glob="*.pdf", loader_cls=PyMuPDFLoader)
    documents = loader.load()
    return documents

# Split the documents into Text chunks
def text_split(extracted_data):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=20
    )
    text_chunks = text_splitter.split_documents(extracted_data)
    return text_chunks

#Download the Embedding s from Hugging Face
from langchain.embeddings import HuggingFaceEmbeddings
def download_hugging_face_embeddings():
    embedding = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
        )
    return embedding

