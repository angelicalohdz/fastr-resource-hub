---
marp: true
theme: fastr
paginate: true
---

## Service utilization analysis

The Service Utilization module (Module 3 in the FASTR analytics platform) analyzes health service delivery patterns to detect and quantify disruptions in service volumes over time.

**Key capabilities:**
- Identifies when health services deviate significantly from expected patterns
- Measures magnitude of disruptions at national, provincial, and district levels
- Distinguishes normal fluctuations from genuine disruptions requiring investigation

---

### Two-stage analysis process

**Part 1: Control chart analysis**
- Model expected patterns using historical trends and seasonality
- Detect significant deviations from expected volumes
- Flag disrupted periods

**Part 2: Disruption quantification**
- Use panel regression to estimate service volume changes
- Calculate shortfalls and surpluses in absolute numbers
