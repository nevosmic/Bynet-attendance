from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)
# '192.168.56.102'
#app.config['MYSQL_HOST'] = '192.168.56.102'
app.config['MYSQL_HOST'] = 'localhost'
#app.config['MYSQL_PORT'] = 22
app.config['MYSQL_USER'] = 'michalflask'
app.config['MYSQL_PASSWORD'] = '28111992'
app.config['MYSQL_DB'] = 'flaskdb'

mysql = MySQL(app)


@app.before_first_request
def init_db():
    # Creating a connection cursor
    cursor = mysql.connection.cursor()
    # Executing SQL Statements

    cursor.execute('''DROP TABLE IF EXISTS `flaskdb`.`Attendance`''')
    cursor.execute(''' CREATE TABLE `flaskdb`.`Attendance` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` TEXT NOT NULL,
  `total time` TEXT NOT NULL,
  `total percentage` TEXT NOT NULL,
  `num of meetings` TEXT NOT NULL,
  PRIMARY KEY (`id`)); ''')
    cursor.execute(''' INSERT INTO `flaskdb`.`Attendance`(`name`, `total time`, `total percentage`, `num of meetings`) VALUES (%s,%s,%s,%s) ''', ("Michal", "100", "100.0", "1"))
    mysql.connection.commit()
    mysql.connection.close()  
  
"""cursor.execute(''' INSERT INTO flaskdb.Attendance('name', 'total time', 'total percentage', 'num of meetings') VALUES (%s,%s,%s,%s)''', ("Michal", "100", "100.0", "1"))
"""


@app.route('/')
def index():
    return 'Hello world!!'


app.run(debug=True, host='0.0.0.0', port=5000)
