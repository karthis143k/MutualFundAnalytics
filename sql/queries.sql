-- 1. Top 5 Funds by AUM
SELECT fund_house, SUM(aum_crore) AS total_aum
FROM fact_aum
GROUP BY fund_house
ORDER BY total_aum DESC
LIMIT 5;

-- 2. Average NAV per Month
SELECT strftime('%Y-%m', date) AS month,
AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY month;

-- 3. SIP Transactions Count
SELECT transaction_type, COUNT(*)
FROM fact_transactions
GROUP BY transaction_type;

-- 4. Transactions by State
SELECT state, COUNT(*)
FROM fact_transactions
GROUP BY state
ORDER BY COUNT(*) DESC;

-- 5. Funds with Expense Ratio < 1%
SELECT amfi_code
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- 6. Average 1-Year Return
SELECT AVG(return_1yr_pct)
FROM fact_performance;

-- 7. Highest Sharpe Ratio Funds
SELECT amfi_code, sharpe_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 10;

-- 8. Total NAV Records
SELECT COUNT(*)
FROM fact_nav;

-- 9. Average Transaction Amount
SELECT AVG(amount_inr)
FROM fact_transactions;

-- 10. Fund Count by Category
SELECT category, COUNT(*)
FROM dim_fund
GROUP BY category;