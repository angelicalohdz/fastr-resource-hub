---
marp: true
theme: fastr
paginate: true
---


# In-Country Working Session: FASTR Implementation & RMNCAH-N Service Monitoring Analysis

**January 27-30, 2026** | **Lusaka**

*GFF FASTR Team*

<img src="../resources/logos/FASTR_Primary_01_FullName.png" style="position: absolute; bottom: 40px; right: 40px; width: 180px;">

---


<!-- _class: agenda -->
# Agenda

**Day 1 -- Laying the Foundation: Introducing FASTR and Configuring the Analytics Platform**

| Time | Agenda | Facilitator/Presenter |
|------|--------|--------|
| **Opening Session** | | |
| 08:30-09:00 | Participant registration | MoH team |
| 09:00-09:10 | Welcome and opening remarks | MoH team |
| 09:10-09:20 | Icebreakers/Introductions | MoH team |
| 09:20-09:35 | Overview of agenda, workshop objectives | GFF FASTR team |
| **Session 1: Overview of the FASTR approach** | | |
| 09:35-10:30 | Overview: FASTR Approaches | GFF FASTR team |
| **Session 2: HMIS data extraction** | | |
| 10:30-11:30 | Data extraction: Rationale and methods | GFF FASTR team |
| **Session 3: Introduction to the FASTR analytics platform** | | |
| 11:30-12:30 | Introduction to the FASTR analytics platform | GFF FASTR team |
| 12:30-14:00 | *Lunch Break* | |
| 14:00-14:30 | Getting participants into the platform | GFF FASTR team |
| **Session 4: Configuring the FASTR analytics platform** | | |
| 14:30-16:30 | Configuring the analysis platform | GFF FASTR team |
| 16:30-17:00 | Key messages and wrap-up |  |

---

<!-- _class: agenda -->
# Agenda

**Day 2 -- Building the Analysis: Applying FASTR Methods and Generating Outputs**

| Time | Agenda | Facilitator/Presenter |
|------|--------|--------|
| 09:00-09:15 | Overview of Day 2 agenda | GFF FASTR team |
| **Session 5: Overview of FASTR methods and analytical outputs** | | |
| 09:15-10:15 | Data quality, service utilization, coverage | GFF FASTR team |
| **Session 6: Creating a project** | | |
| 10:15-11:15 | Project creation and settings | GFF FASTR team |
| **Session 7: Creating visualizations** | | |
| 11:15-12:30 | Creating and editing visualizations | GFF FASTR team |
| 12:30-14:00 | *Lunch Break* | |
| **Session 8: Creating reports** | | |
| 14:30-16:30 | Practice creating and editing reports | GFF FASTR team |
| 16:30-17:00 | Key messages and wrap-up |  |

---

<!-- _class: agenda -->
# Agenda

**Day 3 -- From Analysis to Action: Interpreting Results and Using FASTR for Decision-Making**

