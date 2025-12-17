---
marp: true
theme: fastr
paginate: true
---

## Question 2: Are Numbers Reasonable?

---

## Outliers: Spotting Suspicious Numbers

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

## How We Spot Outliers

**We use two checks:**

**Check 1: Is this value much higher than usual for this facility?**
- Look at the facility's typical monthly values
- If one month is extremely different, flag it

**Check 2: Does one month account for most of the year's total?**
- If March has 80% of the facility's annual deliveries, something's wrong
- Services should be spread more evenly across months

**Both checks together** help us find data entry errors or reporting problems.

---

## Outlier Example

**Health Center B - Malaria Tests:**

| Month | Tests Reported | Normal? |
|-------|----------------|---------|
| January | 245 | Normal |
| February | 267 | Normal |
| **March** | **2,890** | **Outlier** |
| April | 256 | Normal |

**What happened?** Probably someone entered "2890" instead of "289" (extra zero)

**Impact if we don't fix it:** March would show a huge "spike" in malaria that didn't really happen.

---

## Outliers: FASTR Output

![Outliers](../../shared assets/fastr-outputs/m1_Proportion_of_outliers.png)

---
