# Databricks notebook source

# from pyspark.sql import functions as F, types as T

# COMMAND ----------

# Get the base_parameters from the job
input_path = dbutils.widgets.get("input_path")
checkpoint_path = dbutils.widgets.get("checkpoint_path")
table_name = dbutils.widgets.get("raw_table_name")

# COMMAND ----------

# Read and write
stream = (
    spark.readStream.format("cloudFiles")
    .option("cloudFiles.format", "json")
    .option("cloudFiles.inferColumnTypes", "false")
    .option("cloudFiles.schemaEvolutionMode", "addNewColumns")
    .option("cloudFiles.schemaLocation", checkpoint_path)
    .load(input_path)
    # Write
    .writeStream.option("checkpointLocation", checkpoint_path)
    .option("mergeSchema", "true")
    .trigger(availableNow=True)
    .toTable(table_name)
)

stream.awaitTermination()
