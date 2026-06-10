from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class ServiceRequest(BaseModel):
            
    subject: str = ""  
    start_text: str = ""