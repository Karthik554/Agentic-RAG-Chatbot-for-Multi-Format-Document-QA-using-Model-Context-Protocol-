from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from posthog import api_key

from utils.mcp_protocol import MCPMessage

load_dotenv()
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash",api_key='AIzaSyBgjqBguV8UHA0LJFc-CdPNIUu_Fg-EH74')

def generate_response(message: MCPMessage) -> MCPMessage:
    query = message["payload"]["query"]
    context = message["payload"]["context"]

    prompt = f"""Answer the following question using the provided context, by assuming you are the expert in that field where the users asks about details from the document via a query.\n\nQuestion: {query}\n\nContext:\n{context}"""
    response = llm.invoke(prompt)

    return {
        "sender": "LLMResponseAgent",
        "receiver": "User",
        "type": "FINAL_RESPONSE",
        "trace_id": message["trace_id"],
        "payload": {
            "answer": response.content
        }
    }
