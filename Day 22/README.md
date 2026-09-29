# Cohort Retention Basics

## Objective
Build a cohort retention table by signup month and understand retention over time.

## Tools
- Python
- SQL
- Pandas
- NumPy
- Matplotlib
- Seaborn

## Deliverables
1. `cohort_retention_table.csv` – retention percentages by signup cohort and month.
2. `cohort_active_customers.csv` – active customer counts.
3. `cohort_retention_heatmap.png` – visual retention heatmap.
4. `cohort_retention_analysis.py` – complete Python workflow.
5. `cohort_retention.sql` – SQL cohort-retention query.
6. `insights.md` – business insights and interpretation.
7. `customer_events.csv` – reproducible synthetic event dataset.

## How to run
```bash
pip install pandas numpy matplotlib seaborn
python cohort_retention_analysis.py
```

## Retention definition
Retention % = active unique customers in a given month / Month 0 cohort size × 100.

## Dataset note
A synthetic e-commerce customer-event dataset is included so the project is self-contained and reproducible.
