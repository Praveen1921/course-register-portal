from flask import Flask, render_template, request, redirect, session, flash
from werkzeug.security import check_password_hash
import mysql.connector
import pymysql


app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="root",         # Change if needed
    password="karthi@2006",         # Change if your MySQL has a password
    database="alagappa_db"
)
cursor = db.cursor()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/course')
def course():
    return render_template('course.html')

@app.route('/course1')
def course1():
    return render_template('course1.html')

@app.route('/course2')
def course2():
    return render_template('course2.html')

@app.route('/course3')
def course3():
    return render_template('course3.html')

@app.route('/course4')
def course4():
    return render_template('course4.html')

@app.route('/course5')
def course5():
    return render_template('course5.html')

@app.route('/course6')
def course6():
    return render_template('course6.html')

@app.route('/course7')
def course7():
    return render_template('course7.html')

@app.route('/course8')
def course8():
    return render_template('course8.html')

@app.route('/course9')
def course9():
    return render_template('course9.html')

@app.route('/course10')
def course10():
    return render_template('course10.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = request.form
        sql = """
        INSERT INTO registrations(
            student_name, email, course_id, gender,
            phone_number, Aadhar_no,
            Tamil, English, CS_Bio, Mathematics, Chemistry, Physics, cutoff
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (
            data['student_name'], data['email'], data['course_id'], data['gender'],
            data['phone_number'], data['Aadhar_no'],
            data['Tamil'], data['English'], data['Computer Science/Biology'],
            data['Mathematics'], data['Chemistry'], data['Physics'], data['cutoff']
        )
        cursor.execute(sql, values)
        db.commit()
        return render_template("message.html", name=data['student_name'])
    return render_template('register.html')

@app.route('/message')
def message():
    return render_template('message.html')


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        email = request.form.get('email')
        password_input = request.form.get('password')

        # ✅ Manual check — skip database
        if email == 'admin@123' and password_input == '1234':
            session['admin'] = email
            flash('Login successful.', 'success')
            return redirect('/admin_view')
        else:
            flash('Invalid email or password.', 'danger')
            return redirect('/admin')

    return render_template('admin.html')

# Route: View Registered Students
@app.route('/admin_view', methods=['GET'])
def admin_view():
    if 'admin' not in session:
        return redirect('/admin')

    try:
        # Get query parameters
        course_name = request.args.get('course_name', '').strip()
        gender = request.args.get('gender', '').strip()
        cutoff = request.args.get('cutoff', '').strip()

        # Build SQL dynamically
        query = "SELECT * FROM registrations WHERE 1=1"
        params = []

        if course_name:
            query += " AND course_id LIKE %s"
            params.append(f"%{course_name}%")

        if gender:
            query += " AND gender = %s"
            params.append(gender)

        if cutoff:
            try:
                cutoff_value = int(cutoff)
                query += " AND cutoff >= %s"
                params.append(cutoff_value)
            except ValueError:
                pass  # Ignore invalid cutoff value

        cursor.execute(query, tuple(params))
        records = cursor.fetchall()

        return render_template(
            'admin_view.html',
            records=records,
            selected_course=course_name,
            selected_gender=gender,
            selected_cutoff=cutoff
        )

    except Exception as e:
        return f"Error: {e}"


@app.route('/admin/logout')
def admin_logout():
    session.pop('admin', None)
    return redirect('/admin')


if __name__ == '__main__':
    app.run(debug=True)
