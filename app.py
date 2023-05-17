from flask import Flask, jsonify, request
import psycopg2
import random
import os
from dotenv import load_dotenv
from dbconn import conn,close_connection

#create_vendors_table()

#create_table_query()
# Load environment variables from .env file
cursor=conn.cursor()
a=""
if(conn is not None and cursor):
  a="connection established"
else:
    a="no connection"
app=Flask(__name__)
@app.route('/')
def home():
    return "hey"

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
# @app.route('/csv-to-json', methods=['GET'])
# def csv_to_json():
#     csv_file = 'C:\Users\prrra\Desktop\store status.csv'  # Replace with the path to your CSV file
    
#     # Read the CSV file
#     data = []
#     with open(csv_file, 'r') as file:
#         reader = csv_file.DictReader(file)
#         for row in reader:
#             data.append(row)
    
#     # Return the data in JSON format
#     return jsonify(data)



if __name__ == '__main__':
    app.run(port=8080,debug=True)
    close_connection()
