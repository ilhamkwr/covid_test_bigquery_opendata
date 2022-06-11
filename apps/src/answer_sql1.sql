SELECT 
SUM(cumulative_persons_vaccinated) AS cumulative_persons_vaccinated,
country_name, 
date
FROM `bigquery-public-data.covid19_open_data.covid19_open_data`
WHERE country_code = 'ID' AND date = '2022-06-01'
GROUP BY date, country_name