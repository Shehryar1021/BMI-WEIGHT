height= float (input("ENTER YOUR HEIGHT IN CM: "))
weight= float (input("ENTER YOUR WEIGHT IN KG: "))

BMI = weight / (height/100)**2

print("YOUR BMI IS". BMI)

if BMI <= 18.4:
print("YOU ARE UNDERWEIGHT.")
elif BMI <= 24.9
print("YOU ARE HEALTHY.")
elif BMI <= 29.9
print("YOU ARE OVER WEIGHT.")
elif BMI <= 34.9
print("YOU ARE SURELY OVERWEIGHT.")
elif BMI <= 39.9
print("YOU ARE OBESE.")
else:
print("YOU ARE SEVERLY OBESE.")
