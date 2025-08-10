## **📌 Project Blueprint — ESG Disclosure Classifier**

**Goal**
Automatically classify whether a company’s public documents (reports, press releases, or filings) disclose specific ESG metrics — e.g., greenhouse gas emissions, water usage, diversity metrics.

**Problem Statement**
Companies often publish long reports where ESG disclosures are buried in text. This tool flags and categorizes those disclosures automatically, saving analysts time and improving data quality.

**Example Input**
Text from annual ESG reports, 10-K sustainability sections, or CDP responses.

**Example Output**

| Sentence                                                              | Disclosure Type       | Confidence |
| --------------------------------------------------------------------- | --------------------- | ---------- |
| “Our Scope 1 emissions in 2023 totaled 1.5 million metric tons CO₂e.” | Emissions             | 0.94       |
| “We increased women in leadership positions from 20% to 25%.”         | Diversity & Inclusion | 0.88       |
