import gradio as gr
import tempfile
import shutil
import asyncio
import logging
import os

from agents.ingestion_agent import ingest_documents
from graph.rag_graph import build_rag_graph

logging.basicConfig(level=logging.DEBUG)

async def async_rag_chat(file, query):
    logging.debug("📥 Received file(s) and query")
    temp_dir = tempfile.mkdtemp()

    file_paths = []
    for f in file:
        filename = os.path.basename(f.name)
        temp_path = os.path.join(temp_dir, filename)
        shutil.copy(f.name, temp_path)
        file_paths.append(temp_path)
        logging.debug(f"📄 File copied to: {temp_path}")

    logging.debug("⚙️ Ingesting documents...")
    mcp_msg = ingest_documents(file_paths)

    logging.debug("📚 Building RAG graph...")
    rag_graph = build_rag_graph(mcp_msg["payload"]["vectorstore"], query)

    logging.debug("🤖 Running graph.invoke()...")
    final_msg = rag_graph.invoke(mcp_msg)

    answer = final_msg["payload"]["answer"]
    logging.debug(f"✅ Final Answer: {answer}")
    return answer

def rag_chat_sync(file, query):
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

    try:
        return loop.run_until_complete(async_rag_chat(file, query))
    except Exception as e:
        logging.exception("❌ Exception in async handler")
        return f"Error: {str(e)}"

def launch_ui():
    with gr.Blocks(title="📄 Agentic RAG Chatbot for Multi-Format Document ") as demo:
        gr.Markdown("## 📄 Agentic RAG Chatbot for Multi-Format Document ")

        with gr.Row():
            file_input = gr.File(
                label="Upload Documents",
                file_types=[".pdf", ".txt", ".csv", ".docx"],
                file_count="multiple"
            )
            query_input = gr.Textbox(
                label="Enter your question here",
                placeholder="Ask something from your documents"
            )

        submit_btn = gr.Button("Get Answer")
        output_box = gr.Textbox(label="Answer")  # always visible for older Gradio

        def wrapper(file, query):
            return rag_chat_sync(file, query)

        submit_btn.click(fn=wrapper, inputs=[file_input, query_input], outputs=[output_box])

    print("✅ UI components built, launching Gradio...")
    demo.launch()

