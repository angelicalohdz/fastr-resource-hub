---
marp: true
theme: fastr
paginate: true
---
# Data Quality: Assessment & Adjustment

Understanding and improving the reliability of routine health data

---
## Why Talk About Data Quality?

**The challenge:** Health facilities report data every month, but sometimes:
- Numbers seem too high or too low
- Facilities forget to report
- Related numbers don't match up

**The impact:** Bad data leads to bad decisions
- We might think services are improving when they're not
- We might miss real problems in certain areas
- Resources might go to the wrong places

**FASTR's solution:** Check data quality systematically, fix what we can, and be transparent about limitations

---
## Three Simple Questions About Data Quality

**1. Are facilities reporting regularly?**
- Completeness: Did we get reports from facilities this month?

**2. Are the numbers reasonable?**
- Outliers: Are there any suspiciously high values?

**3. Do related numbers make sense together?**
- Consistency: Do related services show expected patterns?

These three questions help us understand if we can trust the data for decision-making.

---

## Question 1: Are Facilities Reporting?

---

## Completeness: Did We Get Reports?

**What we're checking:**
Each month, are facilities sending in their reports?

**Example:**
- District has 20 health centers
- In March, only 15 sent ANC data
- **Completeness = 75%** (15 out of 20 reported)

**Why it matters:**
- If many facilities don't report, we're missing part of the picture
- Trends might look like services dropped, when really facilities just didn't report

---

## What's Good Completeness?

**It depends on your health system:**
- 90%+ is excellent
- 80-90% is good
- Below 80% means we're missing a lot of information

**Important:** Even 100% completeness doesn't mean we have the full picture - some services might happen outside facilities or some facilities might not be in the reporting system.

**What to look for:** Is completeness improving over time? Which areas have low completeness?

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
| January | 245 | ✓ Normal |
| February | 267 | ✓ Normal |
| **March** | **2,890** | ✗ **Outlier** |
| April | 256 | ✓ Normal |

**What happened?** Probably someone entered "2890" instead of "289" (extra zero)

**Impact if we don't fix it:** March would show a huge "spike" in malaria that didn't really happen.

---

## Question 3: Do Related Numbers Match Up?

---

## Consistency: Do Related Services Make Sense Together?

**What we're checking:**
Health services are related - certain patterns are expected.

**Example 1 - ANC visits:**
- More women should get their **1st** ANC visit (ANC1)
- Fewer should complete all **4** visits (ANC4)
- We expect: ANC1 ≥ ANC4

**Example 2 - Vaccinations:**
- More babies should get their **1st** Penta dose (Penta1)
- Fewer should complete all **3** doses (Penta3)
- We expect: Penta1 ≥ Penta3

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
| ANC1 | 5,200 visits | Should be higher ✓ |
| ANC4 | 4,100 visits | Should be lower ✓ |

**This passes the consistency check** - more women started ANC (5,200) than completed 4 visits (4,100).

**If it was reversed** (more ANC4 than ANC1), we'd know there's a data quality problem.

---

## Putting It All Together: Overall Data Quality

---

## Overall Quality Score

**For each facility and month, we combine all three checks:**

✓ **Complete:** Did the facility report?
✓ **No outliers:** Are the numbers reasonable?
✓ **Consistent:** Do related numbers make sense?

**If all three pass → Quality Score = 1 (good quality)**
**If any fail → Quality Score = 0 (quality issue)**

**This score helps us:**
- Decide which data to use for analysis
- Identify facilities that need support
- Track if data quality is improving over time

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

## How We Fill Missing Data

**For missing reports:**
- Don't leave them as zero (that would make it look like services stopped)
- **Estimate what the value probably was**
- Use the facility's typical value from nearby months

**Example:**
- Jan: 45 malaria tests
- **Feb: No report (missing)**
- Mar: 48 malaria tests

**Estimated February value:** Average of nearby months ≈ 47 tests

This prevents gaps from creating false "drops" in service delivery.

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

## How to Use Data Quality Information

---

## For Program Managers

**Three questions to ask:**

1. **Can we trust this data for decision-making?**
   - Check the quality scores for your area
   - If most months have good quality → yes, use it
   - If quality is poor → dig deeper before making decisions

2. **Which areas need data quality support?**
   - Low completeness → facilities need reporting support
   - Many outliers → need better data entry or validation
   - Consistency problems → need training on indicator definitions

3. **Is data quality improving?**
   - Track quality scores over time
   - See if interventions (training, digitization) are working

---

## For Data Analysts

**How to use the quality outputs:**

**For analysis:**
- Use the adjusted datasets (version 4 typically)
- Filter to high-quality months if needed
- Report which version you used

**For data quality improvement:**
- Share outlier lists with facilities for correction
- Identify facilities with chronic quality problems
- Prioritize areas for in-person data quality assessments

**For reporting:**
- Always mention data quality caveats
- Show before/after adjustment comparisons
- Be transparent about limitations

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

## "What if our data quality is really bad?"

**FASTR can still help:**

**First: Understand HOW bad**
- The assessment shows exactly where problems are
- Completeness, outliers, consistency by area and indicator
- This guides improvement efforts

**Second: Use what you can**
- Even partial data is better than no data
- Focus on areas/indicators with better quality
- Track improvement over time

**Third: Set realistic expectations**
- Coverage estimates will have more uncertainty
- Trend directions still useful even if exact numbers uncertain
- Transparency about limitations builds trust

---

## Key Takeaways

---

## Remember These Points

**1. Data quality matters for decision-making**
- Bad data → bad decisions
- Systematic checking prevents mistakes

**2. Three simple dimensions to check**
- Completeness: Are facilities reporting?
- Outliers: Are numbers reasonable?
- Consistency: Do related numbers match?

**3. We can both report and adjust**
- Transparency about problems
- Statistical fixes where appropriate
- Multiple versions for flexibility

**4. Use quality information strategically**
- For analysis: Choose appropriate data version
- For improvement: Target support where needed
- For reporting: Be transparent about limitations

---

## What's Next?

**Now that we have quality-assessed and adjusted data, we can:**

**Module 3: Analyze service delivery trends**
- Detect disruptions in services
- Quantify shortfalls and surpluses
- Monitor health system performance

**Module 4: Estimate population coverage**
- What percentage of people are being reached?
- Are we meeting targets?
- Where are the gaps?

**The data quality work enables everything else!**

---
