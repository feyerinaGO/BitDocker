from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route('/')
def get_table():
    config = {'user': 'root',
              'password': '01234567',
              'host': 'db',
              'database': 'mysql_db'
              }
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    sql_reader = "SELECT name, age FROM Persons"
    cursor.execute(sql_reader)
    records = cursor.fetchall()
    result = {}
    for i in range(len(records)):
        result[i] = {'name': records[i][0], 'age': records[i][1]}
    return str(result)


@app.route('/health')
def is_health():
    return '{"status": "OK"}'


# @app.errorhandler(404)
# def page_not_found(e):
#     return '404'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)