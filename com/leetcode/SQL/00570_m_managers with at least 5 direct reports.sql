SELECT name FROM Employee e
JOIN
(SELECT e1.id, count(e2.id) AS reports
FROM Employee e1 LEFT OUTER JOIN Employee e2
ON e1.id = e2.managerId
GROUP BY e1.id HAVING reports >= 5) report
ON e.id = report.id