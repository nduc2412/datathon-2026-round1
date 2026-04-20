---
trigger: model_decision
description: Use this when you need structure and information (data dictionary) of files related to master files.
---

# Master Data Schema: Datathon 2026 (Fashion E-commerce)

**Context:** This document provides the schema for the Master Data tables of a Vietnamese Fashion E-commerce dataset (4/7/2012-31/12/2022). Use this schema to perform data joining, cleaning, and feature engineering.

---

## 1. Table: `products.csv` (Product Catalog)
*Description: Contains detailed attributes of all fashion items sold.*

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `product_id` | `int` | **Primary Key**. Unique identifier for each product. |
| `product_name` | `str` | Name of the product. |
| `category` | `str` | Product category (e.g., Shirt, Pants, Dress). |
| `segment` | `str` | Market segment (e.g., Premium, Mass, Budget). |
| `size` | `str` | Size variant (S, M, L, XL, etc.). |
| `color` | `str` | Color label. |
| `price` | `float` | Retail unit price. |
| `cogs` | `float` | Cost of Goods Sold (Acquisition cost). |

---

## 2. Table: `customers.csv` (Customer Registry)
*Description: Contains demographic information and signup details of customers.*

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `customer_id` | `int` | **Primary Key**. Unique identifier for each customer. |
| `zip` | `int` | **Foreign Key**. Links to `geography.csv`. |
| `city` | `str` | City of residence. |
| `signup_date` | `date` | Date the customer registered. |
| `gender` | `str` | Gender (nullable). |
| `age_group` | `str` | Age classification (nullable). |
| `acquisition_channel`| `str` | Marketing channel source (nullable). |

---

## 3. Table: `promotions.csv` (Marketing Campaigns)
*Description: Defines discount rules and campaign durations.*

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `promo_id` | `str` | **Primary Key**. Unique identifier for the promotion. |
| `promo_name` | `str` | Name of the marketing campaign. |
| `promo_type` | `str` | Discount type (`percentage` or `fixed`). |
| `discount_value` | `float` | Value of the discount. |
| `start_date` | `date` | Official start date. |
| `end_date` | `date` | Official end date. |
| `applicable_category`| `str` | Target category (null = all categories). |
| `promo_channel` | `str` | Distribution channel (nullable). |
| `stackable_flag` | `int` | Flag (0/1) for combined promotions. |
| `min_order_value` | `float` | Minimum spend requirement. |

---

## 4. Table: `geography.csv` (Location Mapping)
*Description: Provides regional mapping for spatial analysis.*

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `zip` | `int` | **Primary Key**. Unique postal code identifier. |
| `city` | `str` | Name of the city. |
| `region` | `str` | Geographic region (North, Central, South). |
| `district` | `str` | Specific district or county. |