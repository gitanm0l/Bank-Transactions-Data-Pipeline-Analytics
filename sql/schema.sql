
CREATE TABLE Customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(100),
    dob DATE,
    city VARCHAR(50)
);

CREATE TABLE Accounts (
    account_id INT PRIMARY KEY,
    customer_id INT,
    type VARCHAR(20),
    balance DECIMAL(12,2),
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

CREATE TABLE Transactions (
    txn_id INT PRIMARY KEY,
    account_id INT,
    date DATE,
    amount DECIMAL(12,2),
    type VARCHAR(10),
    FOREIGN KEY (account_id) REFERENCES Accounts(account_id)
);
