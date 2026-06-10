from llm import llm
from models.ServiceRequest import ServiceRequest
from models.WorkerState import WorkerState

from workers.orcestor_builder import state_gr_worker

state = WorkerState(
    raw_text="I have an issue with my order #12345. It hasn't arrived yet"
)

result  = state_gr_worker.invoke(state)
print(result)