from pydantic import BaseModel
from typing import List, Optional

# llm output format models
# quantitative: {"Disclosure": <0 or 1>, "Data": {"KPI": "{kpi}", "Topic": "{topic}", "Value":"<value>", "Unit": "<unit>"}}
# qualititative: {"Disclosure": <0 or 1>, "Data": {"KPI": "{kpi}", "Topic": "{topic}", "Target":"<target>", "Action": "<action>"}}

class ESGQuantData(BaseModel):
  kpi: str
  topic: str
  value: float
  unit: str

class ESGQuantResponse(BaseModel):
  disclosure: bool
  data: list[ESGQuantData]

class ESGQualData(BaseModel):
  kpi: str
  topic: str
  target: str
  action: str

class ESGQualResponse(BaseModel):
  disclosure: bool
  data: list[ESGQualData]

# graph models - WIP
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