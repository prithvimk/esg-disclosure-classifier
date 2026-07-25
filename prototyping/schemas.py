"""
Pydantic schemas for extracting climate-related data from sustainability
reports into a knowledge graph.

Designed for LLM-based structured extraction (LlamaIndex / Instructor / etc.)
targeting a Property Graph where:
  - Nodes  = entities   (Organization, Facility, EmissionMetric, …)
  - Edges  = relations  (REPORTS_METRIC, HAS_TARGET, LOCATED_IN, …)

Aligned with GRI 300-series, SASB, and TCFD disclosure frameworks.
"""

from __future__ import annotations

from datetime import date
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


# ──────────────────────────────────────────────────────────────────────
#  Enums
# ──────────────────────────────────────────────────────────────────────

class GHGScope(str, Enum):
    """Greenhouse-gas emission scope per the GHG Protocol."""
    SCOPE_1 = "scope_1"
    SCOPE_2_LOCATION = "scope_2_location_based"
    SCOPE_2_MARKET = "scope_2_market_based"
    SCOPE_3 = "scope_3"


class Scope3Category(str, Enum):
    """Material Scope 3 categories commonly reported in sustainability reports."""
    PURCHASED_GOODS_AND_SERVICES = "purchased_goods_and_services"
    CAPITAL_GOODS = "capital_goods"
    FUEL_AND_ENERGY = "fuel_and_energy_related_activities"
    UPSTREAM_TRANSPORT = "upstream_transportation_and_distribution"
    WASTE_GENERATED = "waste_generated_in_operations"
    BUSINESS_TRAVEL = "business_travel"
    EMPLOYEE_COMMUTING = "employee_commuting"
    UPSTREAM_LEASED_ASSETS = "upstream_leased_assets"
    DOWNSTREAM_TRANSPORT = "downstream_transportation_and_distribution"
    PROCESSING_OF_SOLD_PRODUCTS = "processing_of_sold_products"
    USE_OF_SOLD_PRODUCTS = "use_of_sold_products"
    END_OF_LIFE_TREATMENT = "end_of_life_treatment_of_sold_products"
    DOWNSTREAM_LEASED_ASSETS = "downstream_leased_assets"
    FRANCHISES = "franchises"
    INVESTMENTS = "investments"


class EnergySourceType(str, Enum):
    """Primary energy source categories."""
    NATURAL_GAS = "natural_gas"
    JET_KEROSENE = "jet_kerosene"
    FUEL_OIL = "fuel_oil"
    MOTOR_GASOLINE = "motor_gasoline"
    PROPANE = "propane"
    LPG = "liquefied_petroleum_gas"
    SAF = "sustainable_aviation_fuel"
    RENEWABLE_ELECTRICITY = "renewable_electricity"
    NONRENEWABLE_ELECTRICITY = "nonrenewable_electricity"
    SOLAR = "solar"
    WIND = "wind"
    HYDROPOWER = "hydropower"
    BIOMASS = "biomass"
    GEOTHERMAL = "geothermal"
    OTHER = "other"


class WasteCategory(str, Enum):
    """Waste classification."""
    HAZARDOUS = "hazardous"
    NONHAZARDOUS = "nonhazardous"
    UNIVERSAL = "universal"
    SOLID = "solid"


class WasteDisposalMethod(str, Enum):
    """Waste disposal methods per GRI 306."""
    RECYCLED = "recycled"
    COMPOSTED = "composted"
    REUSED = "reused"
    INCINERATION_ENERGY_RECOVERY = "incineration_with_energy_recovery"
    INCINERATION_NO_RECOVERY = "incineration_without_energy_recovery"
    LANDFILL = "landfill"
    OTHER = "other_disposal"


class WaterSourceType(str, Enum):
    """Water withdrawal source type per GRI 303."""
    SURFACE_WATER = "surface_water"
    GROUNDWATER = "groundwater"
    THIRD_PARTY = "third_party"
    RAINWATER = "rainwater"
    SEAWATER = "seawater"
    RECLAIMED = "reclaimed"


class TargetStatus(str, Enum):
    """Progress status for a climate target or commitment."""
    NOT_STARTED = "not_started"
    IN_PROGRESS = "in_progress"
    ON_TRACK = "on_track"
    BEHIND = "behind"
    ACHIEVED = "achieved"
    EXCEEDED = "exceeded"


