from databricks.connect import DatabricksSession

#spark = DatabricksSession.builder.getOrCreate()
spark = DatabricksSession.builder.remote(serverless=True).getOrCreate()
#spark = DatabricksSession.builder.remote(cluster_id="<cluster_id>").getOrCreate()

spark.sql("select 1").show()