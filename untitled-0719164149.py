from airflow import DAG

from airflow_notebook.pipeline import NotebookOp
from airflow.utils.dates import days_ago

# Setup default args with older date to automatically trigger when uploaded
args = {
    "project_id": "untitled-0719164149",
}

dag = DAG(
    "untitled-0719164149",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 2.2.4 pipeline editor using untitled.pipeline.",
    is_paused_upon_creation=False,
)


notebook_op_7ca054b8_6235_4826_b756_e11a0bd7ed23 = NotebookOp(
    name="load_data",
    namespace="default",
    task_id="load_data",
    notebook="examples/pipelines/hello_world/load_data.ipynb",
    cos_endpoint="http://34.64.108.55:9000/",
    cos_bucket="emart-dt-prd-datalake",
    cos_directory="untitled-0719164149",
    cos_dependencies_archive="load_data-7ca054b8-6235-4826-b756-e11a0bd7ed23.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=[],
    image="amancevice/pandas:1.1.1",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minioadmin",
        "AWS_SECRET_ACCESS_KEY": "minioadmin",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
    },
    config_file="None",
    dag=dag,
)


notebook_op_489dd75b_1bf9_42d5_a1bc_9536de078b38 = NotebookOp(
    name="Part_1___Data_Cleaning",
    namespace="default",
    task_id="Part_1___Data_Cleaning",
    notebook="examples/pipelines/hello_world/Part 1 - Data Cleaning.ipynb",
    cos_endpoint="http://34.64.108.55:9000/",
    cos_bucket="emart-dt-prd-datalake",
    cos_directory="untitled-0719164149",
    cos_dependencies_archive="Part 1 - Data Cleaning-489dd75b-1bf9-42d5-a1bc-9536de078b38.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=[],
    image="amancevice/pandas:1.1.1",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minioadmin",
        "AWS_SECRET_ACCESS_KEY": "minioadmin",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
    },
    config_file="None",
    dag=dag,
)

(
    notebook_op_489dd75b_1bf9_42d5_a1bc_9536de078b38
    << notebook_op_7ca054b8_6235_4826_b756_e11a0bd7ed23
)


notebook_op_47df13ba_e0bc_4b8a_8277_cb351aba952d = NotebookOp(
    name="Part_2___Data_Analysis",
    namespace="default",
    task_id="Part_2___Data_Analysis",
    notebook="examples/pipelines/hello_world/Part 2 - Data Analysis.ipynb",
    cos_endpoint="http://34.64.108.55:9000/",
    cos_bucket="emart-dt-prd-datalake",
    cos_directory="untitled-0719164149",
    cos_dependencies_archive="Part 2 - Data Analysis-47df13ba-e0bc-4b8a-8277-cb351aba952d.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=[],
    image="amancevice/pandas:1.1.1",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minioadmin",
        "AWS_SECRET_ACCESS_KEY": "minioadmin",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
    },
    config_file="None",
    dag=dag,
)

(
    notebook_op_47df13ba_e0bc_4b8a_8277_cb351aba952d
    << notebook_op_489dd75b_1bf9_42d5_a1bc_9536de078b38
)


notebook_op_256cd78d_f1f4_49c6_8725_bd6d5d46d8d4 = NotebookOp(
    name="Part_3___Time_Series_Forecasting",
    namespace="default",
    task_id="Part_3___Time_Series_Forecasting",
    notebook="examples/pipelines/hello_world/Part 3 - Time Series Forecasting.ipynb",
    cos_endpoint="http://34.64.108.55:9000/",
    cos_bucket="emart-dt-prd-datalake",
    cos_directory="untitled-0719164149",
    cos_dependencies_archive="Part 3 - Time Series Forecasting-256cd78d-f1f4-49c6-8725-bd6d5d46d8d4.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=[],
    image="amancevice/pandas:1.1.1",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minioadmin",
        "AWS_SECRET_ACCESS_KEY": "minioadmin",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
    },
    config_file="None",
    dag=dag,
)

(
    notebook_op_256cd78d_f1f4_49c6_8725_bd6d5d46d8d4
    << notebook_op_489dd75b_1bf9_42d5_a1bc_9536de078b38
)
