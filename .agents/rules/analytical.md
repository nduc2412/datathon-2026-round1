---
trigger: model_decision
description: Use this when you need schemas of files related to analytical files. 
---

### Table `sales.csv`

This table contains essential aggregated financial metrics. It serves as the primary dataset for Time-Series Forecasting and business performance analysis.

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `Date` | `date` | The date on which the orders were placed. |
| `Revenue` | `float` | Total Net Revenue generated for the specific day. |
| `COGS` | `float` | Total Cost of Goods Sold (COGS) incurred for the day. |
