from llm import llm
from models.ServiceRequest import ServiceRequest

from workers.orcestor_builder import state_gr_worker


request = ServiceRequest (
    start_text = "I have an issue with my order #12345. It hasn't arrived yet"
)

result  = state_gr_worker.invoke(request)
print(result)