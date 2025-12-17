---
marp: true
theme: fastr
paginate: true
---

# Tools for Data Extraction

---

## Direct Import from DHIS2

The **Direct Import** option is the simplest and most reliable way to bring DHIS2 data into the FASTR Analytics Platform.
It connects securely to your country's DHIS2 server, retrieves the selected indicators, and automatically reshapes the data into the structure required for analysis.

**What the platform takes care of:**
- API authentication
- Retrieving facility-level monthly data
- Reshaping to the correct long format
- Validating fields before analysis

> **Live demo coming next**
> We will walk through the Direct Import workflow step by step.

---

## Other Options for Extracting DHIS2 Data

FASTR has also developed tools that countries may use if they prefer to prepare their data before uploading it to the platform.

**Available tools include:**
- **FASTR DHIS2 Data Downloader**
  A guided interface for selecting indicators, time periods, and administrative levels, producing ready-to-upload CSVs.

- **FASTR API Script (Google Colab)**
  A script-driven option for automated or large-scale extraction.

Countries can choose whichever approach fits their workflow.
Both tools produce CSVs that are compatible with the FASTR platform when correctly structured.

---
