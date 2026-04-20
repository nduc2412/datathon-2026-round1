---
trigger: always_on
---

# Project Strategy: Daily Revenue Forecasting (Vietnam Fashion E-commerce)

## 1. Business Context & Objective
You are acting as a **Lead Data Scientist** for a Vietnamese fashion e-commerce firm. 
- **Mission:** Build an accurate Daily Revenue Forecast model.
- **Timeline:** 04/07/2012 – 31/12/2022 (Training Data).
- **Core Business Values:**
    1. **Inventory Optimization:** Prevent stockouts/overstock.
    2. **Promotion Planning:** Align sales spikes with marketing spend.
    3. **Logistics Management:** Forecast load for nationwide delivery.

---

## 2. Data Architecture Overview
The dataset consists of 15 CSV files categorized into 4 layers. 
*Note: Refer to `@master.md`, `@transaction.md`, `@analytical.md`, and `@operational.md` for specific field definitions.*

### Table Relationships & Cardinality
| Entity Pair | Cardinality | Key Joining Logic |
| :--- | :--- | :--- |
| `orders` ↔ `payments` | 1 : 1 | Direct link for financial reconciliation. |
| `orders` ↔ `shipments` | 1 : 0 or 1 | Identify successful deliveries vs. lost/failed. |
| `orders` ↔ `returns` | 1 : 0 or many | Calculate "Return Rate" impact on revenue. |
| `orders` ↔ `reviews` | 1 : 0 or many | Sentiment analysis (~20% of delivered orders). |
| `order_items` ↔ `promotions` | many : 0 or 1 | Map specific product discounts. |
| `products` ↔ `inventory` | 1 : many | Monthly snapshots (1 record/product/month). |

---

## 3. Analytical instructions

- Follow the cleaning pipeline in `skills/data-cleaning-pipeline`.
- Handle the COVID-19 period (2020-2021) as a high-impact anomaly.

