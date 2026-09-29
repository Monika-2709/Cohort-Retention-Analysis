-- Cohort Retention Basics
-- Table assumed: customer_events
-- Columns: CustomerID, SignupDate, EventDate

WITH base AS (
    SELECT DISTINCT
        CustomerID,
        DATE_TRUNC('month', SignupDate) AS cohort_month,
        DATE_TRUNC('month', EventDate) AS activity_month
    FROM customer_events
),
cohort_activity AS (
    SELECT
        CustomerID,
        cohort_month,
        (
            EXTRACT(YEAR FROM activity_month) * 12
            + EXTRACT(MONTH FROM activity_month)
            - EXTRACT(YEAR FROM cohort_month) * 12
            - EXTRACT(MONTH FROM cohort_month)
        )::INT AS cohort_index
    FROM base
),
cohort_size AS (
    SELECT
        cohort_month,
        COUNT(DISTINCT CustomerID) AS cohort_size
    FROM cohort_activity
    WHERE cohort_index = 0
    GROUP BY cohort_month
),
retention AS (
    SELECT
        ca.cohort_month,
        ca.cohort_index,
        COUNT(DISTINCT ca.CustomerID) AS active_customers,
        cs.cohort_size,
        ROUND(
            100.0 * COUNT(DISTINCT ca.CustomerID) / cs.cohort_size,
            1
        ) AS retention_pct
    FROM cohort_activity ca
    JOIN cohort_size cs
      ON ca.cohort_month = cs.cohort_month
    GROUP BY ca.cohort_month, ca.cohort_index, cs.cohort_size
)
SELECT *
FROM retention
ORDER BY cohort_month, cohort_index;

-- For a pivoted table in PostgreSQL, conditional aggregation can be used:
SELECT
    cohort_month,
    MAX(CASE WHEN cohort_index = 0 THEN retention_pct END) AS month_0,
    MAX(CASE WHEN cohort_index = 1 THEN retention_pct END) AS month_1,
    MAX(CASE WHEN cohort_index = 2 THEN retention_pct END) AS month_2,
    MAX(CASE WHEN cohort_index = 3 THEN retention_pct END) AS month_3,
    MAX(CASE WHEN cohort_index = 4 THEN retention_pct END) AS month_4,
    MAX(CASE WHEN cohort_index = 5 THEN retention_pct END) AS month_5
FROM retention
GROUP BY cohort_month
ORDER BY cohort_month;
