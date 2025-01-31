from flask import Flask, render_template, request, url_for, redirect

#Create Instance of Flask
app = Flask(__name__)

# homepage route
@app.route('/')
def homepage():
    return render_template('homepage.html')



@app.route('/form', methods = ['POST','GET'])
def form():
    if request.method == "POST":
        return redirect(url_for('dashboard'))

    return render_template('form.html')

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