---
marp: true
theme: fastr
paginate: true
---


# FASTR Workshop - Nigeria

**January 10-15, 2026** | **Lagos**

*TBD*

<img src="../assets/logos/FASTR_Primary_01_FullName.png" style="position: absolute; bottom: 40px; right: 40px; width: 180px;">

---


# Workshop Agenda

**Day 1**

| Time | Session |
|------|--------|
| 9:00 AM | **Welcome & Introductions** |
| 9:15 AM | **Identify Questions & Indicators** |
| 10:30 AM | *Tea Break* |
| 10:45 AM | **Data Extraction** |

**Day 2**

| Time | Session |
|------|--------|
| 9:00 AM | **Welcome & Introductions** |
| 9:15 AM | **The FASTR Data Analytics Platform** |
| 10:30 AM | *Tea Break* |

**Day 3**

| Time | Session |
|------|--------|
| 9:00 AM | **Welcome & Introductions** |
| 9:15 AM | **Data Quality Assessment** |
| 10:30 AM | *Tea Break* |

**Day 4**

| Time | Session |
|------|--------|
| 9:00 AM | **Welcome & Introductions** |
| 9:15 AM | **Data Quality Adjustment** |
| 10:30 AM | *Tea Break* |

**Day 5**

| Time | Session |
|------|--------|
| 9:00 AM | **Welcome & Introductions** |
| 9:15 AM | **Data Analysis** |
| 10:30 AM | *Tea Break* |

---



## Introduction to FASTR: Gaps and Challenges

*Content to be developed*

This section will cover:
- Identifying gaps and challenges that FASTR is well suited to support
- How FASTR serves as an entry point to reduce fragmentation
- Starting the conversation with government stakeholders

---



## Development of a Data Use Case

*Content to be developed*

This section will cover:
- Co-creation workshop approach with MoH and stakeholders
- Data use case development guidance
- Example use cases from country implementations

---



## Defining Priority Questions and Selecting Indicators

*Content to be developed*

This section will cover:
- How to define priority questions for FASTR analysis
- Criteria for selecting indicators
- What makes a good FASTR indicator
- Aligning indicators with national strategies

---



## Preparing for Data Extraction

*Content to be developed*

This section will cover:
- Pre-extraction checklist
- Understanding your DHIS2 configuration
- Mapping indicators to data elements
- Planning your extraction timeline

---


# Lunch Break

**60 minutes**

We'll resume at 12:30 PM

---

# See You Tomorrow!

**Day 1 Complete**

We resume tomorrow at **9:00 AM**

**Tomorrow:** Data Extraction, FASTR Analytics Platform

---


## Why Extract Data?

### Why Extract Data from DHIS2? Why not analyse directly inside DHIS2?

**The FASTR Analytics Platform applies data quality adjustments**

The FASTR methodology includes specific approaches to:
- Identify and adjust for outliers
- Adjust for incomplete reporting
- Apply consistent data quality metrics

These adjustments require processing that cannot be done within DHIS2's native analytics.

### What Format and Granularity is Required?

Data should be extracted at the **facility-month level** to enable:
- Facility-level data quality assessment
- Subnational disaggregation of results
- Longitudinal trend analysis

---



## Tools for Data Extraction

*Content to be developed*

This section will cover:
- DHIS2 data export options
- API-based extraction methods
- Data transformation requirements
- Quality checks on extracted data

---


# Tea Break

**15 minutes**

We'll resume at 10:30 AM

---


## Overview of the Platform

*Content to be developed*

This section will cover:
- Introduction to the FASTR analytics platform
- Key features and capabilities
- How the platform supports the FASTR methodology

---



## Accessing the Platform

*Content to be developed*

This section will cover:
- Creating accounts
- Signing in
- User permissions and roles

---



## Setting Up the Structure

*Content to be developed*

This section will cover:
- Configuring admin areas (regions, districts)
- Setting up facilities
- Defining indicators

---



## Importing a Dataset

*Content to be developed*

This section will cover:
- Data format requirements
- Import process
- Validation and error handling

---



## Installing and Running Modules

*Content to be developed*

This section will cover:
- Available analysis modules
- Module installation
- Running analyses

---



## Creating a New Project

*Content to be developed*

This section will cover:
- Project setup workflow
- Configuration options
- Best practices

---



## Creating Visualizations

*Content to be developed*

This section will cover:
- Available chart types
- Customization options
- Exporting visualizations

---



## Creating Reports

*Content to be developed*

This section will cover:
- Report templates
- Automated report generation
- Customizing reports

---


# Lunch Break

**60 minutes**

We'll resume at 12:30 PM

---

# See You Tomorrow!

**Day 2 Complete**

We resume tomorrow at **9:00 AM**

**Tomorrow:** Data Quality Assessment, Data Quality Adjustment

---


## Data Quality Assessment

Understanding the reliability of routine health data

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

## Completeness: FASTR Output

![Indicator Completeness](../../resources/default_outputs/Default_2._Proportion_of_completed_records.png)

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

![Outliers](../../resources/default_outputs/Default_1._Proportion_of_outliers.png)

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

![Internal Consistency](../../resources/default_outputs/Default_4._Proportion_of_sub-national_areas_meeting_consistency_criteria.png)

---



## Putting It All Together: Overall Data Quality

---

