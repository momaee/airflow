from pendulum import today

from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.pod import \
    KubernetesPodOperator

with DAG(
    "kubernetes",
    default_args={"owner": "airflow"},
    start_date=today().add(days=-1),
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
