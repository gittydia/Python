
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in cm: "))

bmi = weight/height**2*10000

print("Your BMI is: ", bmi)

if (bmi > 0):
    if (bmi <= 18.5):
        print("You are underweight")
    elif (bmi <= 24.9):
        print("You are normal weight")
    else:
        print("You are overweight")

