---
marp: true
theme: fastr
paginate: true
---

## Estimating denominators from ANC-1

If ANC-1 coverage is known from survey data, we can derive other denominators:

**Example calculation:**
- ANC-1 count from DHIS2: **100,000**
- Survey ANC-1 coverage: **95%**
- Estimated pregnancies = 100,000 ÷ 0.95 = **105,263**

**Applying the cascade:**

| Step | Calculation | Result |
|------|-------------|--------|
| Pregnancies | 100,000 ÷ 0.95 | 105,263 |
| Deliveries | 105,263 × (1 - 0.03) | 102,105 |
| Births | 102,105 × (1 + 0.015) | 103,637 |
| Live births | 103,637 × (1 - 0.02) | 101,564 |
| DPT-eligible | 101,564 × (1 - 0.03) | 98,517 |
| Measles-eligible | 98,517 × (1 - 0.02) | 96,547 |
