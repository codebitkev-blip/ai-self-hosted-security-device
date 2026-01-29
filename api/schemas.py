from pydantic import BaseModel

class Alert(BaseModel):
    id: int
    src: str
    dst: str
    size: int

class AlertStats(BaseModel):
    total_alerts: int
    unique_sources: int
