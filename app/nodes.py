from state import SupportState
from llm import process_customer_query

def classify_intent_node(state:SupportState):
    result = process_customer_query(state["query"])

    lines = result.splitlines()

    intent = lines[0].replace("Intent:", "").strip()
    response = "\n".join(lines[1:]).replace("Response:", "", 1).strip()

    return {
        "intent": intent,
        "response": response
    }


def cancel_order_node(state: SupportState):
    return {"response": state["response"]}


def order_status_node(state: SupportState):
    return {"response": state["response"]}


def refund_or_complaint_node(state: SupportState):
    return {"response": state["response"]}


def general_faq_node(state: SupportState):
    return {"response": state["response"]}