class ClimateRiskType(str, Enum):
    """TCFD climate-related risk categories."""
    TRANSITION_POLICY = "transition_policy_and_legal"
    TRANSITION_TECHNOLOGY = "transition_technology"
    TRANSITION_MARKET = "transition_market"
    TRANSITION_REPUTATION = "transition_reputation"
    PHYSICAL_ACUTE = "physical_acute"
    PHYSICAL_CHRONIC = "physical_chronic"


class ClimateOpportunityType(str, Enum):
    """TCFD climate-related opportunity categories."""
    RESOURCE_EFFICIENCY = "resource_efficiency"
    ENERGY_SOURCE = "energy_source"
    PRODUCTS_AND_SERVICES = "products_and_services"
    MARKETS = "markets"
    RESILIENCE = "resilience"


class DisclosureFramework(str, Enum):
    """Sustainability disclosure frameworks."""
    GRI = "GRI"
    SASB = "SASB"
    TCFD = "TCFD"
    CDP = "CDP"
    ISSB = "ISSB"
    CSRD = "CSRD"
    SBTi = "SBTi"


class RelationshipType(str, Enum):
    """Edge types for the knowledge graph."""
    REPORTS_METRIC = "REPORTS_METRIC"
    HAS_TARGET = "HAS_TARGET"
    HAS_INITIATIVE = "HAS_INITIATIVE"
    LOCATED_IN = "LOCATED_IN"
    OPERATES_FACILITY = "OPERATES_FACILITY"
    SUBSIDIARY_OF = "SUBSIDIARY_OF"
    PARTNERS_WITH = "PARTNERS_WITH"
    GOVERNED_BY = "GOVERNED_BY"
    USES_ENERGY_SOURCE = "USES_ENERGY_SOURCE"
    ALIGNED_WITH_FRAMEWORK = "ALIGNED_WITH_FRAMEWORK"
    PRODUCES_WASTE = "PRODUCES_WASTE"
    WITHDRAWS_WATER = "WITHDRAWS_WATER"
    FACES_RISK = "FACES_RISK"
    HAS_OPPORTUNITY = "HAS_OPPORTUNITY"
    MITIGATES = "MITIGATES"
    SUPERSEDES = "SUPERSEDES"
    REFERENCES_REGULATION = "REFERENCES_REGULATION"
    VERIFIED_BY = "VERIFIED_BY"


# ──────────────────────────────────────────────────────────────────────
#  Base / shared models
# ──────────────────────────────────────────────────────────────────────

class SourceReference(BaseModel):
    """Provenance pointer back to the original document."""
    document_name: str = Field(
        ..., description="Name or title of the source report."
    )
    page_or_section: Optional[str] = Field(
        None, description="Page number, section heading, or chunk ID."
    )
    excerpt: Optional[str] = Field(
        None, description="Verbatim quote supporting the extracted fact."
    )


class ReportingPeriod(BaseModel):
    """The time window a metric or disclosure covers."""
    start_date: Optional[date] = Field(
        None, description="Start of the reporting period (YYYY-MM-DD)."
    )
    end_date: Optional[date] = Field(
        None, description="End of the reporting period (YYYY-MM-DD)."
    )
    fiscal_year: Optional[int] = Field(
        None, description="Fiscal/calendar year the data represents."
    )


# ──────────────────────────────────────────────────────────────────────
#  Node models (knowledge-graph entities)
# ──────────────────────────────────────────────────────────────────────

class Organization(BaseModel):
    """A company, subsidiary, or joint venture mentioned in the report."""
    name: str = Field(..., description="Legal or common name of the entity.")
    ticker: Optional[str] = Field(None, description="Stock ticker symbol.")
    industry: Optional[str] = Field(None, description="GICS or NAICS industry.")
    headquarters: Optional[str] = Field(None, description="City/country of HQ.")
    description: Optional[str] = Field(
        None, description="Brief description of the organization."
    )


class Facility(BaseModel):
    """A physical site (factory, office, lab, warehouse) owned or operated."""
    name: str = Field(..., description="Name or identifier of the facility.")
    location: Optional[str] = Field(
        None, description="City, state/province, country."
    )
    facility_type: Optional[str] = Field(
        None, description="E.g. manufacturing, office, laboratory, warehouse."
    )
    area_sqft: Optional[float] = Field(
        None, description="Total area in square feet."
    )
    is_water_stressed: Optional[bool] = Field(
        None, description="Whether the facility is in a water-stressed area."
    )


