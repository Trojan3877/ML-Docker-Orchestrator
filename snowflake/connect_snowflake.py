# snowflake/connect_snowflake.py

"""
This script connects to Snowflake and fetches a dataset for ML processing.
You can later integrate this with your model training or inference pipeline.
"""

import snowflake.connector
import pandas as pd

# Snowflake credentials (replace with secrets manager or env vars in real usage)
SNOWFLAKE_USER = "your_username"
SNOWFLAKE_PASSWORD = "your_password"
SNOWFLAKE_ACCOUNT = "your_account"
SNOWFLAKE_WAREHOUSE = "COMPUTE_WH"
SNOWFLAKE_DATABASE = "ML_DB"
SNOWFLAKE_SCHEMA = "PUBLIC"

# Establish connection
conn = snowflake.connector.connect(
    user=SNOWFLAKE_USER,
    password=SNOWFLAKE_PASSWORD,
    account=SNOWFLAKE_ACCOUNT,
    warehouse=SNOWFLAKE_WAREHOUSE,
    database=SNOWFLAKE_DATABASE,
    schema=SNOWFLAKE_SCHEMA
)

# Query data
query = "SELECT * FROM CUSTOMER_FEATURES;"
df = pd.read_sql(query, conn)
print(df.head())

# Close connection
conn.close()
