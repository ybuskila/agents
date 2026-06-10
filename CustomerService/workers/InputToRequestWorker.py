from models.WorkerState import WorkerState
from llm import llm
from langchain.prompts import ChatPromptTemplate
from models.ServiceRequest import ServiceRequest

def InputToRequestWorker(state: WorkerState) -> WorkerState:  
    prompt = ChatPromptTemplate.from_template("""
             אתה עוזר לנתח פניות שירות.
             קיבלת טקסט חופשי.
            חלץ:
            - subject → כותרת קצרה
            - start_text → העתק את הטקסט המקורי בדיוק כמו שקיבלת, ללא שינוי וללא קיצור.

            הטקסט:
            {start_text}
    """)
    structured_llm = llm.with_structured_output(ServiceRequest)
    
    pipe = prompt | structured_llm
    request  = pipe.invoke({"start_text": state.raw_text})
    
    return {
    "request": request
   }