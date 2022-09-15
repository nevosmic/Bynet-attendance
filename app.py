import os

from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
from csv_handler import *



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
  `emails` VARCHAR(200) NOT NULL,
  `names` VARCHAR(200) NOT NULL,
  `total time` VARCHAR(200) NOT NULL,
  `average` VARCHAR(200) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `emails_UNIQUE` (`emails` ASC) VISIBLE); ''')
    cursor.execute(''' INSERT INTO `flaskdb`.`Attendance`(`emails`, `names`, `total time`, `average`) VALUES (%s,%s,%s,%s)''', ("mimi@gamil.com", "Mimi", "650", "100 %"))
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
    vm_path = '/home/nevosmic/Flask-Proj/Bynet-attendance/static/files/example.csv'
    path = 'static/files/attendance.csv'
    init_db()
    # create_example_students_csv(vm_path)
    read_from_csv(path, mysql)
    
@app.route('/')
def show_students():
    # get students from db:
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM `flaskdb`.`Attendance` ''')
    students = cur.fetchall()
    print(students)
    return render_template('students.html', data=students)

app.run(debug=True, host='0.0.0.0', port=5000)
