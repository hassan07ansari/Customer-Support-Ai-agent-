from state import SupportState
from llm import process_customer_query
from database import get_order_details, get_shipment_details


def classify_intent_node(state: SupportState):
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


def process_order_number_node(state: SupportState):

    order_number = state["current_message"].strip()

    # Retrieve order information
    order_details = get_order_details(order_number)

    if order_details is None:
        return {
            "response": "I couldn't find an order with that number. Please check and provide your order number again.",
            "awaiting_order_number": True
        }

    # Retrieve shipment information
    shipment_details = get_shipment_details(order_number)

    return {
        "order_number": order_number,
        "order_details": order_details,
        "shipment_details": shipment_details,
        "awaiting_order_number": False
    }


def order_status_node(state: SupportState):

    order = state["order_details"]
    shipment = state.get("shipment_details")

    response = f"""
    Here are your order details:

    Order Number: {order['order_number']}
    Order Status: {order['status']}
    Order Date: {order['placed_at']}
    Expected Delivery: {order['expected_delivery_date']}
    Total Amount: ₹{order['total_inr']}
    """

    if shipment:
        response += f"""

    Shipment Details:

    Carrier: {shipment['carrier']}
    Tracking Number: {shipment['tracking_number']}
    Shipment Status: {shipment['status']}
    Estimated Delivery: {shipment['estimated_delivery_date']}
    Last Known Location: {shipment['last_known_location']}
    """
    else:
        response += """

    Shipment details are not available yet.
    """

    return {"response": response}


def refund_or_complaint_node(state: SupportState):
    return {"response": state["response"]}


def general_faq_node(state: SupportState):
    return {"response": state["response"]}


def request_order_number_node(state: SupportState):

    return {
        "response": "Please provide your order number so I can check its status.",
        "awaiting_order_number": True
    }
