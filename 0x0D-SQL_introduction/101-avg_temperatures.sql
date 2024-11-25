-- Script to calculate the average temperature (Fahrenheit) by city
-- Results are ordered by temperature in descending order

SELECT city, AVG(temperature) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
