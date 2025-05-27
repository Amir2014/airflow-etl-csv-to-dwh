# Airflow ETL: CSV to Data Warehouse (BigQuery)

This project shows how I work with data pipelines using Apache Airflow. I created this project as an example of a basic ETL process that I have used in real scenarios—cleaning a CSV file and loading the cleaned data into BigQuery for reporting or further analysis.

It’s a simple and clear solution for automating a common data task.

## What this project does

- Reads a raw CSV file from the `data/` folder
- Cleans the data using a Python function (removes empty rows, trims values)
- Saves the cleaned version to a new CSV file
- Loads the cleaned data into BigQuery using Airflow

## Technologies used

These are the tools I use in this project:

- Apache Airflow (for workflow management)
- Python with pandas (for cleaning the data)
- Google BigQuery (as cloud data warehouse)
- Docker (to run everything locally)

## Folder structure

```
airflow-etl-csv-to-dwh/
├── dags/
│   └── etl_csv_pipeline.py       # The Airflow DAG file
├── data/
│   └── input_data.csv            # Sample input file
│   └── cleaned_data.csv          # Output after cleaning
├── docker-compose.yaml          # For local Airflow setup
├── requirements.txt             # Python packages
└── README.md                    # This file
```

## How to run this project

1. Clone this repo:
   ```bash
   git clone https://github.com/Amir2014/airflow-etl-csv-to-dwh.git
   cd airflow-etl-csv-to-dwh
   ```

2. Start Airflow using Docker:
   ```bash
   docker-compose up -d
   ```

3. Open the Airflow web UI:
   - URL: [http://localhost:8080](http://localhost:8080)
   - Login: `airflow` / `airflow`
   - Trigger the DAG named `etl_csv_pipeline`

## Customization

This project is simple, and you can change parts of it depending on your data:

- Replace the CSV file in `data/input_data.csv`
- Update the Python cleaning logic to fit your columns
- Change the BigQuery project, dataset, and table in the DAG file

## Author
**Amir Emami**  
Data & AI & BI Engineer  
[LinkedIn profile](https://www.linkedin.com/in/amir-emami-98834636/)

---

You are welcome to use or improve this example. I hope it helps you understand how to build simple and useful data workflows.
