from langchain_ollama import ChatOllama


llm = ChatOllama(
    model="qwen3:4b-instruct",
    temperature=0
)

def process_customer_query(query):

    prompt = f"""
    You are a customer support assistant.

    Classify the customer query into exactly one intent:
    order_status
    cancel_order
    refund_or_complaint
    general_faq

    Return your answer in exactly this format:
    Intent: <intent>
    Response: <customer support response>

    Customer query: {query}
    """

    result = llm.invoke(prompt)

    return result.content.strip()
