from flask_wtf import FlaskForm
from wtforms import IntegerField, DateField, SubmitField
from wtforms.validators import InputRequired, NumberRange

class HealthForm(FlaskForm):
    date = DateField('Date', format='%Y-%m-%d')
    exercise = IntegerField('Workout session (minutes)',validators=[InputRequired(),NumberRange()])
    meditation = IntegerField('Meditation session (minutes)',validators=[InputRequired(),NumberRange()])
    sleep = IntegerField('Sleep session (hours)',validators=[InputRequired(),NumberRange()])
    submit = SubmitField('Submit')

