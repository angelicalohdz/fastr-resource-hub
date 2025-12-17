---
marp: true
theme: fastr
paginate: true
---

# Adjustment for Outliers

---

## How We Adjust Data

**For outliers (suspiciously high values):**
- Don't just delete them
- **Replace with the facility's typical value**
- Use the average of surrounding months

**Example:**
- Feb: 80 deliveries
- **Mar: 450 deliveries** (outlier)
- Apr: 85 deliveries

**Adjusted March value:**  Average of Feb and Apr = 83 deliveries

This preserves the facility's pattern while removing the data error.

---

## Common Questions

---

## "Why not just fix all the problems in DHIS2?"

**We do both!**

**Long-term solution:** Improve data quality at the source
- Training, supervision, better systems
- This is the goal - takes time

**Short-term solution:** Statistical adjustments
- Enables analysis with current data
- Fills gaps while quality improves
- Provides feedback to guide improvements

**FASTR helps with both** - identifies problems for fixing AND enables analysis despite problems.

---

## "How do we know the adjustments are right?"

**We don't claim they're perfect, but they're better than the alternatives:**

**Alternative 1: Use raw data with errors**
- Outliers skew results
- Missing data creates false drops
- Decisions based on bad data

**Alternative 2: Throw out all problem data**
- Lose too much information
- Can't analyze anything
- No basis for decisions

**FASTR approach: Make reasonable estimates**
- Based on facility's own pattern
- Transparent about what was changed
- Provide multiple versions for comparison

---
