# Cohort Retention Analysis – Insights

## Key findings
- The analysis groups customers by **signup month** and tracks whether they return in each subsequent month.
- Month 0 retention is 100% by definition because the cohort consists of customers who signed up in that month.
- Average Month 1 retention across cohorts with a Month 1 observation is **59.9%**.
- Average Month 3 retention across cohorts with a Month 3 observation is **32.6%**.
- The strongest observed Month 1 cohort is **2009-04** with **67.7%** retention.
- The largest signup cohort is **2009-05** with **80 customers**.
- Retention generally declines as the number of months since signup increases, showing the typical customer drop-off pattern.

## Business interpretation
1. **Early retention matters:** Month 1 is a useful checkpoint for identifying whether newly acquired customers come back.
2. **Compare cohorts, not only totals:** A cohort table reveals whether newer signup groups are retaining better or worse than earlier groups.
3. **Investigate drop-off periods:** Large month-to-month declines can indicate opportunities for onboarding, offers, reminders, or product improvements.
4. **Use consistent windows:** Retention percentages should only be compared across cohorts where the relevant month has had enough time to occur.
5. **Next step:** Segment cohorts by acquisition source, country, product category, or customer value to find which groups have stronger long-term retention.

## Method
Retention for a cohort/month is:
**Active unique customers in that month ÷ customers in the cohort at Month 0 × 100**

The project uses a reproducible synthetic customer-event dataset so the full workflow can be run without external downloads.
