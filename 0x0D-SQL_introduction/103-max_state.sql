--  A script that displays the max temperature
-- of Each state (Ordered by stet name)
SELECT state,MAX(value) AS max_temp FROM temperatures GROUP BY state ORDER BY state; 
