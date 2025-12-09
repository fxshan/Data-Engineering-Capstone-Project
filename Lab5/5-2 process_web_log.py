# import the libraries
from datetime import timedelta
from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago

# Task 1 - defining DAG arguments
default_args = {
    'owner': 'Yummy',
    'start_date': days_ago(0),
    'email': ['yummy@example.com'],
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Task 2 - defining the DAG
dag = DAG(
    'process_web_log',
    default_args=default_args,
    description='Data Pipelines Using Apache AirFlow',
    schedule_interval=timedelta(days=1),
)

# define the tasks
# Task 3 - define the task 'extract_data'
extract_data = BashOperator(
    task_id='extract_data',
    bash_command="""cut -d ' ' -f1 /home/project/airflow/dags/capstone/accesslog.txt \
    > /home/project/airflow/dags/capstone/extracted_data.txt""",
    dag=dag,
)

# Task 4 - define the task 'transform_data'
transform_data = BashOperator(
    task_id='transform_data',
    bash_command="grep -v '198.46.149.143' /home/project/airflow/dags/capstone/extracted_data.txt \
    > /home/project/airflow/dags/capstone/transformed_data.txt",
    dag=dag,
)

# Task 5 - define the task 'load_data'
load_data = BashOperator(
    task_id='load_data',
    bash_command="tar -cvf /home/project/airflow/dags/capstone/weblog.tar \
    /home/project/airflow/dags/capstone/transformed_data.txt",
    dag=dag,
)

# Task 6 - define the task pipeline
extract_data >> transform_data >> load_data