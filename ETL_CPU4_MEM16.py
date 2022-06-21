from airflow.models import DAG
from airflow.utils.dates import days_ago
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator
import pendulum
from datetime import datetime
from datetime import timedelta
from airflow.utils.trigger_rule import TriggerRule

KST = pendulum.timezone("Asia/Seoul")

args = {
    'owner': 'airflow', 
    'start_date': days_ago(0),
     }

dag  = DAG(dag_id='ETL_CPU4_MEM16',
           default_args=args,
           schedule_interval=None,
           tags=['Kube'],
        )

t1 = KubernetesPodOperator(
    task_id='ETL_CPU4_MEM16_TASK',
    name='ETL_CPU4_MEM16_TASK',
    namespace='airflow-cluster',
    image='ubuntu:18.04',
    cmds=['echo', 'TEST'],
    # is_delete_operator_pod=True,
    # in_cluster=True,
    node_selectors={
        "CPU": "4",
        "MEM": "16",
        "app": "airflow"
    },
    dag=dag
    )

t1