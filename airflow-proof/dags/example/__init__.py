from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.utils.dates import days_ago
from .helloworld import get_hello_world
import os

dag_args = {
    'owner': 'Marin',
    'start_date': days_ago(2),
    'retries': 0,
    'email_on_failure': False
}

# CURRENT_FOLDER = os.path.dirname(os.path.abspath(__file__))

with DAG(dag_id='example_id', default_args=dag_args, schedule_interval=None, concurrency=4) as dag:
    dummy_operator = DummyOperator(task_id='dummy_task', retries=3, dag=dag)

    python_operator = PythonOperator(task_id='hello_world', python_callable=get_hello_world, dag=dag)

    docker_operator = DockerOperator(task_id='docker_1',
                                     image='node/jsservice:v1',
                                     command=['node', 'index.js'],
                                     auto_remove=True,
                                     volumes=[
                                         '/tmp/airflow/data:/data'
                                     ])

    # docker_operator_server = DockerOperator(task_id='docker_http',
    #                                         image='node/jsservice:v1',
    #                                         command=['npm', 'run', 'start'],
    #                                         docker_url='unix://var/run/docker.sock',
    #                                         auto_remove=True,
    #                                         volumes=["/tmp/airflow/data:/data"])

    dummy_operator >> python_operator >> docker_operator  # >> docker_operator_server
