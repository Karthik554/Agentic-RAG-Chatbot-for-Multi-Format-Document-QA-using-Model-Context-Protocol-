# 🤖 Agentic RAG Chatbot for Multi-Format Documents

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

# 🗂️ File Structure

<img width="358" height="642" alt="image" src="https://github.com/user-attachments/assets/feff9a02-3c42-41c7-80dc-401d85ad72d6" />

# 📂 Supported File Formats
- `.pdf` via `PyPDFLoader`
- `.docx` via `Docx2txtLoader`
- `.pptx` via `UnstructuredPowerPointLoader`
- `.csv` via `CSVLoader`
- `.txt`, `.md` via `TextLoader`

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

<img width="1565" height="4728" alt="image" src="https://github.com/user-attachments/assets/88593237-1fbe-4bef-aecc-0a2602daf1f4" />
<img width="1848" height="1041" alt="image" src="https://github.com/user-attachments/assets/1b583829-2f8b-402c-9d33-9686e8d31a69" />
<img width="1740" height="766" alt="image" src="https://github.com/user-attachments/assets/9f3f37ff-1046-4d0c-9739-433c4454dc86" />
<img width="1758" height="782" alt="image" src="https://github.com/user-attachments/assets/a6d7331f-bc28-42f0-9d50-33f01ee5f533" />
<img width="1798" height="629" alt="image" src="https://github.com/user-attachments/assets/24d4d1e9-c5dc-4b92-a7b9-3ff7d80efb3a" />
<img width="1729" height="580" alt="image" src="https://github.com/user-attachments/assets/20a3dabc-d5fc-41bd-8dfe-1cf7b406e2d4" />

## Project Code ZIP FIlE LINK: https://drive.google.com/file/d/1qu5_n-vRADMfUZI1xI1eYicsbeGLG53K/view?usp=sharing
# 🖥️ How to Run the Application

# Step 1: Clone the Repository
```bash
git clone https://github.com/your_username/Agentic_rag_chatbot_multi_format_document.git
cd Agentic_rag_chatbot_multi_format_document
