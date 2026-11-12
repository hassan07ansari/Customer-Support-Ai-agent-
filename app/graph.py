from langgraph.graph import StateGraph,START,END

from state import SupportState
from nodes import (classify_intent_node,cancel_order_node,refund_or_complaint_node,
                   order_status_node,general_faq_node,process_order_number_node,
                   request_order_number_node)


builder = StateGraph(SupportState)

def route_customer_message(state:SupportState):
    if state['awaiting_order_number']:
        return 'process_order_number'

    return 'classify_intent'

def route_intent(state:SupportState):
    if state["intent"] == "order_status" and not state.get("order_number"):
        return "request_order_number"
    
    return state["intent"]

def route_after_order_number(state: SupportState):

    if state["awaiting_order_number"]:
        return "retry"

    return state["intent"]


builder.add_node("classify_intent",classify_intent_node)
builder.add_node("cancel_order",cancel_order_node)
builder.add_node("order_status",order_status_node)
builder.add_node("refund_or_complaint",refund_or_complaint_node)
builder.add_node("general_faq",general_faq_node)
builder.add_node("process_order_number",process_order_number_node)
builder.add_node("request_order_number",request_order_number_node)

builder.add_conditional_edges(
    START,
    route_customer_message,
    {
        "process_order_number" : "process_order_number",
        "classify_intent" : "classify_intent"
    }
)

builder.add_conditional_edges(
    "classify_intent",
    route_intent,
    {
         "cancel_order": "cancel_order",
        "order_status": "order_status",
        "refund_or_complaint": "refund_or_complaint",
        "general_faq": "general_faq",
        "request_order_number" : "request_order_number"
    }
)

builder.add_conditional_edges(
    "process_order_number",
    route_after_order_number,
    {
        "retry": END,
        "cancel_order": "cancel_order",
        "order_status": "order_status",
        "refund_or_complaint": "refund_or_complaint",
        "general_faq": "general_faq"
    }
)

builder.add_edge("cancel_order", END)
builder.add_edge("order_status", END)
builder.add_edge("refund_or_complaint", END)
builder.add_edge("general_faq",END)
builder.add_edge("request_order_number",END)

graph = builder.compile()

