import os
from dotenv import load_dotenv
import psycopg2

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

# def create_vendors_table():
#     create_table_query = """
#         CREATE TABLE IF NOT EXISTS public.vendors (
#             vendor_id SERIAL PRIMARY KEY,
#             vendor_name VARCHAR(255) NOT NULL
#         )
#     """
    
#     cursor.execute(create_table_query)
#     conn.commit()


# Close the cursor and connection
def close_connection():
    cursor.close()
    conn.close()