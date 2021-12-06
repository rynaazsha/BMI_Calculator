# 🚨 Don't change the code below 👇


#h_convert = (float(height))
#print (type(h))


#w_convert = (float(weight))
#print (type(w))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
height = float(input("enter your height in m: "))
#if (height == ""):
  #print (" To Calculate BMI, Height cannot be empty!")
  #height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
  #if (weight == ""):
    #print (" To Calculate BMI, Weight cannot be empty!")
    #weight = float(input("enter your weight in kg: "))
BMI = float(weight) / (float(height) ** 2)
BMI = round(BMI,2)
print(BMI)
if (BMI <= 18.5):
  print(f"Your BMI is {BMI} and you are Under weight")
elif (BMI >18.5) and (BMI <= 25):
  print (f"Your BMI is {BMI} and you are Normal weight")
elif (BMI > 25) and (BMI <= 30):
  print (f"Your BMI is {BMI} and you are Over weight")
elif (BMI > 30) and (BMI <= 35):
  print (f"Your BMI is {BMI} and you are Obese")
else:
  print (f"You BMI is {BMI} and you are Clinically Obese")