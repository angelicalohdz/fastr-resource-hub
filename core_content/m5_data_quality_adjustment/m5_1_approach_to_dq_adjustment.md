---
marp: true
theme: fastr
paginate: true
---
# Data Adjustment

Fixing data quality issues to enable reliable analysis

---

## What Do We Do About Quality Issues?

---

## Two Options: Accept or Adjust

**Option 1: Just report the quality issues**
- Show which data has problems
- Let users decide whether to use it
- Be transparent about limitations

**Option 2: Try to fix the problems statistically**
- Replace bad values with estimates
- Fill in missing reports
- Produce "cleaned" datasets

**FASTR does both** - we report quality issues AND provide adjusted datasets, so users can choose.

---

## Four Versions of the Data

**To give users flexibility, we create four versions:**

1. **Original (no changes):** Raw data as reported
2. **Outliers fixed:** Only extreme values replaced
3. **Missing filled:** Only gaps filled in
4. **Both fixed:** Outliers replaced AND gaps filled

**Why four versions?**
- You can see the impact of adjustments
- Choose the version that makes sense for your analysis
- Transparency about what was changed

**Most common choice:** Version 4 (both adjustments) for cleanest analysis

---

## Real-World Example: Comparing Versions

**Province Y - Institutional Deliveries (Q1 totals):**

| Version | Total Deliveries | Difference |
|---------|------------------|------------|
| Original (no changes) | 12,450 | Baseline |
| Outliers fixed | 11,890 | -560 (outliers removed) |
| Missing filled | 13,210 | +760 (gaps filled) |
| Both fixed | 12,650 | +200 (net effect) |

**Interpretation:** Outliers were inflating the total, but missing reports were deflating it. The "both fixed" version is probably closest to reality.

---

## Volume Change: FASTR Output

![Volume Change Due to DQ Adjustments](../../assets/fastr-outputs/m2_Volume_change_due_to_data_quality_adjustments.png)

---

## Service Volume Trends: FASTR Output

![Service Volume by Year](../../assets/fastr-outputs/m2_Change_in_service_volume_(Admin_area_2).png)

---
