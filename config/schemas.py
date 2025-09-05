from pydantic import BaseModel
from typing import List, Optional

class Provenance(BaseModel):
    doc_id: str
    page: int
    table_id: Optional[str]
    text_span: str

class Measure(BaseModel):
    value: Optional[float]
    unit: str
    period_start: Optional[str]
    period_end: Optional[str]
    boundary: Optional[str]
    scope_detail: Optional[str]
    location: Optional[str]
    methodology: Optional[str]
    provenance: Provenance
    confidence: float

class Metric(BaseModel):
    metric_name: str
    standard_codes: List[str]
    measures: List[Measure]

class ReportExtract(BaseModel):
    company: dict
    report: dict
    metrics: List[Metric]   