import mysql.connector
import pandas as pd

config = {'user': 'root',
          'password': '01234567',
          'host': 'db'
          }

try:
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS mysql_db")
except mysql.connector.Error as err:
    print("Failed: {}".format(err))

# config with the new database
config = {'user': 'root',
          'password': '01234567',
          'host': 'db',
          'database': 'mysql_db'
          }

try:
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()

    # create table
    sql_drop = "DROP TABLE IF EXISTS Persons"
    sql_create = '''CREATE TABLE IF NOT EXISTS Persons (
                        id int PRIMARY KEY AUTO_INCREMENT,
                        name varchar(255),
                        age int
                    );'''

    sql_insert = """INSERT INTO persons(name, age) VALUES("%s", "%s")"""
    sql_reader = "SELECT name, age FROM Persons"

    cursor.execute(sql_drop)
    cursor.execute(sql_create)

    # read csv and insert data from it to the created table
    df = pd.read_csv('data/data.csv')
    for i in range(df.shape[0]):
        cursor.execute(sql_insert, [df.loc[i][0], int(df.loc[i][1])])

    # get inserted data
    cursor.execute(sql_reader)
    records = cursor.fetchall()
    cnx.commit()
    cursor.close()

    # print inserted data to console
    print(records)

except mysql.connector.Error as err:
    print("Failed: {}".format(err))
    exit(1)