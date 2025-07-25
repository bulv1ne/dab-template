# Databricks notebook source

# from pyspark.sql import functions as F, types as T

# COMMAND ----------

# Get the base_parameters from the job
input_table_name = dbutils.widgets.get("input_table_name")
checkpoint_path = dbutils.widgets.get("checkpoint_path")
table_name = dbutils.widgets.get("table_name")

# COMMAND ----------

# Read and write
stream = (
    spark.readStream.table(input_table_name)
    # Transformations
    # Write your transformations here
    # ...
    # Write
    .writeStream.option("checkpointLocation", checkpoint_path)
    .option("mergeSchema", "true")
    .trigger(availableNow=True)
    .toTable(table_name)
)

stream.awaitTermination()
