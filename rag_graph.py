from langgraph.graph import StateGraph, END
from utils.mcp_protocol import MCPMessage
from agents.retrieval_agent import retrieve_context
from agents.llm_response_agent import generate_response

def build_rag_graph(vectorstore, query: str):
    graph = StateGraph(MCPMessage)

    def retrieval_step(message: MCPMessage) -> MCPMessage:
        return retrieve_context(message, query)

    def response_step(message: MCPMessage) -> MCPMessage:
        return generate_response(message)

    graph.add_node("retrieve", retrieval_step)
    graph.add_node("respond", response_step)

    graph.set_entry_point("retrieve")
    graph.add_edge("retrieve", "respond")
    graph.add_edge("respond", END)

    return graph.compile()
