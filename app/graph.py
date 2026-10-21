from langgraph.graph import StateGraph,START,END

from state import SupportState
from nodes import (classify_intent_node,cancel_order_node,refund_or_complaint_node,order_status_node)


builder = StateGraph(SupportState)

def route_intent(state:SupportState):
    return state['intent']

builder.add_node("classify_intent",classify_intent_node)
builder.add_node("cancel_order",cancel_order_node)
builder.add_node("order_status",order_status_node)
builder.add_node("refund_or_complaint",refund_or_complaint_node)

builder.add_edge(START,"classify_intent")

builder.add_conditional_edges(
    "classify_intent",
    route_intent,
    {
         "cancel_order": "cancel_order",
        "order_status": "order_status",
        "refund_or_complaint": "refund_or_complaint",
        "general_faq": END
    }
)

builder.add_edge("cancel_order", END)
builder.add_edge("order_status", END)
builder.add_edge("refund_or_complaint", END)


graph = builder.compile()

