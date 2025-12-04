mass = int(input("Enter your body mass in KG: "))
height = int(input("Enter your height in  meters: "))


height = height / 100
BMI = mass / (height ** 2)

print(f"Your BMI is {round(BMI, 2)}")

if BMI < 18.5:
    print("you are underweight")
elif BMI < 25:
    print("you are normal")
elif BMI < 30:
    print("you are overweight")
else :
    print("you are obese")
