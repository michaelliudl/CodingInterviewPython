SELECT round(sum(CASE players.day_count WHEN 2 THEN 1 ELSE 0 END) / count(players.player_id), 2) AS fraction FROM 
(SELECT act.player_id, count(act.event_date) AS day_count
FROM Activity act
LEFT OUTER JOIN
(SELECT player_id, min(event_date) AS first_date
FROM Activity
GROUP BY player_id) first_play
ON act.player_id = first_play.player_id
WHERE DATEDIFF(act.event_date, first_play.first_date) <= 1
GROUP BY act.player_id) players
