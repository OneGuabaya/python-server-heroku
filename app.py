#!pip install psycopg2
#!pip install Flask
import psycopg2
from psycopg2.extras import RealDictCursor
from datetime import datetime
from flask import Flask
from flask import jsonify
from flask_cors import CORS, cross_origin
import os




DB_NAME = "postgres" #to be changed
DB_USERNAME = "postgres" #to be changed
DB_PASSWORD = "hellothisisapasswordandihopeitsstrongenough2021" #to be changed


def try_connect(host_value,database_value,user_value,password_value):
    print("\n\n")
    print("Connecting... ")
    conn = psycopg2.connect(host=host_value, database=database_value, user=user_value, password=password_value)
    print("Connected!", datetime.now())
    return conn

def select_my_datas(host_value,sql_statement,mode_select=True):
    my_connection = try_connect(host_value,DB_NAME,DB_USERNAME,DB_PASSWORD)
    # create a cursor
    cur = my_connection.cursor(cursor_factory=RealDictCursor)

    # execute a statement
    cur.execute(sql_statement)

    # display the PostgreSQL database results
    if(mode_select==True):
        db_results = cur.fetchall()
    # if not a select statement: commits to update the database
    else:
        db_results = my_connection.commit()


    # close the communication with the PostgreSQL
    cur.connection.close()
    cur.close()

    # return datas as a JSON object
    return jsonify(db_results)

# nothing but hello world on home
def home():    
    return "HELLO WORLD!"



app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'






######################### LOCALHOST HERE

@app.route('/<string:host_value>/<string:sql_statement>')
def give_results(host_value,sql_statement):
    print(host_value)
    print(sql_statement)
    return select_my_datas(host_value,sql_statement)

@app.route('/')
def welcome():
    return home()



@app.route('/<string:host_value>/<string:sql_statement>/<string:mode_select>')
def give_results_no_select(host_value,sql_statement,mode_select):
    print("***************** CORS *******************")
    print(host_value)
    print(sql_statement)
    return select_my_datas(host_value,sql_statement,False)

######################### END OF LOCALHOST HERE













######################### CORS HERE

@app.route('/')
@cross_origin()
def welcome_cors():
    return home()

@app.route('/<string:host_value>/<string:sql_statement>')
@cross_origin()
def give_results_with_cors(host_value,sql_statement):
    print("***************** CORS *******************")
    print(host_value)
    print(sql_statement)
    return select_my_datas(host_value,sql_statement)

@app.route('/<string:host_value>/<string:sql_statement>/<string:mode_select>')
@cross_origin()
def give_results_with_cors_no_select(host_value,sql_statement,mode_select):
    print("***************** CORS *******************")
    print(host_value)
    print(sql_statement)
    return select_my_datas(host_value,sql_statement,mode_select)


######################### END OF CORS HERE













# to run this file locally, execute python app.py
# then go to : https://127.0.0.1:5000/
# and discard all security alerts as it's run on localhost
if __name__ == "__main__":
  context=('cert.pem', 'key.pem') #certificate and key files
  app.run(debug=True, ssl_context=context)