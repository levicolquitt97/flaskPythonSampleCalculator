# LEVI COLQUITT
# Assignment 3+4 STQA
# 3/15/2020
# FORMS.py
# This .py file creates the forms and grabs the user input. then it passes that to the main.py file for further use
from flask_wtf import FlaskForm

from wtforms import StringField, IntegerField, DecimalField, SubmitField

from wtforms.validators import DataRequired, Length, InputRequired, NumberRange
[]
# Form that takes input for BMI page and also validates the input
class BMIForm(FlaskForm):
    heightFeet = IntegerField('Height feet', validators=[InputRequired(), NumberRange(min=1, max=12)])
    heightInches = IntegerField('Height inches', validators=[InputRequired(), NumberRange(min=0, max=12)])
    weight = DecimalField('Weight in pounds', validators=[DataRequired(message='MUST BE VALID DECIMAL/INTEGER VALUE'), NumberRange(min=0, max=1000)])
    submit = SubmitField('Calculate')

# Form that takes input for retirement page and also validates the input
class retirementForm(FlaskForm):
    age = IntegerField('Current age:', validators=[InputRequired(), NumberRange(min=0, max=99)])
    salary = IntegerField('Annual salary in $:', validators=[InputRequired(), NumberRange(min=0)])
    percentSaved = IntegerField('Enter annual percent of salary saved:', validators=[InputRequired(), NumberRange(min=0, max=99)])
    desiredSavingsGoal = IntegerField('Enter your desired savings goal:', validators=[InputRequired(), NumberRange(min=0)])
    submit = SubmitField('Calculate')

