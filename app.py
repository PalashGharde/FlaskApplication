from datetime import datetime
from flask import Flask, render_template, request, url_for, redirect
from Form import HealthForm
from flask_sqlalchemy import SQLAlchemy

#Create Instance of Flask
app = Flask(__name__)
app.secret_key = 'FlaskAppSecretKey'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///health_tracker.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# homepage route
@app.route('/')
def homepage():
    return render_template('homepage.html')


# Form route to collect information and upload to dataset
@app.route('/form', methods = ['POST','GET'])
def form():
    healthform = HealthForm()
    if healthform.validate_on_submit():
        date = healthform.date.data
        exercise = healthform.exercise.data
        meditation = healthform.meditation.data
        sleep = healthform.sleep.data

        return render_template('dashboard.html')

    return render_template('form.html', form=healthform)

# dashboard route
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == "__main__":
    app.run(debug=True)