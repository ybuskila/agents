from langgraph.graph import StateGraph, START
from workers.InputToRequestWorker import InputToRequestWorker
from models.WorkerState import WorkerState

state_gr = StateGraph(WorkerState)

state_gr.add_node("InputToRequestWorker", InputToRequestWorker)

state_gr.add_edge(START, "InputToRequestWorker")

state_gr_worker = state_gr.compile()
