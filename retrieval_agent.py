from utils.vector_store import get_retriever
from utils.mcp_protocol import MCPMessage

def retrieve_context(message: MCPMessage, query: str) -> MCPMessage:
    store = message["payload"]["vectorstore"]
    retriever = get_retriever(store)
    results = retriever.get_relevant_documents(query)
    context = "\n".join([doc.page_content for doc in results])

    return {
        "sender": "RetrievalAgent",
        "receiver": "LLMResponseAgent",
        "type": "CONTEXT_RESPONSE",
        "trace_id": message["trace_id"],
        "payload": {
            "context": context,
            "query": query
        }
    }
