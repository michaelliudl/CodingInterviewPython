SELECT DATE_FORMAT(trans_date, '%Y-%m') AS month, country,
count(id) AS trans_count,
sum(CASE state WHEN 'approved' THEN 1 ELSE 0 END) AS approved_count,
sum(amount) AS trans_total_amount,
sum(CASE state WHEN 'approved' THEN amount ELSE 0 END) AS approved_total_amount
FROM Transactions
GROUP BY month, country