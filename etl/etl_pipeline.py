import pandas as pd
import sqlite3
import os
from datetime import datetime

# --- Safety check: remove old DB if it exists ---
if os.path.exists("bank.db"):
    os.remove("bank.db")
    print("⚠️ Old database deleted. Fresh DB will be created.")

# Load CSVs
customers = pd.read_csv('../data/customers.csv')
accounts = pd.read_csv('../data/accounts.csv')
transactions = pd.read_csv('../data/transactions.csv')

# Connect to SQLite DB
conn = sqlite3.connect('bank.db')
cursor = conn.cursor()

# Create tables
cursor.executescript(open('../sql/schema.sql').read())

# Insert data
customers.to_sql('Customers', conn, if_exists='append', index=False)
accounts.to_sql('Accounts', conn, if_exists='append', index=False)
transactions.to_sql('Transactions', conn, if_exists='append', index=False)

conn.commit()

# ---- Summary Section ----
print(f"\n✅ ETL Run Completed at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("-------------------------------------------------")

# Total counts
cursor.execute("SELECT COUNT(*) FROM Customers;")
print(f"Total Customers       : {cursor.fetchone()[0]}")

cursor.execute("SELECT COUNT(*) FROM Accounts;")
print(f"Total Accounts        : {cursor.fetchone()[0]}")

cursor.execute("SELECT COUNT(*) FROM Transactions;")
print(f"Total Transactions    : {cursor.fetchone()[0]}")

# High-value & suspicious transactions
cursor.execute("SELECT COUNT(*) FROM Transactions WHERE amount > 50000;")
print(f"High-Value Txns (>50k): {cursor.fetchone()[0]}")

cursor.execute("""
    SELECT COUNT(*)
    FROM Transactions t
    JOIN Accounts a ON t.account_id = a.account_id
    WHERE t.type = 'Debit' AND t.amount > a.balance;
""")
print(f"Suspicious Txns       : {cursor.fetchone()[0]}")
print("-------------------------------------------------")

# ---- Fraud / Segmentation Outputs ----

# Top 5 suspicious transactions
print("\n🚨 Suspicious Transactions (Top 5):")
suspicious = pd.read_sql("""
    SELECT t.txn_id, t.account_id, t.date, t.amount, t.type
    FROM Transactions t
    JOIN Accounts a ON t.account_id = a.account_id
    WHERE t.type = 'Debit' AND t.amount > a.balance
    LIMIT 5;
""", conn)
if not suspicious.empty:
    print(suspicious.to_string(index=False))
else:
    print("No suspicious transactions found.")

# Top 5 high-value customers
print("\n💰 High Net-Worth Customers (Top 5 by Balance):")
hnw = pd.read_sql("""
    SELECT c.customer_id, c.name, c.city, SUM(a.balance) as total_balance
    FROM Customers c
    JOIN Accounts a ON c.customer_id = a.customer_id
    GROUP BY c.customer_id
    ORDER BY total_balance DESC
    LIMIT 5;
""", conn)
print(hnw.to_string(index=False))

# Show 10 sample transactions
print("\n📊 Sample Transactions:")
sample_txns = pd.read_sql("SELECT * FROM Transactions LIMIT 10;", conn)
print(sample_txns.to_string(index=False))

conn.close()
