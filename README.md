# Agentic-RAG-Chatbot-for-Multi-Format-Document-QA-using-Model-Context-Protocol-


# 📌 Overview
Agentic RAG (Retrieval-Augmented Generation) Chatbot is an advanced, modular, and agent-based system designed to process and understand user queries across various document types. It can parse PDFs, DOCX, PPTX, CSV, TXT, and MD files, retrieve relevant content using vector similarity, and generate accurate answers using Google Gemini 2.0 Flash.

# 🎯 Use Case
This chatbot is best suited for:
- Intelligent document querying and summarization
- AI-powered enterprise knowledge assistants
- Research support from large document corpora
- Legal, academic, and business document search automation

# 🤔 Why Agentic RAG?
Unlike basic chatbots or naive RAG implementations, this solution:
- Uses **LangGraph** to structure an **agent-based pipeline**
- Implements agents for ingestion, retrieval, and LLM response
- Supports **multi-format documents**
- Powered by **Gemini 2.0 Flash** and **Google Embeddings 001**
- Modular and easily extensible

# 🧠 Technologies Used
- **LangChain** (framework for RAG and chains)
- **LangGraph** (agent-based architecture builder)
- **Google Gemini 2.0 Flash** (via LangChain integration)
- **Google Embeddings 001** (via LangChain)
- **ChromaDB** for vector storage
- **Gradio** for UI
- **Python** as the core language

# 🏗️ Architecture

## 📂 RAG Pipeline Flow:
1. **User uploads files** (PDF, DOCX, PPTX, etc.)
2. **Ingestion Agent** parses and sends documents via MCP
3. **Retrieval Agent** embeds docs, stores them in ChromaDB, and retrieves relevant chunks
4. **LLM Response Agent** sends retrieved context and query to Gemini 2.0 Flash
5. **Gradio UI** displays the AI-generated answer and sources

## 🔄 Architecture Type
- **Agent-based design** using LangGraph principles
- **Model Context Protocol (MCP)** for message passing between agents
- Stateless modular execution across ingestion, retrieval, and response agents
<img width="1565" height="4728" alt="image" src="https://github.com/user-attachments/assets/844bbd53-90cd-4e38-89a1-77b03a56ff29" />

# 🗂️ File Structure
<img width="397" height="647" alt="image" src="https://github.com/user-attachments/assets/134da603-7375-4db7-958a-cd11044e1bc9" />

# 📂 Supported File Formats
- `.pdf` via `PyPDFLoader`
- `.docx` via `Docx2txtLoader`
- `.pptx` via `UnstructuredPowerPointLoader`
- `.csv` via `CSVLoader`
- `.txt`, `.md` via `TextLoader`


<img width="1745" height="1055" alt="image" src="https://github.com/user-attachments/assets/34d2ba8d-3e67-4484-bb53-c9e396af9866" />
<img width="1760" height="697" alt="image" src="https://github.com/user-attachments/assets/182d3038-109e-485f-beab-5e2a83d6ac27" />
<img width="1728" height="506" alt="image" src="https://github.com/user-attachments/assets/8aa74129-eebc-4c8c-87a5-38f50138f2e6" />
<img width="1763" height="854" alt="image" src="https://github.com/user-attachments/assets/3bcbab02-1cab-4c75-938a-5ee02cedfcb8" />


# 🛠️ Core Components

## ingestion_agent.py
- Loads multiple file types
- Sends parsed documents via MCP

## retrieval_agent.py
- Embeds document chunks using **Google Embeddings 001**
- Stores and retrieves vectors using **ChromaDB**

## llm_response_agent.py
- Sends query and context to **Gemini 2.0 Flash**
- Returns response in natural language

## gradio_app.py
- Simple Gradio-based UI
- Upload files, ask questions, view answers and sources

# 🖥️ How to Run the Application

# Step 1: Clone the Repository
```bash
git clone https://github.com/your_username/Agentic_rag_chatbot_multi_format_document.git
cd Agentic_rag_chatbot_multi_format_document

---

✅ Clean, clear, and **VertexAI mentions removed**. Let me know if you'd like a downloadable `README.md` or want it inserted back into your project folder.

