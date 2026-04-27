---
trigger: model_decision
description: Use this when you need structure and information (data dictionary) of files related to transaction files. 
---

# Transaction Data Schema: Datathon 2026 (Fashion E-commerce)

**Context:** This document outlines the transaction-related tables for the Vietnamese Fashion E-commerce dataset. These tables capture the lifecycle of an order, from placement to delivery, payment, and potential returns or reviews.

---

## 1. Table: `orders.csv` (Orders)
*Description: The core transaction table containing high-level order information.*

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `order_id` | `int` | **Primary Key**. Unique identifier for each order. |
| `order_date` | `date` | Date when the order was placed. |
| `customer_id` | `int` | **Foreign Key**. Links to `customers.csv`. |
| `zip` | `int` | Shipping postal code for the order. |
| `order_status` | `str` | Current status (e.g., Shipped, Delivered, Cancelled). |
| `payment_method` | `str` | Primary payment method used. |
| `device_type` | `str` | Device used to place the order (Mobile, Web, App). |
| `order_source` | `str` | Marketing channel source for the order. |

---

## 2. Table: `order_items.csv` (Order Details)
*Description: Line-item details for each product within an order.*

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `order_id` | `int` | **Foreign Key**. Links to `orders.csv`. |
| `product_id` | `int` | **Foreign Key**. Links to `products.csv`. |
| `quantity` | `int` | Number of units purchased. |
| `unit_price` | `float` | Unit price after discount applied. |
| `discount_amount`| `float` | Total discount amount applied to these items. |
| `promo_id` | `str` | **Foreign Key**. Links to `promotions.csv` (nullable). |
| `promo_id_2` | `str` | Secondary promotion applied (nullable). |

---

## 3. Table: `payments.csv` (Payments)
*Description: Transactional payment details. Has a 1:1 relationship with `orders.csv`.*

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `order_id` | `int` | **Foreign Key**. Links to `orders.csv`. |
| `payment_method` | `str` | Specific payment method used. |
| `payment_value` | `float` | Total value paid for the order. |
| `installments` | `int` | Number of installment payments (if applicable). |

---

## 4. Table: `shipments.csv` (Logistics)
*Description: Shipping and delivery tracking. Only applicable for shipped/delivered/returned orders.*

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `order_id` | `int` | **Foreign Key**. Links to `orders.csv`. |
| `ship_date` | `date` | Date the package was sent. |
| `delivery_date` | `date` | Date the package reached the customer. |
| `shipping_fee` | `float` | Cost of shipping charged. |

---

## 5. Table: `returns.csv` (Returns)
*Description: Records of returned products and refund amounts.*

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `return_id` | `str` | **Primary Key**. Unique identifier for the return. |
| `order_id` | `int` | **Foreign Key**. Links to `orders.csv`. |
| `product_id` | `int` | **Foreign Key**. Links to `products.csv`. |
| `return_date` | `date` | Date when the return was processed. |
| `return_reason` | `str` | Reason for returning the item. |
| `return_quantity`| `int` | Number of units returned. |
| `refund_amount` | `float` | Amount refunded to the customer. |

---

## 6. Table: `reviews.csv` (Product Reviews)
*Description: Customer feedback and ratings for specific products.*

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `review_id` | `str` | **Primary Key**. Unique identifier for the review. |
| `order_id` | `int` | **Foreign Key**. Links to `orders.csv`. |
| `product_id` | `int` | **Foreign Key**. Links to `products.csv`. |
| `customer_id` | `int` | **Foreign Key**. Links to `customers.csv`. |
| `review_date` | `date` | Date the review was submitted. |
| `rating` | `int` | Star rating (typically 1–5). |
| `review_title` | `str` | Summary/Title of the review. |

