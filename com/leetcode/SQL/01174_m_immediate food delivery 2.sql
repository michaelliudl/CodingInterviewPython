
SELECT round(sum((CASE order_date = customer_pref_delivery_date WHEN TRUE THEN 1 ELSE 0 END)) / count(*) * 100.0, 2) AS immediate_percentage
FROM Delivery JOIN 
(SELECT customer_id, min(order_date) AS first_date
FROM Delivery
GROUP BY customer_id
ORDER BY order_date) AS first_order
ON Delivery.customer_id = first_order.customer_id AND Delivery.order_date = first_order.first_date