import time
from customer import get_customer_query
from llm import get_llm_response

query = get_customer_query()

start_time = time.perf_counter()

response = get_llm_response(query)

end_time = time.perf_counter()

print(response)


print(f"\nLLM latency: {end_time - start_time:.2f} seconds")


