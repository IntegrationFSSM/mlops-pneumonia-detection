"""
DAG Simple pour Test - Doit apparaître dans Airflow UI
"""
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def hello():
    print("✅ DAG fonctionne!")
    return "Success"

dag = DAG(
    'test_simple',
    start_date=datetime(2025, 1, 1),
    schedule_interval=None,
    catchup=False,
)

task = PythonOperator(
    task_id='hello',
    python_callable=hello,
    dag=dag,
)
