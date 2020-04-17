print("What's your height in cm?")
height = int(input())
height = height / 100
print(f"Your height is {height}m.")
print("What's your weight in kg?")
weight = int(input())
height_squared= height * height 
print(f"Your BMI is {weight / height_squared}.")
