import os
from dotenv import load_dotenv
import psycopg2
import pandas as pd
load_dotenv()


# Define your API endpointcs and routes here

db_host = 'localhost'
db_port = '5432'
db_name = 'store_status'
db_user = 'postgres'
db_password=os.getenv("db_password")

# Connect to the database
conn = psycopg2.connect(
    host=db_host,
    port=db_port,
    database=db_name,
    user=db_user,
    password=db_password
)

# Create a cursor
cursor = conn.cursor()

def create_vendors_table():
    create_table_query = """
        CREATE TABLE IF NOT EXISTS store_status.vendors (
            vendor_id SERIAL PRIMARY KEY,
            vendor_name VARCHAR(255) NOT NULL
        )
    """
  
    
    cursor.execute(create_table_query)
    conn.commit()
    schema=[]
    cursor.execute(
        """
        SELECT column_name, data_type
        FROM information_schema.columns
        WHERE table_name = 'vendors'
        ORDER BY ordinal_position
        """
    )
    for row in cursor.fetchall():
        column_name, data_type = row
        schema.append({'column_name': column_name, 'data_type': data_type})
    return schema


def import_xlsx_to_database(xlsx_path, table_name):
   
    cursor.execute(f"TRUNCATE TABLE {table_name}")
    df = pd.read_csv(xlsx_path)
    data = [tuple(row) for row in df.values]

    # Generate placeholders for the SQL query
    placeholders = ','.join(['%s'] * len(df.columns))

    insert_query = f"INSERT INTO {table_name} VALUES ({placeholders})"

    # Execute the INSERT statement with the data
    cursor.executemany(insert_query, data)
    conn.commit()
    
# Close the cursor and connection
def close_connection():
    cursor.close()
    conn.close()