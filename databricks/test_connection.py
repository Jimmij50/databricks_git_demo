import os
from pathlib import Path
from dotenv import load_dotenv

# Load auth injected by the VS Code Databricks extension
env_file = Path(__file__).parent.parent / ".databricks" / ".databricks.env"
load_dotenv(env_file, override=True)

from databricks.connect import DatabricksSession

print(f"Host : {os.environ.get('DATABRICKS_HOST')}")
print(f"Auth : {os.environ.get('DATABRICKS_AUTH_TYPE')}")
print()

spark = DatabricksSession.builder.getOrCreate()
print(f"Spark version: {spark.version}")
print()

spark.sql("SELECT 1 AS test, 'connection ok' AS status").show()
