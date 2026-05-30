from pinecone import Pinecone
from dotenv import load_dotenv
import os
# Load .env file
load_dotenv()

# Get API key from .env
api_key = os.getenv("PINECONE_API_KEY")

# Initialize Pinecone
pc = Pinecone(api_key=api_key)

index_name = "textembedding"
index = pc.Index(index_name)
