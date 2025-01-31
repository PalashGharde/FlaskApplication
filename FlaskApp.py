from datetime import datetime

from flask import Flask, render_template, request, url_for, redirect

from FlaskApplication.Form import HealthForm

#Create Instance of Flask
app = Flask(__name__)
app.secret_key = 'FlaskAppSecretKey'


# homepage route
@app.route('/')
def homepage():
    return render_template('homepage.html')



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

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')



users = [
    {'name': 'Palash Gharde', 'age':25},
    {'name': 'Anshul Gharde', 'age':21},
    {'name': 'Rishi Gharde', 'age':18},
    {'name': 'Ayush Gharde', 'age':16},
    {'name': 'Anuj Gharde', 'age':10}
]

@app.route('/userlist')
def userlist():
    return render_template('userlist.html', title = "List of Users", usersList = users)


if __name__ == "__main__":
    app.run(debug=True)