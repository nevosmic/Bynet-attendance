from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)
# '192.168.56.102'
app.config['MYSQL_HOST'] = '192.168.56.102'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_USER'] = 'michalflask'
app.config['MYSQL_PASSWORD'] = '28111992'
app.config['MYSQL_DB'] = 'flaskdb'

#mysql = MySQL(app)

"""
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
"""

@app.route('/')
def index():
    return 'Hello world!!'


app.run(debug=True, host='0.0.0.0', port=5000)
