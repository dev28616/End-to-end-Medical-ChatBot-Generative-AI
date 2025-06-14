from src.helper import load_pdf_file, text_split, download_hugging_face_embeddings
from pinecone.grpc import PineconeGRPC as Pineicone
from pinecone import ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv
import os

load_dotenv()

PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")
os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY

extracted_data = load_pdf_file(data= 'D:/STUDY/Projects/End-to-end-Medical-ChaatBot-Generative-AI/Data')
text_chunks = text_split(extracted_data)
embeddingds = download_hugging_face_embeddings()

pc = Pineicone(
    api_key="pcsk_41R8hB_H8Ce2i79MTyk62iCheSGxfh2u5hqbfhTZ8nqppaug6R5cB6i5TEsB7fdYaUHFo5"
)

index_name = "medicalbot"

pc.create_index(
    name=index_name,
    dimension=384,  # Dimension of the embeddings
    metric="cosine",  # Distance metric
    spec=ServerlessSpec(
        cloud="aws",
        region="us-east-1"
    )
)


docsearch = PineconeVectorStore.from_documents(
    documents=text_chunks,
    embedding=embeddingds,
    index_name=index_name
)