class GovernanceBody(BaseModel):
    """A board committee or management-level body overseeing climate matters."""
    name: str = Field(..., description="Name of the governance body.")
    role: Optional[str] = Field(
        None, description="Its responsibility in climate/ESG oversight."
    )
    reporting_frequency: Optional[str] = Field(
        None, description="How often it reviews climate topics (e.g. quarterly)."
    )


# ──────────────────────────────────────────────────────────────────────
#  Metric nodes
# ──────────────────────────────────────────────────────────────────────

class GHGEmission(BaseModel):
    """A single GHG emissions data point."""
    scope: GHGScope = Field(..., description="GHG Protocol scope.")
    scope_3_category: Optional[Scope3Category] = Field(
        None, description="Applicable only when scope is SCOPE_3."
    )
    value: float = Field(
        ..., description="Emissions quantity."
    )
    unit: str = Field(
        default="metric_tons_co2e",
        description="Unit of measurement (e.g. metric_tons_co2e)."
    )
    reporting_period: ReportingPeriod = Field(
        ..., description="Time period this measurement covers."
    )
    methodology: Optional[str] = Field(
        None,
        description="Calculation methodology (e.g. GHG Protocol, EPA factors)."
    )
    verified: Optional[bool] = Field(
        None, description="Whether the data was third-party verified."
    )
    verifier: Optional[str] = Field(
        None, description="Name of the third-party verifier, if applicable."
    )
    source: Optional[SourceReference] = Field(
        None, description="Where in the report this data was found."
    )


class EnergyConsumption(BaseModel):
    """An energy consumption data point."""
    source_type: EnergySourceType = Field(
        ..., description="Type of energy source."
    )
    value: float = Field(..., description="Energy quantity consumed.")
    unit: str = Field(
        default="terajoules",
        description="Unit of measurement (e.g. terajoules, MWh, GJ)."
    )
    is_renewable: bool = Field(
        ..., description="Whether this is a renewable energy source."
    )
    reporting_period: ReportingPeriod = Field(
        ..., description="Time period this measurement covers."
    )
    source: Optional[SourceReference] = Field(
        None, description="Where in the report this data was found."
    )


class WaterMetric(BaseModel):
    """A water withdrawal, discharge, or consumption data point."""
    source_type: WaterSourceType = Field(
        ..., description="Type of water source."
    )
    metric_type: str = Field(
        ..., description="One of: withdrawal, discharge, consumption, reclaimed."
    )
    value: float = Field(..., description="Volume of water.")
    unit: str = Field(
        default="megaliters", description="Unit (e.g. megaliters, cubic_meters)."
    )
    is_water_stressed_area: Optional[bool] = Field(
        None, description="Whether drawn from a water-stressed region."
    )
    reporting_period: ReportingPeriod = Field(
        ..., description="Time period this measurement covers."
    )
    source: Optional[SourceReference] = Field(
        None, description="Where in the report this data was found."
    )


class WasteMetric(BaseModel):
    """A waste generation / disposal data point."""
    category: WasteCategory = Field(..., description="Waste classification.")
    disposal_method: WasteDisposalMethod = Field(
        ..., description="How the waste was handled."
    )
    value: float = Field(..., description="Quantity of waste.")
    unit: str = Field(
        default="metric_tons", description="Unit (e.g. metric_tons, kg)."
    )
    reporting_period: ReportingPeriod = Field(
        ..., description="Time period this measurement covers."
    )
    source: Optional[SourceReference] = Field(
        None, description="Where in the report this data was found."
    )


# ──────────────────────────────────────────────────────────────────────
#  Target / commitment models
# ──────────────────────────────────────────────────────────────────────

