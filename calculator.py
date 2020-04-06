
#LEVI COLQUITT
#Assignment 2 STQA
#3/15/2020
#The following code will calculate the BMI or retirement savings as dictated by the user

#BEGIN

#BMI class that will calculate our BMI given input in feet, inches, and pounds
def BMICalc(feet, inches, weight, BMIvalue, weight_category):

    #Math to convert to metric
    feet_in_inches = (feet * 12)
    height = (feet_in_inches + inches)
    metric_height = (height * .025)
    print(metric_height)
    metric_weight = (weight * .45)
    print(metric_weight)
    height_squared = float(metric_height * metric_height)
    BMIvalue = (metric_weight/height_squared)

    #Determines "health" category based upon BMI
    if BMIvalue <= 18.5:
        weight_category = ' weight category: Underweight'
    if BMIvalue > 18.5 and BMIvalue <= 24.9:
        weight_category = ' weight category: Normal weight'
    if BMIvalue >= 25 and BMIvalue <= 29.9:
        weight_category = ' weight category: Overweight'
    if BMIvalue > 29.9:
        weight_category = ' weight category: Obese'



    #Print results to user
    return BMIvalue, weight_category



def retirementCalc(age, salary, percentSaved, desiredSavingsGoal, savingsPrinter):

    #variables needed for the loop and to count up savings plus employer match
    i = int(0)
    savings = int(0)
    employer_match = .35
    while i <= (100-age):

        savings = float((salary * (percentSaved/100)) + savings)
        bonus = ((salary*(percentSaved/100)) *.35)
        savings = savings + bonus
        age += 1
        if savings >= desiredSavingsGoal:
            savings = str(savings)
            age = str(age)
            desiredSavingsGoal = str(desiredSavingsGoal)
            savingsPrinter = ("You will have saved: $"+savings+" By age: "+age+" Which meets your savings goal of: $"+desiredSavingsGoal)
            return savingsPrinter
            i = int(101)