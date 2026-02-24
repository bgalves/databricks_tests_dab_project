
import os
import sys

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

try:
    from databricks.connect import DatabricksSession
    spark = DatabricksSession.builder.getOrCreate()
except ImportError:
    try:
        from pyspark.sql import SparkSession
        spark = SparkSession.builder.getOrCreate()
    except:
        raise ImportError("Neither Databricks Session or Spark Session are available")