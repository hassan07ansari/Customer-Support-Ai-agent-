
from typing import TypedDict, NotRequired


class SupportState(TypedDict):
    # Customer messages
    query: str
    current_message: str

    # Intent classification
    intent: NotRequired[str]

    # Order information
    order_number: NotRequired[str]
    order_details: NotRequired[dict]

    # Shipment information
    shipment_details: NotRequired[dict | None]

    # Agent response and conversation flow
    response: str
    awaiting_order_number: bool
