---
marp: true
theme: fastr
paginate: true
---

## Approach to Data Quality Adjustment

The Data Quality Adjustment module (Module 2 in the FASTR analytics platform) systematically corrects two common problems in routine health facility data:

1. **Outliers** - extreme values caused by reporting errors or data entry mistakes
2. **Missing data** - from incomplete reporting

Rather than simply deleting problematic data, this module replaces questionable values with statistically sound estimates based on each facility's own historical patterns.

---

### Four Adjustment Scenarios

The module produces four parallel versions of the data:

| Scenario | Description |
|----------|-------------|
| **None** | Original data, no adjustments |
| **Outliers only** | Only outlier corrections applied |
| **Completeness only** | Only missing data filled in |
| **Both** | Both types of corrections applied |

This allows analysts to understand how sensitive their results are to different data quality assumptions.
