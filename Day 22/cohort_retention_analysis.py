"""
Cohort Retention Basics
Build a cohort retention table by signup month using Python.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

INPUT = "customer_events.csv"

df = pd.read_csv(INPUT, parse_dates=["SignupDate", "EventDate"])

# 1. Define cohort and activity month
df["cohort_month"] = df["SignupDate"].dt.to_period("M").dt.to_timestamp()
df["activity_month"] = df["EventDate"].dt.to_period("M").dt.to_timestamp()

# 2. Calculate month number since signup
df["cohort_index"] = (
    (df["activity_month"].dt.year - df["cohort_month"].dt.year) * 12
    + (df["activity_month"].dt.month - df["cohort_month"].dt.month)
)

# 3. Unique active customers
active = df[["CustomerID", "cohort_month", "cohort_index"]].drop_duplicates()

# 4. Cohort size = unique customers active in Month 0
cohort_sizes = (
    active[active["cohort_index"] == 0]
    .groupby("cohort_month")["CustomerID"]
    .nunique()
    .rename("cohort_size")
)

# 5. Active customer count by cohort/month
cohort_counts = (
    active.groupby(["cohort_month", "cohort_index"])["CustomerID"]
    .nunique()
    .rename("active_customers")
    .reset_index()
    .merge(cohort_sizes, on="cohort_month")
)

# 6. Retention percentage
cohort_counts["retention_pct"] = (
    cohort_counts["active_customers"] / cohort_counts["cohort_size"] * 100
)

# 7. Retention table
retention = cohort_counts.pivot(
    index="cohort_month",
    columns="cohort_index",
    values="retention_pct"
).sort_index()

retention.columns = [f"Month {int(c)}" for c in retention.columns]
retention.index = retention.index.strftime("%Y-%m")
retention.to_csv("cohort_retention_table.csv")

print("\nCOHORT RETENTION TABLE (%)")
print(retention.round(1))

# 8. Heatmap
plt.figure(figsize=(12, 7))
sns.heatmap(
    retention.astype(float),
    annot=True,
    fmt=".1f",
    cmap="Blues",
    vmin=0,
    vmax=100,
    linewidths=.5,
    cbar_kws={"label": "Retention (%)"}
)
plt.title("Cohort Retention Heatmap")
plt.xlabel("Months Since Signup")
plt.ylabel("Signup Cohort")
plt.tight_layout()
plt.savefig("cohort_retention_heatmap.png", dpi=180)
plt.show()
