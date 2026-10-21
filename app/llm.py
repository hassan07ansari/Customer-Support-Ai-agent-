from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="qwen3:4b-instruct",
    temperature = 0)

def get_llm_response(query,intent):

    prompt = f"Customer intent: {intent}\nCustomer query: {query}\nRespond appropriately to the customer's intent."
    response = llm.invoke(prompt)
    
    return response.content

def classify_intent(query):
    prompt = f"""
    Classify the customer query into exactly one category:
    order_status
    cancel_order
    refund_or_complaint
    general_faq

    Return only the category name.

    Customer query: {query}
    """

    response = llm.invoke(prompt)

    return response.content.strip()