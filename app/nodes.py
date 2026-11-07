from state import SupportState
from llm import process_customer_query
from database import get_order_details



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

def request_order_number_node(state:SupportState):

    return {
        "response" : "Please provide your order number so i can check its status",
        "awaiting_order_number" : True
    }

def process_order_number_node(state: SupportState):

    order_number = state["current_message"].strip()

    order_details = get_order_details(order_number)

    if order_details is None:
        return {
            "response": "I couldn't find an order with that number. Please check and provide your order number again.",
            "awaiting_order_number": True
        }

    return {
        "order_number": order_number,
        "order_details": order_details,
        "awaiting_order_number": False
    }



