
-- 1. Total deposits and withdrawals per customer
SELECT c.name, SUM(CASE WHEN t.type='Credit' THEN t.amount ELSE 0 END) AS total_deposits,
       SUM(CASE WHEN t.type='Debit' THEN t.amount ELSE 0 END) AS total_withdrawals
FROM Customers c
JOIN Accounts a ON c.customer_id = a.customer_id
JOIN Transactions t ON a.account_id = t.account_id
GROUP BY c.name;

-- 2. Customers with balance < 1000
SELECT c.name, a.balance
FROM Customers c
JOIN Accounts a ON c.customer_id = a.customer_id
WHERE a.balance < 1000;

-- 3. Transactions above 50000 (possible fraud)
SELECT * FROM Transactions
WHERE amount > 50000;

-- 4. Monthly transaction summary
SELECT DATE_FORMAT(date, '%Y-%m') AS month, type, SUM(amount) AS total_amount
FROM Transactions
GROUP BY month, type;
