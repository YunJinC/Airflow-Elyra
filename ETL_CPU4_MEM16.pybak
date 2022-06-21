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
    'start_date': days_ago(1),
#    'on_failure_callback' : alert.slack_fail_alert,
     }

dag  = DAG(dag_id='ETL_CPU4_MEM16',
           default_args=args,
           schedule_interval=timedelta(days=1),
           tags=['Kube'],
        )

# Pod affinity with the KubernetesPodOperator
# is not supported with Composer 2
# instead, create a cluster and use the GKEStartPodOperator
# https://cloud.google.com/composer/docs/using-gke-operator
t1 = KubernetesPodOperator(
    task_id='ETL_CPU4_MEM16_TASK',
    name='ETL_CPU4_MEM16_TASK',
    namespace='airflow-cluster',
    image='perl',
    cmds=['perl'],
    arguments=['-Mbignum=bpi', '-wle', 'print bpi(2000)'],
    dag=dag
    )

t1