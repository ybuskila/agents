from langgraph.graph import StateGraph, END, START
from models.lesson import LessonExtraction
from chains.extraction_chain import lesson_extractor_worker 
from chains.youtube_chain import lesson_youtube_link_loader

state_gr = StateGraph(LessonExtraction)
state_gr.add_node("lesson_extractor_worker", lesson_extractor_worker)
state_gr.add_node("lesson_youtube_link_loader", lesson_youtube_link_loader)
state_gr.add_edge(START, "lesson_extractor_worker")
state_gr.add_edge("lesson_extractor_worker", "lesson_youtube_link_loader")
state_gr.add_edge("lesson_youtube_link_loader", END)

state_gr_worker = state_gr.compile()