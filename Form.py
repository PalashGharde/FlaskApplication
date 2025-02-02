from flask_wtf import FlaskForm
from wtforms import IntegerField, DateField, SubmitField, StringField
from wtforms.validators import InputRequired, NumberRange, Email



# Creates Health form with important fields
class HealthForm(FlaskForm):
    date = DateField('Date', format='%Y-%m-%d')
    exercise = IntegerField('Workout session (minutes)',validators=[InputRequired(),NumberRange()])
    meditation = IntegerField('Meditation session (minutes)',validators=[InputRequired(),NumberRange()])
    sleep = IntegerField('Sleep session (hours)',validators=[InputRequired(),NumberRange()])
    submit = SubmitField('Submit')

# Creates SignUp form with important information
class SignupForm(FlaskForm):
    firstname = StringField('Firstname',validators=[InputRequired()])
    lastname = StringField('Lastname',validators=[InputRequired()])
    email = StringField('Email',validators=[InputRequired(), Email()])
    age = IntegerField('Age',validators=[InputRequired(),NumberRange()])
    submit = SubmitField('Submit')

