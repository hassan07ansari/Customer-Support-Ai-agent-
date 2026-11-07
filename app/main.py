import time
from customer import get_customer_query
from llm import process_customer_query
from graph import graph

query = get_customer_query()

initial_state  = {
    "query" : query,
    "current_message" : query,
    "intent" : "",
    "response": "",
    "awaiting_order_number":False
}



start_time = time.perf_counter()

state = initial_state

while True:

    result = graph.invoke(state)

    print(f"\nCustomer Support Response:\n{result['response']}")

    if not result["awaiting_order_number"]:
        break

    customer_reply = input("\nYou: ")

    state = {
        **result,
        "current_message": customer_reply
    }

end_time = time.perf_counter()

print(f"\nDetected intent: {result['intent']}")
print(f"\nTotal workflow latency: {end_time - start_time:.2f} seconds")