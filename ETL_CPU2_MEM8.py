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
    task_id='ex-pod-affinity',
    name='ex-pod-affinity',
    namespace='airflow-cluster',
    image='perl',
    cmds=['perl'],
    arguments=['-Mbignum=bpi', '-wle', 'print bpi(2000)'],
    # affinity allows you to constrain which nodes your pod is eligible to
    # be scheduled on, based on labels on the node. In this case, if the
    # label 'cloud.google.com/gke-nodepool' with value
    # 'nodepool-label-value' or 'nodepool-label-value2' is not found on any
    # nodes, it will fail to schedule.
    affinity={
        'nodeAffinity': {
            # requiredDuringSchedulingIgnoredDuringExecution means in order
            # for a pod to be scheduled on a node, the node must have the
            # specified labels. However, if labels on a node change at
            # runtime such that the affinity rules on a pod are no longer
            # met, the pod will still continue to run on the node.
            'requiredDuringSchedulingIgnoredDuringExecution': {
                'nodeSelectorTerms': [{
                    'matchExpressions': [{
                        # When nodepools are created in Google Kubernetes
                        # Engine, the nodes inside of that nodepool are
                        # automatically assigned the label
                        # 'cloud.google.com/gke-nodepool' with the value of
                        # the nodepool's name.
                        'key': 'cloud.google.com/gke-nodepool',
                        'operator': 'In',
                        # The label key's value that pods can be scheduled
                        # on.
                        'values': [
                            'user-pool-cpu2-mem8',
                        ]
                    }]
                }]
            }
        }
    },
    dag=dag
    )

t1