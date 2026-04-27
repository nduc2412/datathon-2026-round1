---
trigger: model_decision
description: Use this when you need structure and information (data dictionary) of files related to operational files. 
---

### Table `inventory.csv` - Monthly Inventory Snapshot
*Description: Tracks stock levels and operational efficiency at the end of each month.*

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `snapshot_date` | `date` | The date the snapshot was taken (typically month-end). |
| `product_id` | `int` | **Foreign Key**. Links to `products.csv`. |
| `stock_on_hand` | `int` | Physical inventory remaining at month-end. |
| `units_received` | `int` | Total units added to stock during the month. |
| `units_sold` | `int` | Total units sold during the month. |
| `stockout_days` | `int` | Number of days the product was out of stock. |
| `days_of_supply` | `float` | Estimated days the current stock will last based on sales velocity. |
| `fill_rate` | `float` | Percentage of demand met by available stock. |
| `stockout_flag` | `int` | Binary flag (0/1): Indicates if a stockout occurred. |
| `overstock_flag` | `int` | Binary flag (0/1): Indicates if stock levels exceed healthy limits. |
| `reorder_flag` | `int` | Binary flag (0/1): Indicates if a restock order is required. |
| `sell_through_rate`| `float` | Ratio of units sold compared to total stock available. |

---

### Table `web_traffic.csv` - Daily Website Performance
*Description: Daily metrics summarizing user behavior and traffic on the e-commerce platform.*

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `date` | `date` | The date of the traffic recording. |
| `sessions` | `int` | Total number of browsing sessions. |
| `unique_visitors` | `int` | Number of distinct users visiting the site. |
| `page_views` | `int` | Total number of pages viewed across all sessions. |
| `bounce_rate` | `float` | Percentage of single-page sessions (users leaving immediately). |
| `avg_session_duration_sec` | `float` | Average time spent on the site per session (in seconds). |
| `conversion_rate` | `float` | Percentage of sessions that resulted in a successful order. |
| `traffic_source` | `str` | Origin of the traffic (e.g., Organic, Paid Ads, Social, Direct). |


