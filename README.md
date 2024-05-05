# Airflow

This is a simple repo to work with Apache Airflow.

## Install Airflow

```bash
export AIRFLOW_HOME=~/airflow

AIRFLOW_VERSION=2.9.0

PYTHON_VERSION="$(python -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')"


CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"

pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"
```

Please note you may don't have `python` but `python3` in your system. In that case, you need to replace `python` with `python3` in the above command.

## Check Installation

```bash
airflow version

airflow info
```

## Check db connection

```bash
airflow db check
```

## Add [dags](dags) folder to ~/airflow/airflow.cfg

First, check the current `airflow.cfg` file. If it's empty, you can add the following lines to it.

```bash
[core]
dags_folder = /path/to/this/repo/dags
```

Please note that you need to replace `/path/to/this/repo` with the actual absolute path to this repo. You can get the absolute path by running the following command in the terminal.

```bash
pwd
```

## Start Airflow

```bash
airflow standalone
```

You should see the credentials for the default user. You can change the password for the default user by editing the `standalone_admin_password.txt` file.

## Access Airflow

Open a browser and go to `http://localhost:8080/`

You should see the Airflow UI with all the example dags and your dags, too!

## Hide Example Dags

To hide the example dags, you can add the following line to the `airflow.cfg` file.

```bash
[core]
load_examples = False
```

Then you need to reset the database.

```bash
airflow db reset
```

## Kubernetes DAG

For running the Kubernetes DAG locally, you need to install `kubectl` and `minikube`.

### Kubectl

You can use this [link](https://kubernetes.io/docs/tasks/tools/) to install `kubectl`.

### Minikube

You can use this [link](https://minikube.sigs.k8s.io/docs/start/) to install `minikube`.

### Start minikube

After installing `kubectl` and `minikube`, you can start the minikube cluster by running the following command.

```bash
minikube start
```

Then you should see the minikube cluster running by running the following command.

```bash
kubectl get nodes
```

or

```bash
kubectl cluster-info
```

### Install Airflow Provider for Kubernetes

Now you need to install the Airflow provider for Kubernetes.

```bash
pip install apache-airflow-providers-cncf-kubernetes
```

### Run the Kubernetes DAG

Now you can run the Kubernetes DAG by going to the Airflow UI and turning on the `kubernetes` DAG. Every time you run the DAG, it will create a new pod in the minikube cluster and run the task in that pod. The pod will be deleted after the task is done. To catch the logs of the pod, you can use the following command.

```bash
watch kubectl get pods -A 
```
