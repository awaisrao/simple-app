import os
from flask import Flask,redirect, request, render_template, request, url_for
from flaskext.mysql import MySQL      # For newer versions of flask-mysql 
# from flask.ext.mysql import MySQL   # For older versions of flask-mysql
app = Flask(__name__)

mysql = MySQL()

mysql_database_host = 'MYSQL_DATABASE_HOST' in os.environ and os.environ['MYSQL_DATABASE_HOST'] or  'localhost'

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Root@123'
app.config['MYSQL_DATABASE_DB'] = 'student_db'
app.config['MYSQL_DATABASE_HOST'] = mysql_database_host
mysql.init_app(app)

conn = mysql.connect()

cursor = conn.cursor()

#@app.route("/")
#def main():
#    return "Welcome!"


@app.route("/",methods=['GET','POST'])
def read():
    if request.method == 'POST' and 'name' in request.form and 'student_class' in request.form and 'age' in request.form and 'address' in request.form:
       nm = request.form['name']
       sc = request.form['student_class']
       ag = request.form['age']
       addr = request.form['address']
       cursor.execute("INSERT INTO students VALUES (%s,%s,%s,%s)",(nm,sc,ag,addr))
    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()
    return render_template('index.html',data=records)

@app.route('/delete/<string:name>', methods=['POST'])
def remove(name):
   cursor.execute("DELETE FROM students where name=%s",name)
   return redirect (url_for('read'))

if __name__ == "__main__":
    app.run()


