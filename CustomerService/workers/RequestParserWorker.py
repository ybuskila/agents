from models.ServiceRequest import ServiceRequest
from llm import llm
from langchain.prompts import ChatPromptTemplate

def RequestParserWorker(request: ServiceRequest) -> ServiceRequest:                    
    """
    Parses the incoming request and extracts relevant information.

    Args:
        request (ServiceRequest): The service request object.
    """
    prompt = ChatPromptTemplate.from_template("""
             אתה עוזר לנתח בקשות שירות. אתה מקבל בקשה עם פרטים שונים, ואתה צריך לחלץ את המידע הרלוונטי ולארגן אותו בצורה מסודרת.
             הבקשה כוללת את הפרטים הבאים:  
                {request_details} 
             """)
    structured_llm = llm.with_structured_output(ServiceRequest)
    
    pipe = prompt | structured_llm
    result = pipe.invoke({"request_details":request.start_text})
    return result
    