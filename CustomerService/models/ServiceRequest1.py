from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class ServiceRequest(BaseModel):
    class Config:        
        populate_by_name = True

    # מקור
    request_id: str
    source: str
    customer_id: Optional[str] = None

    # תוכן
    subject: str
    start_text: str = Field(
        description="הטקסט שהבאת מהשיעור",
        alias="טקסט התחלתי"
    )

    # ניתוח
    category: Optional[str] = None
    sentiment: Optional[str] = None
    priority: Optional[str] = None

    # נתוני לקוח
    customer_tier: Optional[str] = None
    open_cases: int = 0

    # תגובה
    response_draft: Optional[str] = None

    # ניתוב
    assigned_team: Optional[str] = None
    escalate: bool = False

    # סטטוס
    status: str = "new"

    # זמנים
    created_at: datetime = datetime.utcnow()