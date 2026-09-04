import os
import sqlite3
import pandas as pd
import pymssql  # Pure Python MSSQL driver, ideal for Linux containers

user = os.environ["DB_USER"]
password = os.environ["DB_PASS"]

print("Connecting to Celestial SQL Server...")
remote_conn = pymssql.connect(
    server="db.altiumlibrary.com",
    port=1433,
    user=user,
    password=password,
    database="altium_library",
)

local_conn = sqlite3.connect("celestial.sqlite3")

cursor = remote_conn.cursor()
cursor.execute(
    "SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE='VIEW' OR TABLE_TYPE='BASE TABLE'"
)
tables = [row[0] for row in cursor.fetchall()]

for table in tables:
    try:
        print(f"Syncing: {table}")
        df = pd.read_sql(f"SELECT * FROM [{table}]", remote_conn)
        df.to_sql(table, local_conn, if_exists="replace", index=False)
    except Exception as e:
        print(f"Skipping {table}: {e}")

remote_conn.close()
local_conn.close()
print("Done! SQLite database generated.")