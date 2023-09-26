from datetime import datetime

from pydantic import BaseModel


class TransportOrderAuditModel(BaseModel):
    order_id: int
    customer_id: int
    origin: str
    destination: str
    transport_status: str
    change_type: str
    change_timestamp: datetime
    user_id: int
