from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.pod import \
    KubernetesPodOperator
from airflow.utils.dates import days_ago

with DAG(
    "kubernetes",
    default_args={"owner": "airflow"},
    schedule_interval=None,
    start_date=days_ago(2),
    tags=["example"],
) as dag:
    k = KubernetesPodOperator(
        name="hello-world",
        image="alpine",
        cmds=["echo"],
        arguments=["hello world"],
        labels={"foo": "bar"},
        task_id="run_hello_world",
        do_xcom_push=True,
    )

    k


# k = KubernetesPodOperator(
#     name="hello-dry-run",
#     image="debian",
#     cmds=["bash", "-cx"],
#     arguments=["echo", "10"],
#     labels={"foo": "bar"},
#     task_id="dry_run_demo",
#     do_xcom_push=True,
# )

# k.dry_run()
