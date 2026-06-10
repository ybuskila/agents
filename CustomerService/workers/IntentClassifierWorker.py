from models.WorkerState import WorkerState
from models.IntentResult import IntentResult
from langchain.prompts import ChatPromptTemplate
from llm import llm


def IntentClassifierWorker(state: WorkerState) -> dict:
    prompt = ChatPromptTemplate.from_template("""
                                              אתה עוזר לנתח פניות שירות, קיבלת טקסט חופשי
                                             החזר intent בלבד.
                                            דוגמאות:
                                            technical_support
                                            refund_request
                                            cancel_request
                                            delivery_issue
                                            general_question
                                             הטקסט:
                                             {start_text}                                    
                                              """)
    
    structured_llm = llm.with_structured_output(IntentResult)
    
    pipe = prompt | structured_llm
    result  = pipe.invoke({"start_text": state.request.start_text})
    
    return {
    "intent": result.intent
   }