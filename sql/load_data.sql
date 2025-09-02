
-- Load data from CSV (syntax may vary depending on DBMS)
-- Example for MySQL:
LOAD DATA INFILE 'customers.csv' INTO TABLE Customers
FIELDS TERMINATED BY ',' IGNORE 1 ROWS;

LOAD DATA INFILE 'accounts.csv' INTO TABLE Accounts
FIELDS TERMINATED BY ',' IGNORE 1 ROWS;

LOAD DATA INFILE 'transactions.csv' INTO TABLE Transactions
FIELDS TERMINATED BY ',' IGNORE 1 ROWS;
