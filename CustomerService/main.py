from llm import llm
from models.ServiceRequest import ServiceRequest
from models.WorkerState import WorkerState

from workers.orcestor_builder import state_gr_worker

state = WorkerState(
    raw_text="""I have an issue with my order #12345. It hasn't arrived yet. 
                My Computer is not working, and I need help with it. 
                Please do it as soon as possible, I am loosing money every day. 
                I am very frustrated and I need this issue resolved quickly. 
                I have tried contacting customer support multiple times, but I haven't received any response. 
                I am considering taking legal action if this issue is not resolved soon. 
                Please prioritize my request and provide a solution as soon as possible. Thank you."""
)

result  = state_gr_worker.invoke(state)
print(result)