class ClimateTarget(BaseModel):
    """A quantified climate-related goal or commitment."""
    description: str = Field(
        ..., description="Natural-language description of the target."
    )
    metric_type: str = Field(
        ...,
        description="What the target measures (e.g. ghg_reduction, "
        "renewable_energy_pct, saf_compatibility)."
    )
    target_value: Optional[float] = Field(
        None, description="Numeric target (e.g. 30 for a 30% reduction)."
    )
    target_unit: Optional[str] = Field(
        None, description="Unit for target_value (e.g. percent, metric_tons_co2e)."
    )
    base_year: Optional[int] = Field(
        None, description="Baseline year for the target."
    )
    target_year: Optional[int] = Field(
        None, description="Year by which the target should be achieved."
    )
    status: Optional[TargetStatus] = Field(
        None, description="Current status toward achieving the target."
    )
    progress_value: Optional[float] = Field(
        None, description="Latest reported progress value."
    )
    progress_description: Optional[str] = Field(
        None, description="Qualitative description of progress."
    )
    is_science_based: Optional[bool] = Field(
        None, description="Whether validated by SBTi or equivalent."
    )
    scope: Optional[str] = Field(
        None,
        description="Boundary of the target (e.g. Scope 1+2, operations, "
        "all majority-owned subsidiaries)."
    )
    source: Optional[SourceReference] = Field(
        None, description="Where in the report this target was found."
    )


# ──────────────────────────────────────────────────────────────────────
#  Initiative / project models
# ──────────────────────────────────────────────────────────────────────

class ClimateInitiative(BaseModel):
    """A programme, project, or partnership aimed at climate goals."""
    name: str = Field(..., description="Name of the initiative or programme.")
    description: Optional[str] = Field(
        None, description="Brief summary of what it involves."
    )
    category: Optional[str] = Field(
        None,
        description="E.g. fleet_renewal, SAF, advanced_technology, "
        "operational_efficiency, carbon_removal."
    )
    investment_amount: Optional[float] = Field(
        None, description="Financial commitment, if disclosed."
    )
    investment_currency: Optional[str] = Field(
        None, description="Currency code (e.g. USD)."
    )
    partners: list[str] = Field(
        default_factory=list,
        description="Names of partner organizations or agencies."
    )
    status: Optional[str] = Field(
        None, description="E.g. planned, in_progress, completed."
    )
    start_year: Optional[int] = Field(None, description="Year started.")
    source: Optional[SourceReference] = Field(
        None, description="Where in the report this was found."
    )


# ──────────────────────────────────────────────────────────────────────
#  TCFD-specific models
# ──────────────────────────────────────────────────────────────────────

class ClimateRisk(BaseModel):
    """A climate-related risk identified by the reporting organization (TCFD)."""
    risk_type: ClimateRiskType = Field(
        ..., description="TCFD risk category."
    )
    description: str = Field(
        ..., description="Description of the identified risk."
    )
    time_horizon: Optional[str] = Field(
        None, description="Short / medium / long-term."
    )
    potential_financial_impact: Optional[str] = Field(
        None, description="Qualitative or quantitative financial impact."
    )
    mitigation_strategy: Optional[str] = Field(
        None, description="How the organization plans to mitigate this risk."
    )
    source: Optional[SourceReference] = Field(
        None, description="Where in the report this risk was found."
    )


class ClimateOpportunity(BaseModel):
    """A climate-related opportunity identified by the organization (TCFD)."""
    opportunity_type: ClimateOpportunityType = Field(
        ..., description="TCFD opportunity category."
    )
    description: str = Field(
        ..., description="Description of the opportunity."
    )
    time_horizon: Optional[str] = Field(
        None, description="Short / medium / long-term."
    )
    potential_financial_impact: Optional[str] = Field(
        None, description="Expected positive financial impact."
    )
    strategy: Optional[str] = Field(
        None, description="How the organization plans to realize this."
    )
    source: Optional[SourceReference] = Field(
        None, description="Where in the report this was found."
    )


# ──────────────────────────────────────────────────────────────────────
#  Framework alignment
# ──────────────────────────────────────────────────────────────────────

class FrameworkAlignment(BaseModel):
    """Disclosure alignment with a sustainability reporting framework."""
    framework: DisclosureFramework = Field(
        ..., description="The reporting framework."
    )
    standard_or_index: Optional[str] = Field(
        None, description="Specific standard code (e.g. GRI 305, SASB RT-AE-410a)."
    )
    disclosure_description: Optional[str] = Field(
        None, description="What the disclosure covers."
    )
    compliance_status: Optional[str] = Field(
        None, description="full, partial, or referenced."
    )


# ──────────────────────────────────────────────────────────────────────
#  Regulation / policy references
# ──────────────────────────────────────────────────────────────────────

