# from flask import Flask, render_template, request, redirect
# import mysql.connector

# app = Flask(__name__)

# # MySQL Configuration
# db = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="Vini@01",  # Change if you set a password
#     database="alagappa_db"
# )
# cursor = db.cursor()

# @app.route('/')
# def home():
#     return render_template('home.html')

# @app.route('/course')
# def course():
#     return render_template('course.html')

# @app.route('/admin')
# def admin():
#     return render_template('admin.html')

# @app.route('/about')
# def about():
#     return render_template('about.html')

# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         data = request.form
#         sql = """
#         INSERT INTO student_registration (
#             student_name, email, course_id, gender,
#             phone_number, Aadhar_no, Tamil, English, CS_Bio,
#             Mathematics, Chemistry, Physics, cutoff
#         ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
#         """
#         values = (
#             data['student_name'], data['email'], data['course_id'], data['gender'],
#             data['phone_number'], data['Aadhar_no'], data['Tamil'], data['English'],
#             data['Computer Science/Biology'], data['Mathematics'], data['Chemistry'],
#             data['Physics'], data['cutoff']
#         )
#         cursor.execute(sql, values)
#         db.commit()
#         return "Registration successful!"
#     return render_template('register.html')

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="root",       # Update if your username is different
    password="",       # Update if you set a password
    database="alagappa_db"
)
cursor = db.cursor()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = request.form
        sql = """
        INSERT INTO student_registration (
            student_name, email, course_id, gender,
            phone_number, Aadhar_no,
            Tamil, English, CS_Bio, Mathematics, Chemistry, Physics, cutoff
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (
            data['student_name'],
            data['email'],
            data['course_id'],
            data['gender'],
            data['phone_number'],
            data['Aadhar_no'],
            data['Tamil'],
            data['English'],
            data['Computer Science/Biology'],
            data['Mathematics'],
            data['Chemistry'],
            data['Physics'],
            data['cutoff']
        )
        cursor.execute(sql, values)
        db.commit()
        return render_template("message.html", name=data['student_name'])
    return render_template('register.html')

@app.route('/message')
def message():
    return render_template('message.html')

# You can also define other routes as needed
@app.route('/course')
def course():
    return render_template('course.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

if __name__ == '__main__':
    app.run(debug=True)
