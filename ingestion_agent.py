from utils.document_parser import load_and_split_documents
from utils.vector_store import create_vectorstore
from utils.mcp_protocol import MCPMessage
import uuid

def ingest_documents(file_paths: list[str]) -> MCPMessage:
    docs = load_and_split_documents(file_paths)
    store = create_vectorstore(docs)
    return {
        "sender": "IngestionAgent",
        "receiver": "RetrievalAgent",
        "type": "DOCS_PARSED",
        "trace_id": str(uuid.uuid4()),
        "payload": {
            "vectorstore": store
        }
    }
