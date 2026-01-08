---
marp: true
theme: fastr
paginate: true
---

## Question 2: Are numbers reasonable?

---

## Outliers: Spotting suspicious numbers

**What we're checking:**
Are there any values that seem way too high compared to what that facility normally reports?

**Real example:**
- Health Center A normally reports 20-25 deliveries per month
- In March, they reported 450 deliveries
- **This is likely a data entry error** (maybe they typed an extra digit, or reported cumulative instead of monthly)

**Why it matters:**
- One extreme value can make it look like there was a huge service increase
- Skews totals and trends for the whole district or province

---

## How we spot outliers

Outliers are identified by assessing the within-facility variation in monthly reporting for each indicator.

A value is flagged as an outlier if it meets EITHER of two criteria:

1. A value greater than 10 times the Median Absolute Deviation (MAD) from the monthly median value for the indicator, OR
2. A value for which the proportional contribution in volume for a facility, indicator, and time period is greater than 80%

AND for which the count is greater than 100.

---

## Outlier example

**Health Center B - Malaria tests:**

| Month | Tests Reported | Normal? |
|-------|----------------|---------|
| January | 245 | Normal |
| February | 267 | Normal |
| **March** | **2,890** | **Outlier** |
| April | 256 | Normal |

**What happened?** Probably someone entered "2890" instead of "289" (extra zero)

**Impact if we don't fix it:** March would show a huge "spike" in malaria that didn't really happen.

---

## Outliers: FASTR output

![Outliers](../../resources/default_outputs/Default_1._Proportion_of_outliers.png)
