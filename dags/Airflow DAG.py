from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',  # Replace ${USER} with 'airflow' or your name
    'depends_on_past': False,
    'start_date': datetime(2024, 2, 15),  # Replace with actual date
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'my_first_dag',  # Replace ${NAME} with your DAG name
    default_args=default_args,
    description='My first Airflow DAG',  # Replace ${DESCRIPTION} with your description
    schedule_interval=timedelta(days=1),
)

# Add at least one task
def print_hello():
    return 'Hello from first Airflow DAG!'

task1 = PythonOperator(
    task_id='hello_task',
    python_callable=print_hello,
    dag=dag,
)

