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

dag  = DAG(dag_id='ETL_CPU2_MEM8',
           default_args=args,
           schedule_interval=timedelta(days=1),
           tags=['Kube'],
        )

affinity = k8s.V1Affinity(
    node_affinity=k8s.V1NodeAffinity(
        preferred_during_scheduling_ignored_during_execution=[
            k8s.V1PreferredSchedulingTerm(
                weight=1,
                preference=k8s.V1NodeSelectorTerm(
                    match_expressions=[
                        k8s.V1NodeSelectorRequirement(key="CPU", operator="In", values=["2"])
                    ]
                ),
            )
        ]
    )
)

# Pod affinity with the KubernetesPodOperator
# is not supported with Composer 2
# instead, create a cluster and use the GKEStartPodOperator
# https://cloud.google.com/composer/docs/using-gke-operator
t1 = KubernetesPodOperator(
    task_id='ETL_CPU2_MEM8_TASK',
    name='ETL_CPU2_MEM8_TASK',
    namespace='airflow-cluster',
    image='perl',
    cmds=['perl'],
    arguments=['-Mbignum=bpi', '-wle', 'print bpi(2000)'],
    is_delete_operator_pod=True,
    in_cluster=True,
    # affinity allows you to constrain which nodes your pod is eligible to
    # be scheduled on, based on labels on the node. In this case, if the
    # label 'cloud.google.com/gke-nodepool' with value
    # 'nodepool-label-value' or 'nodepool-label-value2' is not found on any
    # nodes, it will fail to schedule.
    affinity=affinity,
    dag=dag
    )

t1