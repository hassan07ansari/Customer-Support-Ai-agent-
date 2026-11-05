from typing import TypedDict , NotRequired


class SupportState(TypedDict):
    query : str
    current_message : str
    intent : NotRequired[str]
    order_number : NotRequired[str]
    order_details : NotRequired[dict]
    
    response : str
    awaiting_order_number : bool
