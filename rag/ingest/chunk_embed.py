from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.docstore.document import Document
import json, os

# Load parsed trials
with open("data/parsed_trials.json", "r", encoding="utf-8") as f:
    trials = json.load(f)

# Chunking strategy
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)

# Format and split
documents = []
for trial in trials:
    for chunk_text, metadata in format_trial_chunks(trial):
        for chunk in splitter.split_text(chunk_text):
            documents.append(Document(page_content=chunk, metadata=metadata))

print(f"✅ Prepared {len(documents)} chunks.")

# Embed and store
embedding_model = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(documents, embedding_model)
os.makedirs("vectorstore/faiss_index", exist_ok=True)
vectorstore.save_local("vectorstore/faiss_index")

print("✅ FAISS index saved.")