| Time | Agenda | Facilitator/Presenter |
|------|--------|--------|
| 09:00-09:15 | Overview of Day 3 agenda | GFF FASTR team |
| **Session 8: Interpretation of visualizations** | | |
| 09:15-10:15 | Approaches to support interpretation | GFF FASTR team |
| **Session 9: Creating a Q4 2025 report** | | |
| 10:15-12:30 | Creating short and long reports with country context | GFF FASTR team |
| 12:30-14:00 | *Lunch Break* | |
| **Session 9 (cont'd): Creating a Q4 2025 report** | | |
| 14:00-15:00 | Continue report creation with country context | GFF FASTR team |
| **Session 10: Presenting reports** | | |
| 14:30-15:30 | Present reports, group feedback | GFF FASTR team |
| **Session 11: Action planning** | | |
| 15:30-16:30 | Activity: Action planning | GFF FASTR team |
| 16:30-17:00 | Key messages and wrap-up |  |

---

<!-- _class: agenda -->
# Agenda

**Day 4 -- Designing the Health Facility Assessment**

| Time | Agenda | Facilitator/Presenter |
|------|--------|--------|
| 09:00-09:15 | Overview of Day 4 agenda | GFF FASTR team |
| **Session 12: Overview of FASTR HFA phone survey** | | |
| 09:15-10:15 | HFA overview and questionnaire adaptation guidelines | GFF FASTR team |
| **Session 13: Questionnaire adaptation to the Zambian context** | | |
| 10:15-12:30 | Review questionnaire + hands-on adaptation | GFF FASTR team |
| 12:30-14:00 | *Lunch Break* | |
| **Session 14: Questionnaire adaptation (cont'd)** | | |
| 14:00-15:00 | Continue questionnaire adaptation (in groups) | GFF FASTR team |
| **Session 15: Discussion: HFA adapted questionnaire** | | |
| 14:30-15:30 | Discuss adapted questionnaire in plenary | GFF FASTR team |
| **Session 16: Discussion: HFA priorities and data use** | | |
| 15:30-16:30 | HFA priorities and data use case in Zambia | GFF FASTR team |
| 16:30-17:00 | Key messages and wrap-up |  |

---



# Workshop Objectives

- Prepare MoH for participation in the multi-country workshop
- Strengthen capacity for disruption analysis and data extraction
- Configure the FASTR analytics platform for Zambia
- Produce the first quarterly report
- Adapt the phone survey questionnaire to the Zambian context
- Use data downloader tools for DHIS2

---



# Scope of Work

### Disruption Analysis Activities
- Data extraction and configuration of analytics platform
- Produce first quarterly report
- Review results and contextualize findings (with relevant program teams)

### Phone Survey Activities
- Adaptation of questionnaire (with program input)

### Capacity Building
- Training on data downloader for all with DHIS2 access
- Hybrid format: face-to-face and online

---



# Expected Outputs

- Adapted phone survey questionnaire
- First quarterly report draft
- Trained MoH team on data downloader tools
- Roadmap for participation in Abuja workshop

---


# Session 1: Overview of the FASTR approach

---


## Introduction to FASTR

<div class="columns">
<div>

The Global Financing Facility (GFF) supports country-led efforts to strengthen the use of timely data for decision-making, with the goal of improving primary healthcare (PHC) performance and RMNCAH-N outcomes.

**Frequent Assessments and Health System Tools for Resilience (FASTR)** is the GFF's rapid-cycle analytics framework for monitoring health system performance using high-frequency data.

FASTR brings together four complementary technical approaches:

1. Routine HMIS data analysis
2. Health facility phone surveys
3. High-frequency household phone surveys
4. Follow-on, problem-driven analyses

</div>
<div>

![FASTR Technical Approaches](../resources/diagrams/Technical-Rapid-cycle-analytics--V3.svg)

</div>
</div>

---



## What FASTR does with routine HMIS data

<div class="columns">
<div>

FASTR works directly with Ministries of Health to transform routine HMIS data into actionable evidence for policy and program management.

Using facility-level data, the approach focuses on three core analytic functions:

**Assess data quality**
Identify key issues related to completeness, outliers, and internal consistency.

**Adjust for data quality limitations**
Apply transparent, indicator-specific methods to improve the reliability of trend analysis.

**Analyze service use and coverage trends**
Track changes in priority RMNCAH-N services and compare progress against country priorities and benchmarks.

</div>
<div>

![Steps to implement RMNCAH-N service use monitoring](../resources/diagrams/Steps%20to%20implement%20RMNCAH-N%20service%20chart.svg)

</div>
</div>

---



## Why rapid-cycle analytics?

<div class="columns">
<div>

Routine health information systems are a critical source of data, but they are often underused due to concerns about data quality and long delays between data collection and analysis. Traditional household and facility surveys, while essential, are resource-intensive and infrequent.

FASTR's rapid-cycle analytics address this gap by providing:

- Timely insights aligned with country decision cycles
- Continuous learning rather than one-off assessments
- Direct feedback loops between data, analysis, and action

During the COVID-19 pandemic, this approach was applied in over 20 countries to monitor disruptions to essential RMNCAH-N services and inform response and recovery planning.

</div>
<div>

![FASTR rapid-cycle analytics framework](../resources/diagrams/GFF-Rapid-Cycle-Analytics-Data-Use_Figure-1.svg)

</div>
</div>

---



## Focus of the analysis

### Core indicators

FASTR prioritizes a core set of RMNCAH-N indicators that:

- Represent key service delivery contacts across the continuum of care
- Have relatively high reporting completeness and volumes
- Serve as proxies for broader service delivery performance

Outpatient consultations are included as a proxy for overall health service use. The indicator set can be expanded to reflect country-specific priorities.

### Core data quality metrics

Analysis is anchored in a standardized set of data quality metrics, including:

- Reporting completeness
- Extreme value (outlier) detection
- Consistency across related indicators

These metrics are summarized into an overall data quality score to support interpretation and comparison across areas.

---



## FASTR approach to routine data analysis

The FASTR approach follows a three-step workflow:

### 1. Assess data quality
Identify issues related to completeness, outliers, and internal consistency at national and subnational levels.

### 2. Adjust for data quality limitations
Apply transparent, indicator-specific corrections to improve the reliability of trend analysis.

### 3. Analyze service delivery
Quantify changes in priority service volumes and compare coverage trends against country targets.

This enables continuous, subnational monitoring while data quality is systematically improved.

---


# Session 2: HMIS data extraction

---


## Why extract data from DHIS2?

### Data quality adjustment

The FASTR approach focuses on data quality adjustments to expand the analyses countries can do with DHIS2 data and to generate more robust estimates.

The FASTR methodology includes specific approaches to:
- Identify and adjust for outliers
- Adjust for incomplete reporting
- Apply consistent data quality metrics

These adjustments require processing that cannot be done within DHIS2's native analytics.

---



## Why extract data from DHIS2?

### Analysis complexity

The FASTR approach uses more advanced statistical methods, such as regression analysis, which are not available in DHIS2. While DHIS2 can plot trends over time using raw data, FASTR can go further by:

- Identifying significant increases or decreases in service volume
- Adjusting for data quality issues
- Accounting for expected seasonal variations
- Comparing key periods, such as before and after a reform

The choice between DHIS2 and the FASTR approach should be guided by the specific purpose of your analysis.

---



## Data format and granularity

Data should be downloaded for each **indicator of interest**, at **facility level**, and **monthly** for the **period of interest**.

- Data should be saved in **long format** meaning each row represents a single observation or measurement
- Data should be saved in **.csv format** and can be saved in either a single .csv file or multiple .csv files

### Why monthly facility level data?

We want to use the most granular data we have access to in order to make more fine tuned assessments for data quality. Using monthly facility level data allows us to conduct the most robust analysis.

---



## Key variables

The data extracted should include the following required elements:

| Element | Description |
|---------|-------------|
| Org units | Organizational unit identifier |
| Period | Time period of the data |
| Indicator name | Name of the indicator |
| Total/count | The aggregated value |

---



## How much data?

### Initial FASTR analysis
- Download approximately **five years** of historical data
- Exact period depends on data availability and consistency in indicator definitions

### Routine update to FASTR analysis
- Download new data covering the most recent months not previously included (usually **three months** for quarterly implementation)
- Include the **three preceding months** as recent data is often subject to changes due to late reporting or data quality adjustments

---



## Data extraction tools

We offer two tools for bulk DHIS2 data extraction:

**API Script** (Google Colab)
- Input login credentials, specify timeframes, indicators, and administrative levels
- Download data as a .csv file

**Data Downloader**
- More intuitive, streamlined interface
- Recommended for most users

Both tools enable efficient data extraction, and we provide training resources to support their use.

---



## DHIS2 Data Downloader

The Data Downloader is a desktop application for extracting data from DHIS2.

**Key features:**
- Connect to any DHIS2 instance
- Browse and select data elements and indicators
- Download facility-level data in CSV format
- Maintain download history

**Download from GitHub:**

https://github.com/worldbank/DHIS2-Downloader/releases/

*Facilitator will demonstrate the Data Downloader*

---


# Session 3: Introduction to the FASTR analytics platform

---


## Introduction to the FASTR Analytics Platform

The FASTR analytics platform is a web-based tool for data quality assessment, adjustment, and analysis of routine health data.

**Key features:**

- Upload and analyze data from DHIS2 and other sources
- Built-in statistical methods for data quality adjustment
- User-friendly interface for running analyses
- Flexible visualization and export options

**In this session, we will provide a conceptual walkthrough of the platform and its capabilities.**

---



## Live Demo: Platform Access & Roles

**In this demo, we will:**

- Navigate to the FASTR platform
- Explore user roles: Administrator, Editor, Viewer
- Review user management and permissions
- Understand the workflow for uploading data and making analytical decisions

*Facilitator will demonstrate in the live platform*

---


# <img src="../resources/icons/lunch.png" class="icon" style="height: 1.2em; vertical-align: middle; margin-right: 0.3em;"> Lunch Break

**90 minutes**

Back at 14:00

---


# Session 4: Configuring the FASTR analytics platform

---


## Activity: Setting Up Admin Areas

**In this hands-on session, we will configure:**

- Admin areas (regions, districts)
- Facility structure
- Indicator definitions

*Participants will work directly in the platform*

---



## Activity: Importing Data

**In this hands-on session, we will:**

- Review data format requirements
- Walk through the import process
- Handle validation and error checking

*Participants will import their country's data*

---



## Activity: Installing and Running Modules

**In this hands-on session, we will:**

- Review available analysis modules
- Install required modules
- Run initial analyses

*Participants will configure and run modules on their data*

---



# Day 1 Key Messages

Today we covered:

- Overview of the FASTR approach and methodology
- Data extraction methods and tools for DHIS2
- Introduction to the FASTR Analytics Platform
- Initial platform configuration for Zambia

---

# Looking Ahead to Day 2

Tomorrow we will focus on:

- Creating your first project in the platform
- Building visualizations from your data
- Generating reports for decision-making

---


# Day 2

---


# Recap

On Day 1, we covered:

- The FASTR approach and rapid-cycle analytics methodology
- Data extraction from DHIS2 using the Data Downloader
- Introduction to the FASTR Analytics Platform
- Platform configuration: admin areas, data import, modules

---

# Day 2 Focus

Today we will:

- Explore FASTR methods for data quality and analysis
- Create and configure projects
- Build visualizations
- Generate reports

---


# Session 5: Overview of FASTR methods and analytical outputs

---


## Data quality assessment

Understanding the reliability of routine health data

---
## Why talk about data quality?

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
## Three simple questions about data quality

**1. Are facilities reporting regularly?**
- Completeness: Did we get reports from facilities this month?

**2. Are the numbers reasonable?**
- Outliers: Are there any suspiciously high values?

**3. Do related numbers make sense together?**
- Consistency: Do related services show expected patterns?

These three questions help us understand if we can trust the data for decision-making.

---



## Approach to data quality adjustment

The Data Quality Adjustment module (Module 2 in the FASTR analytics platform) systematically corrects two common problems in routine health facility data:

1. **Outliers** - extreme values caused by reporting errors or data entry mistakes
2. **Missing data** - from incomplete reporting

Rather than simply deleting problematic data, this module replaces questionable values with statistically sound estimates based on each facility's own historical patterns.

---

### Four adjustment scenarios

The module produces four parallel versions of the data:

| Scenario | Description |
|----------|-------------|
| **None** | Original data, no adjustments |
| **Outliers only** | Only outlier corrections applied |
| **Completeness only** | Only missing data filled in |
| **Both** | Both types of corrections applied |

This allows analysts to understand how sensitive their results are to different data quality assumptions.

---



## Service utilization analysis

The Service Utilization module (Module 3 in the FASTR analytics platform) analyzes health service delivery patterns to detect and quantify disruptions in service volumes over time.

**Key capabilities:**
- Identifies when health services deviate significantly from expected patterns
- Measures magnitude of disruptions at national, provincial, and district levels
- Distinguishes normal fluctuations from genuine disruptions requiring investigation

---

### Two-stage analysis process

**Part 1: Control chart analysis**
- Model expected patterns using historical trends and seasonality
- Detect significant deviations from expected volumes
- Flag disrupted periods

**Part 2: Disruption quantification**
- Use panel regression to estimate service volume changes
- Calculate shortfalls and surpluses in absolute numbers

---


# Session 6: Creating a project

---


## Activity: Creating a Project

**In this hands-on session, we will:**

- Set up a new project
- Configure project settings
- Select indicators and time periods
- Apply best practices for project organization

*Participants will create their first project*

---


# Session 7: Creating visualizations

---


## Activity: Creating Visualizations

**In this hands-on session, we will:**

- Explore available chart types
- Create and customize visualizations
- Export charts for use in reports

*Participants will build visualizations from their analysis*

---


# <img src="../resources/icons/lunch.png" class="icon" style="height: 1.2em; vertical-align: middle; margin-right: 0.3em;"> Lunch Break

**90 minutes**

Back at 14:00

---


# Session 8: Creating reports

---


## Activity: Creating Reports

**In this hands-on session, we will:**

- Use report templates
- Generate automated reports
- Customize report content and layout

*Participants will create their first quarterly report draft*

---



# Day 2 Key Messages

Today we covered:

- Overview of FASTR methods for data quality and analysis
- Creating and configuring projects
- Building visualizations from data
- Generating reports in the platform

---

# Looking Ahead to Day 3

Tomorrow we will focus on:

- Interpreting visualizations for decision-making
- Creating the Q4 2025 quarterly report
- Presenting findings effectively
- Action planning for continued use

---


# Day 3

---


# Recap

On Day 2, we covered:

- FASTR methods for data quality assessment and adjustment
- Creating and configuring projects in the platform
- Building visualizations from Zambia data
- Generating reports

---

# Day 3 Focus

Today we move from analysis to action:

- Deep dive into interpretation of results
- Create the Q4 2025 quarterly report
- Present findings to the group
- Develop action plans for continued work

---


# Session 8: Interpretation of visualizations

---


## Analytical thinking & interpretation

*Content to be developed*

This section will cover:
- Frameworks for interpreting FASTR outputs
- Connecting data patterns to programmatic meaning
- Common interpretation pitfalls to avoid
- Building analytical thinking skills

---


# Session 9: Creating a Q4 2025 report

---


## Generating quarterly reporting products

*Content to be developed*

This section will cover:
- Quarterly reporting workflow
- Using the FASTR platform for automated reports
- Quality assurance for reports
- Distribution and feedback mechanisms

---


# <img src="../resources/icons/lunch.png" class="icon" style="height: 1.2em; vertical-align: middle; margin-right: 0.3em;"> Lunch Break

**90 minutes**

Back at 14:00

---


# Session 10: Presenting reports

---


## End user mapping

End user mapping helps ensure that our outputs will meet the real needs of our end users.

### Key questions
1. **Who is my end user?**
2. **What does this end user need to accomplish with the report?**
3. **What information are they most interested in?**
4. **What do they like/not like about current reports?**
5. **How do they like to receive their information?**

---



# Next Steps & Action Planning

Key actions to take after this working session:

- Finalize adapted phone survey questionnaire
- Complete first quarterly report draft
- Train remaining MoH team on data downloader tools
- Prepare roadmap for participation in Abuja workshop

---

# Quarterly Reporting Cycle

Establish a sustainable reporting rhythm:

- Define quarterly report timeline and responsibilities
- Set up data extraction schedule
- Establish review and approval process
- Plan dissemination to stakeholders

---

# Continued Platform Usage

Maintain momentum with the FASTR platform:

- Regular data updates and quality checks
- Expanding analysis to additional indicators
- Building capacity across MoH teams
- Documentation of lessons learned

---



# Day 3 Key Messages

Today we covered:

- Interpretation of FASTR visualizations
- Creation of the Q4 2025 quarterly report
- Presentation and group feedback
- Action planning for continued platform use

---

# Looking Ahead to Day 4

Tomorrow we will focus on:

- Overview of the FASTR HFA phone survey
- Reviewing the questionnaire structure
- Adapting the questionnaire for Zambia
- Planning HFA priorities and data use

---


# Day 4

---


# Recap

On Day 3, we covered:

- Interpretation of FASTR visualizations
- Creation of the Q4 2025 quarterly report
- Presentation of findings and group feedback
- Action planning for continued platform use

---

# Day 4 Focus

Today we design the Health Facility Assessment:

- Overview of the FASTR HFA phone survey
- Review questionnaire structure
- Adapt questionnaire for Zambia context
- Plan HFA priorities and data use

---


# Session 12: Overview of FASTR HFA phone survey

---


## Health Facility Assessment Phone Survey

Complementing routine data with facility-level insights

---

## Survey Objectives

The FASTR HFA phone survey is designed to:

1. **Monitor** service availability, readiness, and functioning of PHC facilities over time (with emphasis on RMNCAH-N services)

2. **Characterize** and assess effect of shocks on PHC functioning

3. **Inform** and assess implementation of interventions for resilient PHC systems

4. **Enhance timeliness** by supplementing large-scale in-person surveys with a rapid-cycle phone approach

---

## Tool Design

**Framework alignment:**
- Aligned with WHO/UNICEF Primary Health Care Measurement Framework (2022)

**Question sources:**
- WHO Harmonized Health Facility Assessment
- WHO Service Availability and Readiness Assessment (SARA)
- World Bank Service Delivery Indicators (SDI)
- DHS Service Provision Assessment (SPA)
- USAID MOMENTUM

**Implementation:**
- Phone-based survey to facility managers/Officers in Charge
- Target duration: 30 minutes
- Quarterly contacts
- Modular design for flexibility

---

## Why phone surveys?

**Routine HMIS data tells us *what* is happening:**
- How many services were delivered
- Which facilities reported
- Where there might be data quality issues

**But HMIS data can't tell us *why*:**
- Is the facility actually open?
- Are essential supplies available?
- Are trained staff present?
- What challenges are facilities facing?

**Phone surveys fill this gap** by contacting facilities directly to understand context.

---

## What the survey covers

1. **Is the facility open and functioning?**
2. **Which services are currently available?**
3. **Are essential medicines in stock?**
4. **What staff are present today?**
5. **What challenges is the facility facing?**

Results help explain *why* routine data might show certain patterns.

---



## Questionnaire adaptation guidelines

---

## Why adapt the questionnaire?

The standard FASTR questionnaire is a **starting point**, not a final product.

**Every country needs to:**
- Translate into local language(s)
- Use local health system terminology
- Focus on nationally relevant indicators
- Adjust for local facility types
- Match local supply/medicine names

---

## Adaptation principles

**Keep what matters:**
- Core questions on operational status
- Essential supply availability
- Basic service provision

**Adapt to context:**
- Local terminology and naming
- Country-specific priority services
- Relevant response categories

**Don't add too much:**
- Phone surveys should stay short (15-30 min)
- Focus on actionable information
- Avoid "nice to know" questions

---


# Session 13: Questionnaire adaptation to the Zambian context

---


## Questionnaire structure and review

*Note: Content generated with AI - human review needed*

---

<!-- _class: compact -->
## Survey blocks

| Block | Content |
|-------|---------|
| **A** | Health Facility and Respondent Information |
| **B** | Shocks |
| **B.1** | Resilience to Shocks |
| **B.2** | Challenges in Past Three Months |
| **C** | Services |
| **D** | Infrastructure |
| **E** | Financing |
| **F** | Workforce and Staffing |
| **G** | Supplies |
| **H** | Leadership and Coordination |
| **I** | Community Engagement |
| **J** | Quality Improvement Processes |

---

## Review process

**For each block, ask:**

1. Is this question relevant for our context?
2. Is the wording clear in local language?
3. Are the response options complete?
4. Should we add country-specific items?
5. Can we remove anything non-essential?

**Goal:** A questionnaire that is locally relevant while maintaining comparability with the FASTR standard.

---



## Hands-on questionnaire adaptation

*Note: Content generated with AI - human review needed*

---

## Activity overview

**What we'll do:**
Work in groups to adapt the standard FASTR questionnaire to our country context.

**Groups:**
- Group 1: Blocks A-B (Facility info, Shocks, Resilience, Challenges)
- Group 2: Blocks C-D (Services, Infrastructure)
- Group 3: Blocks E-F (Financing, Workforce)
- Group 4: Blocks G-J (Supplies, Leadership, Community, QI)

---

## Adaptation checklist

For each question in your block:

- [ ] Is the question clear in local language?
- [ ] Are response options appropriate?
- [ ] Should we add country-specific items?
- [ ] Can we simplify without losing information?
- [ ] Does skip logic make sense?

**Document your changes** for group discussion.

---

## Group discussion

After working in groups, we'll:

1. **Present adaptations** - Each group shares key changes
2. **Discuss trade-offs** - What did we add vs. remove?
3. **Reach consensus** - Agree on final adaptations
4. **Plan pre-testing** - How will we test the adapted questionnaire?

---


# <img src="../resources/icons/lunch.png" class="icon" style="height: 1.2em; vertical-align: middle; margin-right: 0.3em;"> Lunch Break

**90 minutes**

Back at 14:00

---


# Session 16: Discussion: HFA priorities and data use

---


## HFA priorities and data use

*Note: Content generated with AI - human review needed*

---

## Using survey results

**Phone survey results should inform:**

1. **Routine data interpretation**
   - Explain patterns in HMIS data
   - Validate data quality concerns

2. **Targeted support**
   - Identify facilities needing intervention
   - Prioritize supervision visits

3. **Supply chain management**
   - Track stockout patterns
   - Inform distribution planning

---

## Linking survey to routine data

**Example use cases:**

| HMIS pattern | Survey question | Insight |
|--------------|-----------------|---------|
| Facility stopped reporting | Is facility open? | Closed vs. reporting failure |
| Sudden drop in services | Stock availability? | Stockout impact |
| Low immunization numbers | Vaccine in stock? | Supply vs. demand issue |

**Goal:** Triangulate multiple data sources for better decision-making.

---

## Next steps for HFA implementation

1. **Finalize adapted questionnaire**
2. **Train enumerators**
3. **Establish call schedule**
4. **Conduct pilot round**
5. **Analyze and link to HMIS**
6. **Report and use findings**

**Key question:** How will HFA results feed into your routine monitoring and decision-making processes?

---



# Next Steps & Action Planning

Key actions to take after this working session:

- Finalize adapted phone survey questionnaire
- Complete first quarterly report draft
- Train remaining MoH team on data downloader tools
- Prepare roadmap for participation in Abuja workshop

---

# Quarterly Reporting Cycle

Establish a sustainable reporting rhythm:

- Define quarterly report timeline and responsibilities
- Set up data extraction schedule
- Establish review and approval process
- Plan dissemination to stakeholders

---

# Continued Platform Usage

Maintain momentum with the FASTR platform:

- Regular data updates and quality checks
- Expanding analysis to additional indicators
- Building capacity across MoH teams
- Documentation of lessons learned

---



# Workshop Closing

Thank you for your participation!

Over the past four days, we have:

- Configured the FASTR platform for Zambia
- Created the first quarterly RMNCAH-N report
- Adapted the HFA questionnaire for local context
- Built capacity for ongoing analysis and reporting

---

# Stay Connected

Continue the journey:

- Platform access and support
- Quarterly report submissions
- Multi-country workshop in Abuja
- Ongoing technical assistance from GFF team

---

# Thank You

FASTR Working Session - Zambia
January 27-30, 2026
Lusaka

---


# Contact Information

**FASTR Team**

<img src="../resources/icons/email.png" class="icon" style="height: 1em; vertical-align: middle;"> **Email:** 

<img src="../resources/icons/globe.png" class="icon" style="height: 1em; vertical-align: middle;"> **Website:** https://fastr.org

---

