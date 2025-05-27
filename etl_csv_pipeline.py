#---------------------------------------------------------------------------------------------------------#
# dags/etl_csv_pipeline.py
# Author: Amir Emami                                                                                
# Description: Simple ETL workflow that cleans CSV data and loads it to BigQuery using Apache Airflow     
#---------------------------------------------------------------------------------------------------------#
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.google.cloud.operators.bigquery import BigQueryInsertJobOperator
from datetime import datetime
import pandas as pd

# Clean the CSV file: remove empty rows and standardize one column

def clean_csv():
    # Load the file
    df = pd.read_csv('/opt/airflow/dags/data/input_data.csv')

    # Remove rows with missing data
    df.dropna(inplace=True)

    # Clean a specific column (you can change this column name)
    df['cleaned_column'] = df['original_column'].str.strip().str.lower()

    # Save to new file
    df.to_csv('/opt/airflow/dags/data/cleaned_data.csv', index=False)


# DAG config

default_args = {
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
}

# Define the workflow
with DAG(
    dag_id='etl_csv_pipeline',
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
    description='A simple ETL pipeline: clean a CSV file and load it to BigQuery',
) as dag:

    # Step 1: Clean the file with Python
    clean_task = PythonOperator(
        task_id='clean_csv_file',
        python_callable=clean_csv
    )

    # Step 2: Load the cleaned file to BigQuery (update project, dataset, and table)
    load_to_bq = BigQueryInsertJobOperator(
        task_id="load_cleaned_csv_to_bq",
        configuration={
            "load": {
                "sourceUris": ["gs://your-bucket-name/cleaned_data.csv"],
                "destinationTable": {
                    "projectId": "your-gcp-project",
                    "datasetId": "your_dataset",
                    "tableId": "your_table",
                },
                "sourceFormat": "CSV",
                "skipLeadingRows": 1,
                "writeDisposition": "WRITE_TRUNCATE",
                "autodetect": True,
            }
        },
        gcp_conn_id='google_cloud_default'
    )

    # Run cleaning first, then load to BQ
    clean_task >> load_to_bq
