SELECT 
SUM(new_confirmed) AS new_confirmed, 
date,
country_name,
SUM(new_deceased) AS new_deceased
FROM `bigquery-public-data.covid19_open_data.covid19_open_data`
WHERE country_code = 'ID' AND date = '2022-01-01'
GROUP BY date, country_name