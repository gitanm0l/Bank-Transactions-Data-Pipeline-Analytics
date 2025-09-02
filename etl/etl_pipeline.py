
import pandas as pd
import sqlite3

# Load CSVs
customers = pd.read_csv('../data/customers.csv')
accounts = pd.read_csv('../data/accounts.csv')
transactions = pd.read_csv('../data/transactions.csv')

# Connect to SQLite DB (or any RDBMS)
conn = sqlite3.connect('bank.db')
cursor = conn.cursor()

# Create tables
cursor.executescript(open('../sql/schema.sql').read())

# Insert data
customers.to_sql('Customers', conn, if_exists='append', index=False)
accounts.to_sql('Accounts', conn, if_exists='append', index=False)
transactions.to_sql('Transactions', conn, if_exists='append', index=False)

conn.commit()
print("ETL Completed: Data loaded into bank.db")

# Run a sample query
query = "SELECT * FROM Transactions LIMIT 5;"
print(pd.read_sql(query, conn))

conn.close()
