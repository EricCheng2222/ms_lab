





weight_str = input("how much do you weigh(kg)? ")
height_str = input("how tall are you(cm)? ")

weight = int(weight_str)
height = int(height_str)

height_meter = height / 100

bmi = weight / (height_meter * height_meter)

print("your BMI is: " + str(bmi))