class Regulation(BaseModel):
    """A law, regulation, or industry standard referenced in the report."""
    name: str = Field(..., description="Name of the regulation or standard.")
    jurisdiction: Optional[str] = Field(
        None, description="Country or region where it applies."
    )
    description: Optional[str] = Field(
        None, description="Brief description of relevance to the organization."
    )


# ──────────────────────────────────────────────────────────────────────
#  Relationship (edge) model
# ──────────────────────────────────────────────────────────────────────
class EdgeProperty(BaseModel):
    """A key-value pair for flexible relationship properties."""
    key: str = Field(..., description="Name of the property (e.g., 'year', 'amount').")
    value: str = Field(..., description="Value of the property.")

class Relationship(BaseModel):
    """A directed edge in the knowledge graph."""
    source_entity: str = Field(
        ..., description="Name or ID of the source node."
    )
    source_entity_type: str = Field(
        ...,
        description="Node type of the source (e.g. Organization, Facility)."
    )
    relationship_type: RelationshipType = Field(
        ..., description="The type of relationship."
    )
    target_entity: str = Field(
        ..., description="Name or ID of the target node."
    )
    target_entity_type: str = Field(
        ...,
        description="Node type of the target (e.g. GHGEmission, ClimateTarget)."
    )
    properties: Optional[list[EdgeProperty]] = Field(
        None, description="Additional edge attributes (e.g. year, amount) as key-value pairs."
    )


# ──────────────────────────────────────────────────────────────────────
#  Top-level extraction container
# ──────────────────────────────────────────────────────────────────────

class ClimateDisclosureExtraction(BaseModel):
    """
    Root schema for a full climate-disclosure extraction from a single
    sustainability report.  An LLM should populate this model to produce
    a knowledge graph of climate-related facts.
    """
    # ── Metadata ──────────────────────────────────────────────────────
    report_title: str = Field(
        ..., description="Title of the sustainability report."
    )
    reporting_organization: Organization = Field(
        ..., description="The entity that published the report."
    )
    reporting_period: ReportingPeriod = Field(
        ..., description="Period covered by the report."
    )
    publication_date: Optional[date] = Field(
        None, description="Date the report was published."
    )

    # ── Nodes ─────────────────────────────────────────────────────────
    subsidiaries: list[Organization] = Field(
        default_factory=list,
        description="Subsidiaries or JVs mentioned."
    )
    facilities: list[Facility] = Field(
        default_factory=list,
        description="Physical sites referenced in the report."
    )
    governance_bodies: list[GovernanceBody] = Field(
        default_factory=list,
        description="Committees or bodies overseeing climate/ESG."
    )

    # ── Metrics ───────────────────────────────────────────────────────
    ghg_emissions: list[GHGEmission] = Field(
        default_factory=list,
        description="All GHG emission data points extracted."
    )
    energy_consumption: list[EnergyConsumption] = Field(
        default_factory=list,
        description="All energy consumption data points extracted."
    )
    water_metrics: list[WaterMetric] = Field(
        default_factory=list,
        description="Water withdrawal, discharge, or consumption data."
    )
    waste_metrics: list[WasteMetric] = Field(
        default_factory=list,
        description="Waste generation and disposal data."
    )

    # ── Targets & Initiatives ─────────────────────────────────────────
    climate_targets: list[ClimateTarget] = Field(
        default_factory=list,
        description="All climate-related goals and commitments."
    )
    climate_initiatives: list[ClimateInitiative] = Field(
        default_factory=list,
        description="Programmes, partnerships, and projects."
    )

    # ── TCFD ──────────────────────────────────────────────────────────
    climate_risks: list[ClimateRisk] = Field(
        default_factory=list,
        description="Identified climate-related risks (TCFD)."
    )
    climate_opportunities: list[ClimateOpportunity] = Field(
        default_factory=list,
        description="Identified climate-related opportunities (TCFD)."
    )

    # ── Framework alignment ───────────────────────────────────────────
    framework_alignments: list[FrameworkAlignment] = Field(
        default_factory=list,
        description="Framework disclosures referenced."
    )
    regulations: list[Regulation] = Field(
        default_factory=list,
        description="Regulations and standards referenced."
    )

    # ── Relationships ─────────────────────────────────────────────────
    relationships: list[Relationship] = Field(
        default_factory=list,
        description="Explicit edges connecting entities in the graph."
    )
