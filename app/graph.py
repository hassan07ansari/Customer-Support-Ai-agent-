from langgraph.graph import StateGraph,START,END

from state import SupportState
from nodes import classify_intent_node


builder = StateGraph(SupportState)

builder.add_node("classify_intent",classify_intent_node)

builder.add_edge(START,"classify_intent")

builder.add_edge("classify_intent",END)

graph = builder.compile()

