import time
from customer import get_customer_query
from llm import process_customer_query
from graph import graph

query = get_customer_query()

initial_state  = {
    "query" : query,
    "intent" : "",
    "response": ""
}



start_time = time.perf_counter()

result = graph.invoke(initial_state)

end_time = time.perf_counter()

intent = result["intent"]
response = result["response"]

print(f"\nDetected intent: {intent}")
print(f"\nCustomer Support Response:\n{response}")
print(f"\nTotal workflow latency: {end_time - start_time:.2f} seconds")




