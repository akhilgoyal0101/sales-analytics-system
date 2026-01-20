# 📊 Sales Analytics System

## Module 3 – Python Programming Assignment

---

## 📌 Project Overview

This project implements a **Sales Analytics System** for an e-commerce company.  
The system reads and cleans messy sales transaction data, integrates external product data using an API, performs detailed sales analysis, and generates a comprehensive business report.

This assignment demonstrates:
- Python fundamentals
- File handling & encoding handling
- Data cleaning and validation
- Modular programming
- API integration
- Error handling
- Analytical reporting

---

## 🧩 Problem Statement

The system is designed to:
- Read and clean sales transaction data
- Handle encoding and data quality issues
- Analyze sales performance and customer behavior
- Fetch product metadata using an external API
- Enrich transaction data
- Generate a comprehensive analytics report

---

## 📂 Project Structure

---
sales-analytics-system/
├── README.md
├── main.py
├── requirements.txt
├── utils/
│ ├── file_handler.py
│ ├── data_processor.py
│ └── api_handler.py
├── data/
│ ├── sales_data.txt
│ └── enriched_sales_data.txt
├── output/
│ └── sales_report.txt


---

## 🗂 Dataset Details

- File: `data/sales_data.txt`
- Format: Pipe-delimited (`|`)
- Encoding: Non-UTF-8
- Data quality issues handled:
  - Commas in product names
  - Commas in numeric values
  - Missing or extra fields
  - Invalid quantities and prices
  - Invalid ID formats

---

## 🧹 Data Cleaning Rules

### ❌ Records Removed
- Missing CustomerID or Region
- Quantity ≤ 0
- UnitPrice ≤ 0
- TransactionID not starting with `T`

### ✅ Records Cleaned & Kept
- Commas removed from product names
- Commas removed from numeric fields
- Empty lines skipped

---

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.8 or above
- Internet connection (for API calls)

### Install Dependencies
```bash
pip install -r requirements.txt

