import os

from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
from create_csv import *



app = Flask(__name__)

app.config.from_object('config')

mysql = MySQL(app)
def init_db():
    # Creating a connection cursor
    cursor = mysql.connection.cursor()
    mysql.connection.ping(True) 
    # Executing SQL Statements
    cursor.execute('''DROP TABLE IF EXISTS `flaskdb`.`Attendance`''')
    cursor.execute(''' CREATE TABLE `flaskdb`.`Attendance` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` TEXT NOT NULL,
  `total time` TEXT NOT NULL,
  `total percentage` TEXT NOT NULL,
  `num of meetings` TEXT NOT NULL,
  PRIMARY KEY (`id`)); ''')

    cursor.execute(''' INSERT INTO `flaskdb`.`Attendance`(`name`, `total time`, `total percentage`, `num of meetings`) VALUES (%s,%s,%s,%s)''', ("Michal", "650", "100.0", "2"))
    mysql.connection.commit()


# Upload folder
UPLOAD_FOLDER = 'static/files'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# Upload URL
@app.route('/upload')
def upload():
    # Set The upload HTML template '\templates\index.html'
    return render_template('index.html')


# Get the uploaded files
@app.route("/upload", methods=['POST'])
def upload_files():
    # get the uploaded file
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
        # set the file path
        uploaded_file.save(file_path)
        # save the file
    return redirect(url_for('index'))



@app.before_first_request
def init():
    init_db()
    create_example_students_csv('/home/nevosmic/Flask-Proj/Bynet-attendance/static/files/example.csv')
    read_from_csv('/home/nevosmic/Flask-Proj/Bynet-attendance/static/files/example.csv', mysql)
    
@app.route('/')
def index():
    return 'Hello world!!'


app.run(debug=True, host='0.0.0.0', port=5000)
