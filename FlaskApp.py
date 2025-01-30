from flask import Flask,render_template

#Create Instance of Flask
app = Flask(__name__)

# homepage route
@app.route('/')
def homepage():
    return render_template('homepage.html')

if __name__ == "__main__":
    app.run(debug=True)