from pydantic import BaseModel
from datetime import datetime
from typing import Literal, List

class AggregationRequest(BaseModel):
    dt_from: datetime
    dt_upto: datetime
    group_type: Literal['hour', 'day', 'month']

class AggregationResponse(BaseModel):
    dataset: List[int]
    labels: List[str]
