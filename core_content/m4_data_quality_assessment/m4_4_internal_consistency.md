---
marp: true
theme: fastr
paginate: true
---

## Question 3: Do Related Numbers Match Up?

---

## Consistency: Do Related Services Make Sense Together?

**What we're checking:**
Health services are related - certain patterns are expected.

**Example 1 - ANC visits:**
- More women should get their **1st** ANC visit (ANC1)
- Fewer should complete all **4** visits (ANC4)
- We expect: ANC1 >= ANC4

**Example 2 - Vaccinations:**
- More babies should get their **1st** Penta dose (Penta1)
- Fewer should complete all **3** doses (Penta3)
- We expect: Penta1 >= Penta3

**If these relationships are backwards, something's wrong with the data.**

---

## Why Check Consistency at District Level?

**Patients move between facilities:**
- Woman might get ANC1 at Health Center A
- But deliver at District Hospital B
- If we only look at each facility separately, numbers might not match

**Solution:** Check consistency at district level
- Add up all ANC1 visits in the district
- Add up all ANC4 visits in the district
- Compare the totals

This accounts for patients visiting different facilities for different services.

---

## Consistency Example

**District X - ANC Services:**

| Indicator | District Total | Expected Relationship |
|-----------|----------------|----------------------|
| ANC1 | 5,200 visits | Should be higher |
| ANC4 | 4,100 visits | Should be lower |

**This passes the consistency check** - more women started ANC (5,200) than completed 4 visits (4,100).

**If it was reversed** (more ANC4 than ANC1), we'd know there's a data quality problem.

---

## Consistency: FASTR Output

![Internal Consistency](../../shared assets/fastr-outputs/m1_Proportion_of_sub-national_areas_meeting_consistency_criteria.png)

---
