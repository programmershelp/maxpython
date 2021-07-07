#BMI Categories:
#Underweight = &lt;18.5
#Normal weight = 18.5–24.9
#Overweight = 25–29.9
#Obesity = BMI of 30 or greater 

weight = float(input('Please enter your weight in pounds: '))
height = float(input('Please enter your height in inches: '))

BMI = weight * 703 / (height ** 2)

if BMI < 18.5:
    print('Your body mass index (BMI) is', format(BMI, '.2f'), 'Your weight is defined as underweight')
elif BMI > 18.5 and BMI < 25:
    print('Your body mass index (BMI) is', format(BMI, '.2f'), 'Your weight is defined as normal')
elif BMI > 25 and BMI < 30:
    print('Your body mass index (BMI) is', format(BMI, '.2f'), 'Your weight is defined as overweight')
else:
    print('Your body mass index (BMI) is', format(BMI, '.2f'), 'Your weight is defined as Obesity.')