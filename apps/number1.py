import streamlit as st
from apps.service_account import *

a = open('apps/src/answer_sql1.sql', 'r')
query = a.read()
a.close()
client = service_acc()
query_job = client.query(query)
for row in query_job:
	numbers = "{:,}".format(row['cumulative_persons_vaccinated'])
	queue = "Cumulative number of people vaccinated on `{}` is `{}` persons in `{}`".format(row['date'], numbers, row['country_name'])

print(queue)

def app():
	st.title('Answer Number 1')
	st.write('How many persons in Indonesia `(country code: ID)` have been cumulatively vaccinated on June 1st 2022?')
	st.write(queue)