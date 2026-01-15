---
marp: true
theme: fastr
paginate: true
---

## Approach to data quality adjustment

The FASTR analytics platform provides an option for adjusting data for outliers, indicator completeness, or both.

---

## Adjustment for outliers

Each outlier is replaced using the facility's own historical data through a **6-month rolling average**.

**Method depends on position in time series:**

| Position | Method | Example (outlier in June) |
|----------|--------|---------------------------|
| **Middle** | Centered average | Average of Mar-Apr-May + Jul-Aug-Sep |
| **End** | Backward average | Average of Jan-Feb-Mar-Apr-May-Jun (excluding outlier) |
| **Start** | Forward average | Average of Jul-Aug-Sep-Oct-Nov-Dec |

If rolling averages unavailable: same month from previous year, then facility mean.

---

## Adjustment for completeness

Missing values are imputed using the same 6-month rolling average approach.

**Method depends on position in time series:**

| Position | Method | Example (missing in June) |
|----------|--------|---------------------------|
| **Middle** | Centered average | Average of Mar-Apr-May + Jul-Aug-Sep |
| **End** | Backward average | Average of Jan-Feb-Mar-Apr-May |
| **Start** | Forward average | Average of Jul-Aug-Sep-Oct-Nov-Dec |

This prevents reporting gaps from creating artificial drops to zero.
