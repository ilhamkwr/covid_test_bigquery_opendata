from google.cloud import bigquery
from google.oauth2 import service_account

def service_acc():
	key_path = "apps/src/prestient-8c5720286412.json"
	credentials = service_account.Credentials.from_service_account_file(
	    key_path,
	    scopes = ["https://www.googleapis.com/auth/bigquery"],
	)

	client = bigquery.Client(
	    credentials=credentials,
	    project=credentials.project_id
	)

	return client
