from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

from sales_pipeline import (
    extraire_ventes,
    valider_ventes,
    transformer_ventes,
    generer_rapport
)

with DAG(
    dag_id="sales_pipeline",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
) as dag:

    extract = PythonOperator(
        task_id="extract",
        python_callable=extraire_ventes
    )

    validate = PythonOperator(
        task_id="validate",
        python_callable=valider_ventes
    )

    transform = PythonOperator(
        task_id="transform",
        python_callable=transformer_ventes
    )

    report = PythonOperator(
        task_id="report",
        python_callable=generer_rapport
    )

    extract >> validate >> transform >> report
