# Bank Transactions Data Pipeline

## Overview
This project simulates a simple **banking data pipeline** for AU Small Finance Bank style use cases.
It covers:
- Extracting data from CSV files
- Transforming and cleaning data (fraud detection, balances)
- Loading into a SQL database (SQLite/MySQL/Oracle)
- Running queries for insights (monthly reports, fraud detection, low balances)

## Tech Stack
- Python (Pandas, SQLite)
- SQL (DDL + Queries)
- Git/GitHub

## Dataset
- customers.csv → customer_id, name, dob, city
- accounts.csv → account_id, customer_id, type, balance
- transactions.csv → txn_id, account_id, date, amount, type

## ETL Flow
1. **Extract**: Load CSV files using Pandas
2. **Transform**: Basic cleaning & fraud flagging
3. **Load**: Store into SQL tables
4. **Analyze**: Run queries for insights

## Example Queries
- Total deposits/withdrawals per customer
- Customers with balance < 1000
- Transactions above 50,000 (possible fraud)
- Monthly transaction summary

## How to Run
```bash
cd etl
python etl_pipeline.py
```

This will create a SQLite DB (`bank.db`) with Customers, Accounts, Transactions tables.

## Future Improvements
- Build Power BI dashboard on top of DB
- Add advanced fraud detection logic
- Deploy pipeline on cloud (Azure/AWS)
