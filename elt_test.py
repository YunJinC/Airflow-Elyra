from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
import pendulum
from datetime import datetime
from utils.alert import SlackAlert
from airflow.utils.trigger_rule import TriggerRule

alert = SlackAlert()
KST = pendulum.timezone("Asia/Seoul")

args = {
    'owner': 'airflow', 
    'start_date': datetime(2021, 6, 7, tzinfo=KST),
#    'on_failure_callback' : alert.slack_fail_alert,
     }

dag  = DAG(dag_id='elt_test2',
           default_args=args,
           schedule_interval='00 06 * * *')

t1 = BashOperator(task_id='test_task1',
                  bash_command='gcloud compute ssh "fast-elt-001" --zone "asia-northeast3-a" --project "smart-ruler-304409" --command "ls"',
                  trigger_rule=TriggerRule.ALL_DONE,
                  dag=dag)

t2 = BashOperator(task_id='test_task2',
                  bash_command='gcloud compute ssh "fast-elt-001" --zone "asia-northeast3-a" --project "smart-ruler-304409" --command "le"',
                  trigger_rule=TriggerRule.ALL_DONE,
                  dag=dag)

t3 = BashOperator(task_id='test_task3',
                  bash_command='gcloud compute ssh "fast-elt-001" --zone "asia-northeast3-a" --project "smart-ruler-304409" --command "ls"',
                  trigger_rule=TriggerRule.ALL_DONE,
                  dag=dag)

t1 >> t2 >> t3