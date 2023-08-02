from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.secret_key = 'shdgad'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_USER'] = ''
app.config['MYSQL_DB'] = 'details'

mysql = MYSQL(app)

@app.route('/')
def sports_enquiry_form():
    return render_template('index.html')

@app.route('/register', methods=['GET','POST'])
def register():
    name = request.form['name']
    email = request.form['email']
    age = request.form['age']
    sports = request.form['sports']
    cursor =mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("INSERT INTO user() VALUES(%s)",(name))
    mysql.connection.commit()
    

    # Here, you can process the form data (e.g., save to a database, perform validation, etc.)

    return f'Thank you, {name}, for registering for the {sports} academy!'

if __name__ == '__main__':
    app.run(debug=True)

