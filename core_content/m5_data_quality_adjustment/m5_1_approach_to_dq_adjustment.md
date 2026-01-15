---
marp: true
theme: fastr
paginate: true
---

## Approach to data quality adjustment

The FASTR analytics platform provides an option for adjusting data for outliers, indicator completeness, or both.

---

## Adjustment for outliers

The FASTR approach makes adjustment to service volume to replace outlier values (recommended).

Each individual outlier is replaced by the mean volume, excluding any outlier values, of services delivered for the same indicator and the same month but amongst facilities of the same type within the same admin area (province, district, and/or state).

---

## Adjustment for completeness

The FASTR approach allows for adjustment to service volume to replace missing/incomplete values (optional).

Each incomplete/missing value is replaced by the mean volume of services delivered for the same indicator and same facility, calculated as a rolling average of the 12 months surrounding the missing point and excluding any outliers or missing values.
