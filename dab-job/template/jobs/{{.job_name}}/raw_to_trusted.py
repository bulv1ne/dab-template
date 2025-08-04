# Databricks notebook source

# from pyspark.sql import functions as F, types as T

# COMMAND ----------

# Get the base_parameters from the job
input_table_name = dbutils.widgets.get("raw_table_name")
checkpoint_path = dbutils.widgets.get("checkpoint_path")
table_name = dbutils.widgets.get("trusted_table_name")

# COMMAND ----------


def transform_dataframe(df):
    """
    Apply transformations to the input DataFrame.
    Modify this function to include your specific transformations.
    """
    # Example transformation: Add a new column with a constant value
    # df = df.withColumn("new_column", F.lit("constant_value"))

    # Return the transformed DataFrame
    return df


# COMMAND ----------

# Read and write
stream = (
    spark.readStream.table(input_table_name)
    # Transformations
    .transform(transform_dataframe)
    # Write
    .writeStream.option("checkpointLocation", checkpoint_path)
    .option("mergeSchema", "true")
    .trigger(availableNow=True)
    .toTable(table_name)
)

stream.awaitTermination()
