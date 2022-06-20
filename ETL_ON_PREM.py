from airflow.models import DAG
from airflow.utils.dates import days_ago
from airflow.operators.bash_operator import BashOperator
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

dag  = DAG(dag_id='ETL_ON_PREM',
           default_args=args,
           schedule_interval=timedelta(days=1),
           tags=['Kube'],
        )

t1 = BashOperator(task_id='task1',
                  bash_command='echo "ETL on-prem"',
                  trigger_rule=TriggerRule.ALL_DONE,
                  dag=dag)

t1