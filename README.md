# Cohort Retention Analysis

A data analytics project that analyzes customer retention using **cohort analysis** with Python and SQL.

## Project Objective

The objective is to group customers according to their signup month and track their activity across subsequent months to understand customer retention patterns.

## Technologies Used

* Python
* Pandas
* NumPy
* SQL
* Matplotlib
* Seaborn

## Analysis Performed

* Customer data preparation
* Signup-month cohort creation
* Activity-month calculation
* Month-since-signup calculation
* Unique active customer analysis
* Cohort retention percentage calculation
* Retention table generation
* Retention heatmap visualization
* Business insight generation

## Retention Formula

```text
Retention % =
(Active Unique Customers in Month N / Month 0 Cohort Size) × 100
```

## Project Files

* `customer_events.csv` – Customer activity dataset
* `cohort_retention_analysis.py` – Python analysis script
* `cohort_retention.sql` – SQL implementation
* `cohort_retention_table.csv` – Cohort retention percentages
* `cohort_active_customers.csv` – Active customer counts
* `cohort_retention_heatmap.png` – Retention heatmap
* `insights.md` – Business insights
* `README.md` – Project documentation
* `requirements.txt` – Required Python libraries

## Key Insights

The analysis shows how customer retention changes as the number of months since signup increases. The cohort heatmap makes it easier to compare retention patterns between different signup cohorts and identify customer drop-off periods.

## Skills Demonstrated

Python • SQL • Pandas • NumPy • Data Cleaning • Data Transformation • Cohort Analysis • Customer Retention • Data Visualization • Business Analytics

## Future Improvements

* Add Power BI dashboard
* Segment retention by customer attributes
* Calculate Customer Lifetime Value
* Add churn prediction using Machine Learning
* Compare retention across acquisition channels