## Overall Quality Score

**For each facility and month, we combine all three checks:**

**Complete:** Did the facility report?
**No outliers:** Are the numbers reasonable?
**Consistent:** Do related numbers make sense?

**If all three pass -> Quality Score = 1 (good quality)**
**If any fail -> Quality Score = 0 (quality issue)**

**This score helps us:**
- Decide which data to use for analysis
- Identify facilities that need support
- Track if data quality is improving over time

---

## Overall DQA Score: FASTR Output

![Overall DQA Score](../../resources/default_outputs/Default_5._Overall_DQA_score.png)

---

## Mean DQA Score: FASTR Output

![Mean DQA Score](../../resources/default_outputs/Default_6._Mean_DQA_score.png)

---


# Tea Break

**15 minutes**

We'll resume at 10:30 AM

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

---



## Adjustment for Outliers

For each value flagged as an outlier, the module calculates what the value "should have been" based on that facility's historical pattern.

**Methods used (in order of preference):**
1. Average of 3 months before and 3 months after
2. Same month from the previous year (for seasonal indicators)
3. Facility-specific historical average

---

### Outlier Adjustment: FASTR Output

![Percent change in volume due to outlier adjustment.](../../resources/default_outputs/Default_1._Percent_change_in_volume_due_to_outlier_adjustment.png)

Heatmap showing percent change in service volumes due to outlier replacement.

---



## Adjustment for Completeness

For months where data is missing or marked as incomplete, the module imputes (fills in) values using the same rolling average approach.

This ensures that temporary reporting gaps don't create artificial drops to zero in the data.

---

### Completeness Adjustment: FASTR Output

![Percent change in volume due to completeness adjustment.](../../resources/default_outputs/Default_2._Percent_change_in_volume_due_to_completeness_adjustment.png)

Heatmap showing percent change in service volumes due to missing data imputation.

---


# Lunch Break

**60 minutes**

We'll resume at 12:30 PM

---

# See You Tomorrow!

**Day 3 Complete**

We resume tomorrow at **9:00 AM**

**Tomorrow:** Data Analysis

---


## Service Utilization Analysis

The Service Utilization module (Module 3 in the FASTR analytics platform) analyzes health service delivery patterns to detect and quantify disruptions in service volumes over time.

**Key capabilities:**
- Identifies when health services deviate significantly from expected patterns
- Measures magnitude of disruptions at national, provincial, and district levels
- Distinguishes normal fluctuations from genuine disruptions requiring investigation

---

### Two-Stage Analysis Process

**Stage 1: Control Chart Analysis**
- Model expected patterns using historical trends and seasonality
- Detect significant deviations from expected volumes
- Flag disrupted periods

**Stage 2: Disruption Quantification**
- Use panel regression to estimate service volume changes
- Calculate shortfalls and surpluses in absolute numbers

---



## Surplus and Disruption Analyses

The module detects multiple types of service disruptions:

| Disruption Type | Description |
|----------------|-------------|
| **Sharp disruptions** | Single months with extreme deviations |
| **Sustained drops** | Gradual declines over several months |
| **Sustained dips** | Periods consistently below expected levels |
| **Sustained rises** | Periods consistently above expected levels |
| **Missing data patterns** | Gaps in reporting that may signal problems |

---

### Quantifying Impact

Disruption analysis quantifies shortfalls and surpluses by comparing:
- **Predicted volumes** (what would have happened without disruption)
- **Actual volumes** (what was observed)

Results are reported in absolute numbers and percentages at each geographic level.

---



## Service Coverage Estimates

This module estimates health service coverage by answering: **"What percentage of the target population received this health service?"**

**Three data sources integrated:**
1. Adjusted health service volumes from HMIS
2. Population projections from United Nations
3. Household survey data from MICS/DHS

---

### Two-Part Process

**Part 1: Denominator Calculation**
- Calculate target populations using multiple methods (HMIS-based and population-based)
- Compare against survey benchmarks
- Automatically select best denominator for each indicator

**Part 2: Coverage Estimation**
- Override automatic selections based on programmatic knowledge
- Project survey estimates forward using HMIS trends
- Generate final coverage estimates

---


# Tea Break

**15 minutes**

We'll resume at 10:30 AM

---


# Next Steps & Action Items

---

## Immediate Actions (Next 2 Weeks)

- [ ] **[Action 1]** - e.g., Share preliminary findings with MOH
- [ ] **[Action 2]** - e.g., Request additional data for [specific gap]
- [ ] **[Action 3]** - e.g., Schedule follow-up meeting

**Responsible:** [Names/Teams]

---

## Short-term Actions (Next 3 Months)

1. **Data quality improvements**
   - [Specific action]
   - [Specific action]

2. **Capacity building**
   - [Training need]
   - [Support required]

3. **Integration with planning**
   - [How findings will be used]

---

## Long-term Recommendations

- **Routine updates:** [Frequency of FASTR refresh]
- **System strengthening:** [Key improvements needed]
- **Institutionalization:** [How to make this sustainable]

---

## Questions & Discussion

**Contact:** fastr@worldbank.org

**Resources:** https://fastr.org

---


# Thank You!

## Questions & Discussion

---

# Contact Information

**FASTR Team**

📧 Email: fastr@worldbank.org
🌐 Website: https://fastr.org

---

