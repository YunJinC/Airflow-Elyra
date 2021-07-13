from airflow import DAG

from airflow_notebook.pipeline import NotebookOp
from airflow.utils.dates import days_ago

# Setup default args with older date to automatically trigger when uploaded
args = {
    "project_id": "untitled-0713170159",
}

dag = DAG(
    "untitled-0713170159",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 2.2.4 pipeline editor using untitled.pipeline.",
    is_paused_upon_creation=False,
)


notebook_op_5d6a08a7_8102_42cb_ba0b_26e6beb3fd3a = NotebookOp(
    name="load_data",
    namespace="admin",
    task_id="load_data",
    notebook="examples/pipelines/hello_world/load_data.ipynb",
    cos_endpoint="http://34.64.108.55:9000",
    cos_bucket="emart-dt-prd-datalake",
    cos_directory="untitled-0713170159",
    cos_dependencies_archive="load_data-5d6a08a7-8102-42cb-ba0b-26e6beb3fd3a.tar.gz",
    pipeline_outputs=["data/noaa-weather-data-jfk-airport/jfk_weather.csv"],
    pipeline_inputs=[],
    image="amancevice/pandas:1.1.1",
    resources={
        "request_cpu": "1",
    },
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minioadmin",
        "AWS_SECRET_ACCESS_KEY": "minioadmin",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "DATASET_URL": "https://dax-cdn.cdn.appdomain.cloud/dax-fashion-mnist/1.0.2/fashion-mnist.tar.gz",
    },
    config_file="None",
    dag=dag,
)


notebook_op_d1e5ffd8_982e_4d29_aa3d_07a1cab4c770 = NotebookOp(
    name="Part_1___Data_Cleaning",
    namespace="admin",
    task_id="Part_1___Data_Cleaning",
    notebook="examples/pipelines/hello_world/Part 1 - Data Cleaning.ipynb",
    cos_endpoint="http://34.64.108.55:9000",
    cos_bucket="emart-dt-prd-datalake",
    cos_directory="untitled-0713170159",
    cos_dependencies_archive="Part 1 - Data Cleaning-d1e5ffd8-982e-4d29-aa3d-07a1cab4c770.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=["data/noaa-weather-data-jfk-airport/jfk_weather.csv"],
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
    notebook_op_d1e5ffd8_982e_4d29_aa3d_07a1cab4c770
    << notebook_op_5d6a08a7_8102_42cb_ba0b_26e6beb3fd3a
)


notebook_op_45954798_d268_412e_93cb_2f97acd73793 = NotebookOp(
    name="Part_2___Data_Analysis",
    namespace="admin",
    task_id="Part_2___Data_Analysis",
    notebook="examples/pipelines/hello_world/Part 2 - Data Analysis.ipynb",
    cos_endpoint="http://34.64.108.55:9000",
    cos_bucket="emart-dt-prd-datalake",
    cos_directory="untitled-0713170159",
    cos_dependencies_archive="Part 2 - Data Analysis-45954798-d268-412e-93cb-2f97acd73793.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=["data/noaa-weather-data-jfk-airport/jfk_weather.csv"],
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
    notebook_op_45954798_d268_412e_93cb_2f97acd73793
    << notebook_op_d1e5ffd8_982e_4d29_aa3d_07a1cab4c770
)


notebook_op_846106b5_a056_4281_90d7_8cddd15d4636 = NotebookOp(
    name="Part_3___Time_Series_Forecasting",
    namespace="admin",
    task_id="Part_3___Time_Series_Forecasting",
    notebook="examples/pipelines/hello_world/Part 3 - Time Series Forecasting.ipynb",
    cos_endpoint="http://34.64.108.55:9000",
    cos_bucket="emart-dt-prd-datalake",
    cos_directory="untitled-0713170159",
    cos_dependencies_archive="Part 3 - Time Series Forecasting-846106b5-a056-4281-90d7-8cddd15d4636.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=["data/noaa-weather-data-jfk-airport/jfk_weather.csv"],
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
    notebook_op_846106b5_a056_4281_90d7_8cddd15d4636
    << notebook_op_d1e5ffd8_982e_4d29_aa3d_07a1cab4c770
)
