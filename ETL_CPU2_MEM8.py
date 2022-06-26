from airflow.models import DAG
from airflow.utils.dates import days_ago
from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
import pendulum
from datetime import datetime
from datetime import timedelta
from airflow.utils.trigger_rule import TriggerRule
from kubernetes.client import models as k8s


KST = pendulum.timezone("Asia/Seoul")

args = {
    'owner': 'airflow', 
    'start_date': days_ago(0),
     }

dag  = DAG(dag_id='CPU2_MEM8',
           default_args=args,
           schedule_interval=None,
           tags=['Kube'],
        )

t1 = KubernetesPodOperator(
    task_id='ETL_CPU2_MEM8_TASK',
    name='airflow-cluster-worker-ETL_CPU2_MEM8_TASK',
    namespace='airflow-cluster',
    image='ubuntu:18.04',
    cmds=['echo', 'TEST'],
    # is_delete_operator_pod=True,
    # in_cluster=True,
    node_selectors={
        "CPU": "2",
        "MEM": "8",
        "app": "airflow"
    },
    dag=dag
)

t1