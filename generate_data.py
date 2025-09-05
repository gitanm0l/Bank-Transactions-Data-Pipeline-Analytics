import pandas as pd
import random
from faker import Faker

fake = Faker()

# =======================
# Generate Customers
# =======================
customers = []
for i in range(1, 101):  # 100 customers
    customers.append([
        i,
        fake.name(),
        fake.date_of_birth(minimum_age=18, maximum_age=70),
        fake.city(),
        fake.email(),
        fake.phone_number()
    ])

df_customers = pd.DataFrame(customers, columns=["customer_id", "name", "dob", "city", "email", "phone"])
df_customers.to_csv("data/customers.csv", index=False)
print("✅ customers.csv generated with", len(df_customers), "records")


# =======================
# Generate Accounts
# =======================
accounts = []
account_id = 1000
for cust_id in range(1, 101):
    for _ in range(random.randint(1, 3)):  # 1–3 accounts per customer
        accounts.append([
            account_id,
            cust_id,
            random.choice(["Savings", "Current", "Fixed Deposit"]),
            round(random.uniform(1000, 100000), 2)  # balance
        ])
        account_id += 1

df_accounts = pd.DataFrame(accounts, columns=["account_id", "customer_id", "type", "balance"])
df_accounts.to_csv("data/accounts.csv", index=False)
print("✅ accounts.csv generated with", len(df_accounts), "records")


# =======================
# Generate Transactions
# =======================
transactions = []
txn_id = 1
for account_id in df_accounts["account_id"]:  # all accounts
    for _ in range(random.randint(20, 100)):  # 20–100 transactions per account
        transactions.append([
            txn_id,
            account_id,
            fake.date_between(start_date='-1y', end_date='today'),
            round(random.uniform(100, 50000), 2),
            random.choice(["Debit", "Credit"])
        ])
        txn_id += 1

df_transactions = pd.DataFrame(transactions, columns=["txn_id", "account_id", "date", "amount", "type"])
df_transactions.to_csv("data/transactions.csv", index=False)
print("✅ transactions.csv generated with", len(df_transactions), "records")

print("\n🎉 Data generation complete! Now run etl_pipeline.py to load into bank.db")
