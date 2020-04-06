# LEVI COLQUITT
# Assignment 3+4 STQA
# 3/15/2020
#MAIN.py
# this .py file will manage all the routing for the flask application and will also handle sending the calculated values to the user
from calculator import *
from flask import Flask, render_template, url_for, flash, redirect, request
from forms import retirementForm, BMIForm


app = Flask(__name__)

app.config['SECRET_KEY'] = 'c5c59457ae5d80cb7572580c2ce0546d'


@app.route('/')
@app.route('/home')
def homePage():
    return render_template('home.html', title='HOME')


@app.route('/about')
def aboutPage():
    return render_template('about.html', title='About')



#ROUTE for BMI page. ON success or failure this page routes only to itself.
#This form will assign some values and then pass what is gathered from user input and pass it to the calculator
@app.route('/BMI', methods=['GET','POST'])
def BMI():
    form = BMIForm()
    if form.validate_on_submit():
        #assigning preliminary values and then passing it to calculator
        BMIvalue = 0
        weight_category = str('hi')
        feet = int(request.form['heightFeet'])
        inches = int(request.form['heightInches'])
        weight = float(request.form['weight'])
        calc = BMICalc(feet, inches, weight, BMIvalue, weight_category)
        #formatting returned values from Calc function
        calcPrinter = str(calc)
        calc2 = calcPrinter.replace('(', ' ')
        calc3 = calc2.replace(')', ' ')
        calc4 = calc3.replace("'", ' ')
        calc = calc3
        # success message with calculated information
        flash(f'Calculated BMI: {calc}!', 'success')
        return redirect(url_for('BMI'))
    return render_template('BMI.html', title='BMI', form=form)

#ROUTE for Retirement page. ON success or failure this page routes only to itself.
#This form will assign some values and then pass what is gathered from user input and pass it to the calculator
@app.route('/retirement', methods=['GET','POST'])
def retirement():
    form = retirementForm()
    if form.validate_on_submit():
        savingsPrinter = str('hi')
        age = int(request.form['age'])
        salary = int(request.form['salary'])
        percentSaved = int(request.form['percentSaved'])
        desiredSavingsGoal = int(request.form['desiredSavingsGoal'])
        rCalc = retirementCalc(age, salary, percentSaved, desiredSavingsGoal, savingsPrinter)
        # formatting returned values from Calc function
        if rCalc == 0:
            flash(f'Tried to calculate but the goal cannot be met during avg life expectancy (100 y.o.)... Therefore: {rCalc}!', 'danger')

        calcPrinter = str(rCalc)
        calc2 = calcPrinter.replace('(', ' ')
        calc3 = calc2.replace(')', ' ')
        calc4 = calc3.replace("'", "")
        calc5 = calc4.replace(",", "")
        rCalc = calc4
        #success message with calculated information
        flash(f'Calculated: {rCalc}!', 'success')
        return redirect(url_for('retirement'))
    return render_template('retirement.html', title='retirement', form=form)



if __name__ == '__main__':
    app.run(debug=True)


