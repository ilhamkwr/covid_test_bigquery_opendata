import streamlit as st
from apps.service_account import *

a = open('apps/src/answer_sql2.sql', 'r')
query = a.read()
a.close()
client = service_acc()
query_job = client.query(query)
for row in query_job:
	case_confirmed = "{:,}".format(row['new_confirmed'])
	deceased = "{:,}".format(row['new_deceased'])

	queue = "Total case confirmed in {} is `{}` case and `{}` deceased on `{}` (New Year)".format(row['country_name'], case_confirmed, deceased, row['date'])

print(queue)

def app():
	st.title('Answer Number 2')
	st.write('Total confirmed cases in Indonesia during the new year (January 1st 2022)?')
	st.write(queue)