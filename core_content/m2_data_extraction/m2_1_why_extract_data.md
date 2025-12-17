---
marp: true
theme: fastr
paginate: true
---

# Data Extraction

---

## Session Objectives

1. Understand why DHIS2 data needs to be extracted for FASTR analyses
2. Understand the required data structure and level of detail
3. Learn about the available tools for extracting or importing data
---

## Why Extract Data from DHIS2? Why not analyse directly inside DHIS2?

<br>**The FASTR Analytics Platform applies data quality adjustments**

- The platform implements the FASTR approach, automatically correcting for missing reports, outliers, and reporting-rate issues.

- This produces more reliable estimates than raw DHIS2 trend charts.

<br>**The platform enables additional analytical methods**

- It operationalises techniques such as regression-based seasonality adjustment, disruption detection, and denominator modelling.
- These methods go beyond what DHIS2 offers through its built-in analytics tools.

<br>**Different tools for different purposes**

- DHIS2 is ideal for quick visual checks.
- The FASTR Analytics Platform is designed for deeper, reproducible analysis that supports interpretation and decision-making.

---

## How the FASTR Analytics Platform Expects the Data

<div class="columns">

<div>

### Direct Import

The platform expects **facility-level, monthly data** in a standard long format.
<br>**The Direct Import builds this structure for you automatically.**

It:
- Calls the DHIS2 API
- Applies the correct long-format structure
- Standardises organisational units
- Ensures completeness of required fields

No manual formatting is needed.

</div>

<div>

### If uploading CSVs manually

When data are prepared using the Downloader, API script, or DHIS2 exports, the CSV must follow this structure:

**Data format principles**
- **Facility-level:** each row corresponds to a facility
- **Monthly:** one record per facility–indicator–month
- **Long format:** one observation per row
- **CSV file(s):** single or multiple files accepted

**Required fields**
- Organisation unit (facility + hierarchy)
- Period (e.g., 2023-07)
- Indicator or data element
- Reported value
- Date extracted

</div>

</div>

---
## Data format and granularity
<br>

![hmis_data_raw](../../assets/screenshots/hmis-csv-required-fields.png)

---
## How Much Data?

### Initial FASTR analysis

For a first run, we recommend extracting around **five years of historical data**.
This length provides enough information to understand long-term trends, seasonal patterns, and underlying variation.

The exact period may vary depending on:
- How far back reliable DHIS2 data are available
- Whether indicator definitions or reporting practices changed
- The stability of the routine information system

The goal is to include enough history to establish a solid baseline for trends and seasonality.


---

## How Much Data? (continued)

### Routine updates to the FASTR analysis

For each new run, you do **not** need to re-download the full historical dataset.
Instead, update only the period that is new or likely to have changed.

A practical approach is to:
- Download the **new months** not yet in your dataset
- Include a **buffer of recent months** (often the last 2–3 months) because DHIS2 values may change due to late reporting or corrections

If there are signs of major historical revisions or indicator changes, you can always re-download a longer period to ensure consistency.

---
