from pydantic import BaseModel, Field
from datetime import datetime
from models.ServiceRequest import ServiceRequest


class WorkerState(BaseModel):

    # קלט גולמי
    raw_text: str

    # נבנה ע"י InputToRequestWorker
    request: ServiceRequest | None = None

    # ניתוח
    category: str | None = None
    sentiment: str | None = None
    priority: str | None = None

    # נתוני לקוח
    customer_tier: str | None = None
    open_cases: int = 0

    # תגובה
    response_draft: str | None = None

    # ניתוב
    assigned_team: str | None = None
    escalate: bool = False

    # סטטוס
    status: str = "new"

    created_at: datetime = Field(
        default_factory=datetime.utcnow
    )