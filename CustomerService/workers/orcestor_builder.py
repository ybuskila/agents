from langgraph.graph import StateGraph, START
from workers.RequestParserWorker import RequestParserWorker

from models.ServiceRequest import ServiceRequest

state_gr = StateGraph(ServiceRequest)

state_gr.add_node("RequestParserWorker", RequestParserWorker)

state_gr.add_edge(START, "RequestParserWorker")

state_gr.compile()  

state_gr_worker = state_gr.compile()
