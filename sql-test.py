import pandas as pd
import pyodbc
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

connection = "DRIVER={ODBC Driver 17 for SQL Server};SERVER={test-server};DATABASE={test-db};UID={test};PWD={test}"
con = pyodbc.connect(connection)
con.timeout = 3
data = pd.read_sql("select * from Student", con)
print(str(data))

url = URL.create("mssql+pyodbc", query={"odbc_connect": connection})
sqlDb = create_engine(url, connect_args={'remote login timeout': 1, 'Remote Query Timeout': 1})
data = pd.read_sql("exec test_sp", sqlDb)
print(str(data))
