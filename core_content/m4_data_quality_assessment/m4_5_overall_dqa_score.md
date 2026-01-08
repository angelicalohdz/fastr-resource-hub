---
marp: true
theme: fastr
paginate: true
---

## Putting it all together: Overall data quality

---

## Overall quality score

**For each facility and month, we combine all three checks:**

**Complete:** Did the facility report?
**No outliers:** Are the numbers reasonable?
**Consistent:** Do related numbers make sense?

**Binary DQA Score:**
- dqa_score = 1 if all consistency pairs pass
- dqa_score = 0 if any consistency pair fails

**DQA Mean:** Average of completeness-outlier score and consistency score

**This score helps us:**
- Decide which data to use for analysis
- Identify facilities that need support
- Track if data quality is improving over time

---

## Overall DQA score: FASTR output

![Overall DQA Score](../../resources/default_outputs/Default_5._Overall_DQA_score.png)

---

## Mean DQA score: FASTR output

![Mean DQA Score](../../resources/default_outputs/Default_6._Mean_DQA_score.png)
