# covid_test_bigquery_opendata
Load Covid19 in BigQuery OpenData with Streamlit Python
Setup Preparation

1. Before we start and install, we must create virtual environment and make the venv
![image](https://user-images.githubusercontent.com/32015538/173175426-e97f7035-1590-44ab-91e0-5d988d1d8b73.png)
in there i used Anaconda and make virtual Environment is 'covid_test' Then we run the venv

2. Then Install some Library with pip
pip install google-cloud-bigquery
pip install streamlit

3. Then We Run app.py with command
python -m streamlit run app.py

4. Then we can see in browser like this

Anwer Number 1 :
![image](https://user-images.githubusercontent.com/32015538/173175579-6b1b1005-b7d8-4c19-b915-05a57d6467eb.png)

Anwer Number 2 :
![image](https://user-images.githubusercontent.com/32015538/173175609-4348acd7-e0e6-4107-b729-646f5df8e887.png)



Code file explanation :
1. app.py = main file to load the website
2. multiapp.py = file code to make pages the script
3. apps/number1.py = file code to answer question number 1
4. apps/number2.py = file code to answer question number 2
5. apps/service_account = file code to connect with bigquery
6. apps/src/answer_sql1.sql = query file to answer question number 1
7. apps/src/answer_sql2.sql = query file to answer question number 2
8. apps/src/prestient-8c5720286412.json = key file, we get this from google service account
