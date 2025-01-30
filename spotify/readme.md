This is a personal project aimed at extracting data from the Spotify public API and transforming it and loading it to postgres database. Here we have extracted data for artist Anirudh. Free API limits are applied which is 50 requests per transaction. Data will be converted into python pandas dataframe and then loaded to postgres database

Workflow Completed:
1. Extracted data from Spotify API for artist Anirudh
2. Transformed data and loaded to postgres database
3. Visualized data using streamlit

Future Work:
1. Automate the process of extracting data from Spotify API using Apache Airflow
2. Create Delta lake
3. Intoduce Pyspark for ETL
4. Introduce flink for ETL
5. Introduce DBT for ETL