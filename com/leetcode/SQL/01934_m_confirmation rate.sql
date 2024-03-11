SELECT user_id, (CASE count(confirm_user_id) WHEN 0 THEN 0.00 ELSE round(sum(confirm_counter) / count(confirm_user_id), 2) END) AS confirmation_rate
FROM 
(SELECT s.user_id AS user_id, c.user_id AS confirm_user_id,
(CASE c.action WHEN 'confirmed' THEN 1 ELSE 0 END) AS confirm_counter
FROM Signups s
LEFT OUTER JOIN Confirmations c ON s.user_id = c.user_id
) AS confirmed
GROUP BY user_id