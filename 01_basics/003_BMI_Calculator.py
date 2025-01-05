height = float(input("Enter your height in CM: "))
weight = float(input("Enter your weight in KG: "))

bmi = weight / ((height / 100) ** 2)

print(bmi)

if(bmi < 18.5):
    print('Under weight')
elif(18.5 <= bmi < 25):
    print('Normal weight')
elif(25 <= bmi < 30):
    print('Over weight')
else:
    print('Obese')