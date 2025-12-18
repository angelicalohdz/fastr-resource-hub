---
marp: true
theme: fastr
paginate: true
---

## Service Utilization Analysis

The Service Utilization module (Module 3 in the FASTR analytics platform) analyzes health service delivery patterns to detect and quantify disruptions in service volumes over time.

**Key capabilities:**
- Identifies when health services deviate significantly from expected patterns
- Measures magnitude of disruptions at national, provincial, and district levels
- Distinguishes normal fluctuations from genuine disruptions requiring investigation

---

### Two-Stage Analysis Process

**Stage 1: Control Chart Analysis**
- Model expected patterns using historical trends and seasonality
- Detect significant deviations from expected volumes
- Flag disrupted periods

**Stage 2: Disruption Quantification**
- Use panel regression to estimate service volume changes
- Calculate shortfalls and surpluses in absolute numbers
