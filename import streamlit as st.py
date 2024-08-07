import streamlit as st
import  os
from llama_index.llms.groq import Groq
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.core import PromptTemplate, Settings
from llama_index.core.embeddings import resolve_embed_model
from llama_index.vector_stores.pinecone import PineconeVectorStore
from llama_index.core import StorageContext
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
 
 
# Pinecone connection (replace with your details)
api_key = 'e994c77d-9e98-48b1-9415-1bb557bdc275'
index_name = "llamas"
 
def init_pinecone():
  try:
    from pinecone.grpc import PineconeGRPC as Pinecone
    from pinecone import ServerlessSpec
    pc = Pinecone(api_key=api_key)
    if index_name not in pc.list_indexes().names():
      pc.create_index(
          name=index_name,
          dimension=384,
          metric="cosine",
          spec=ServerlessSpec(
              cloud='aws',
              region='us-east-1'
          )
      )
      print("Index created")
    else:
      print("Index already exists")
    return PineconeVectorStore(pinecone_index=pc.Index(index_name))
  except:
    st.error("Error connecting to Pinecone. Please check your API key and network connection.")
    return None
 
def llama_index_groq(query):
  # Load documents (cached within the function)
  if not hasattr(llama_index_groq, 'documents'):
    required_exts = [".pdf"]
    loader = SimpleDirectoryReader("data", required_exts=required_exts)
    llama_index_groq.documents = loader.load_data()
 
  # Prompt template
  template = (
      "We have provided context information below. \n"
      "---------------------\n"
      "{context_str}"
      "\n---------------------\n"
      "Given this information, please answer the question: {query_str}\n"
      "If you don't know the answer, please do mention : I don't know !"
  )
 
  # Initialize LLM and embedding model (cached within the function)
  if not hasattr(llama_index_groq, 'llm'):
    llm = Groq(model="llama3-70b-8192", api_key="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")
    Settings.llm = llm
    Settings.num_output = 400
    embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
    Settings.embed_model = embed_model
  # Pinecone connection (use the cached vector store if available)
  vector_store = getattr(llama_index_groq, 'vector_store', init_pinecone())
  if not vector_store:
    return None
 
  storage_context = StorageContext.from_defaults(vector_store=vector_store)
  index = VectorStoreIndex.from_documents(
      llama_index_groq.documents, storage_context=storage_context
  )
  query_engine = index.as_query_engine(similarity_top_k=3)
  response = query_engine.query(query)
  return response
 
st.title("Llama Index Groq Search")
 
# Text area for user query
user_query = st.text_area("Enter your question here:", height=100)
 
# Submit button to trigger search
if st.button("Search"):
  # Call the function and display the response
  response = llama_index_groq(user_query)
  if response:
    st.write("**Answer:**")
    st.write(response.response)
  else:
    st.write("An error occurred during the search. Please try again later.")