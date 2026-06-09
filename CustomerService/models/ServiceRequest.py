from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class ServiceRequest(BaseModel):
    class Config:        
        populate_by_name = True
  
    start_text: str = Field(
        description="הטקסט שהבאת מהשיעור",
        alias="טקסט התחלתי",
        default=""
    )