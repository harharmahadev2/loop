from flask import Flask, jsonify, request
import psycopg2
import random
import os
from dotenv import load_dotenv
from dbconn import conn,close_connection,create_vendors_table,import_xlsx_to_database

#create_vendors_table()

#create_table_query()
# Load environment variables from .env file
cursor=conn.cursor()
#schema=create_vendors_table()
a=""
if(conn is not None):
  a="connection established"
else:
    a="no connection"
app=Flask(__name__)
@app.route('/')
def home():
    return "hey"


@app.route('/table_schema')
def table_schema():
    schema = create_vendors_table()
    return jsonify({'table_schema': schema})

@app.route('/trigger',methods=['GET'])
def report_trigger():
    randomnumber=random.randint(1,1000000)
    return str(randomnumber)

@app.route('/get_report', methods=['GET'])
def get_report():
    report_id = request.args.get('report_id')
    data={
        'status':'running',
        'type of connection':a

    }
    return jsonify(data)

@app.route('/import_data')
def import_data():
    xlsx_path = 'C:\\Users\\prrra\\Desktop\\Menu hours.csv' # Update with your XLSX file path
    table_name = 'store_status.menu_hours'  # Update with your table name
    import_xlsx_to_database(xlsx_path, table_name)
    return "Data imported successfully"



if __name__ == '__main__':
    app.run(port=8080,debug=True)
    close_connection()
