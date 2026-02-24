import sys
import os
import pytest

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

# Run the tests from the root directory
sys.path.append(os.getcwd())

# Returning a Spark Session
@pytest.fixture() # The scope is a function level...
def spark():
    try:
        from databricks.connect import DatabricksSession
        spark = DatabricksSession.builder.getOrCreate()
    except ImportError:
        try:
            from pyspark.sql import SparkSession
            spark = SparkSession.builder.getOrCreate()
        except:
            raise ImportError("Neither Databricks Session or Spark Session are available")
    return spark