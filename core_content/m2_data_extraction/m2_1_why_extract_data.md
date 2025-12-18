---
marp: true
theme: fastr
paginate: true
---

## Why Extract Data?

### Why Extract Data from DHIS2? Why not analyse directly inside DHIS2?

**The FASTR Analytics Platform applies data quality adjustments**

The FASTR methodology includes specific approaches to:
- Identify and adjust for outliers
- Adjust for incomplete reporting
- Apply consistent data quality metrics

These adjustments require processing that cannot be done within DHIS2's native analytics.

### What Format and Granularity is Required?

Data should be extracted at the **facility-month level** to enable:
- Facility-level data quality assessment
- Subnational disaggregation of results
- Longitudinal trend analysis
