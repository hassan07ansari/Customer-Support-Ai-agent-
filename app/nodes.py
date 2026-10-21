from state import SupportState
from llm import classify_intent

def classify_intent_node(state:SupportState):
    intent = classify_intent(state["query"])

    return {"intent" : intent}

