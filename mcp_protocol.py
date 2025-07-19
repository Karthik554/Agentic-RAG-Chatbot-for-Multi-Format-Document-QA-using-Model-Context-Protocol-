from typing import TypedDict, Literal

class MCPMessage(TypedDict):
    sender: str
    receiver: str
    type: Literal["DOCS_PARSED", "CONTEXT_RESPONSE", "FINAL_RESPONSE"]
    trace_id: str
    payload: dict
