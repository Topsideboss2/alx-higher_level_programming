-- Script that displays the max temperatures of each state
-- Query to display the max temperatures of each state

SELECT state, MAX(value) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state ASC;
