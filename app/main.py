import time
from customer import get_customer_query
from llm import get_llm_response
from graph import graph

query = get_customer_query()

initial_state  = {
    "query" : query,
    "intent" : "",
    "response": ""
}

result = graph.invoke(initial_state)

intent = result["intent"]

print(f"Detected intent : {intent}")

start_time = time.perf_counter()

response = get_llm_response(query,intent)

end_time = time.perf_counter()

print(response)


print(f"\nLLM latency: {end_time - start_time:.2f} seconds")


