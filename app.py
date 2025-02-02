from datetime import datetime
from flask import Flask, render_template, request, url_for, redirect
from Form import HealthForm, SignupForm
from flask_sqlalchemy import SQLAlchemy, Model

#Create Instance of Flask
app = Flask(__name__)
app.secret_key = 'FlaskAppSecretKey'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///health_tracker2.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(150), nullable=False, unique=True)
    lastname = db.Column(db.String(150), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    age = db.Column(db.Integer)

class HealthData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    exercise = db.Column(db.Integer, nullable=False)
    meditation = db.Column(db.Integer, nullable=False)
    sleep = db.Column(db.Integer, nullable=False)

def __repr__(self):
    return f'<HealthData(self.id)>'

# homepage route
@app.route('/')
def homepage():
    return render_template('homepage.html')


@app.route('/signup', methods = ['POST','GET'])
def signup():
    signupForm = SignupForm()
    if signupForm.validate_on_submit():
        firstname = signupForm.firstname.data
        lastname = signupForm.lastname.data
        email = signupForm.email.data
        age = signupForm.age.data

        new_user = User(firstname=firstname, lastname=lastname, email=email, age=age)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('success',firstname = firstname, lastname= lastname, email=email))
    return render_template('signup.html', form=signupForm)

@app.route('/success')
def success():
    firstname = request.args.get('firstname')
    lastname = request.args.get('lastname')
    email = request.args.get('email')

    return render_template('success.html',firstname=firstname,lastname=lastname,email=email)

@app.route('/users')
def users():
    all_users= User.query.all()
    return render_template('users.html', users = all_users)

# Form route to collect information and upload to dataset
@app.route('/form', methods = ['POST','GET'])
def form():
    healthform = HealthForm()
    if healthform.validate_on_submit():
        date = healthform.date.data
        exercise = healthform.exercise.data
        meditation = healthform.meditation.data
        sleep = healthform.sleep.data

        health_data = HealthData(date=date, exercise=exercise, meditation=meditation, sleep=sleep)
        db.session.add(health_data)
        db.session.commit()

        return redirect(url_for('dashboard'))
    return render_template('form.html', form=healthform)

# dashboard route
@app.route('/dashboard')
def dashboard():
    all_data = HealthData.query.all()
    return render_template('dashboard.html', all_data = all_data)

if __name__ == "__main__":
    app.run(debug=True)