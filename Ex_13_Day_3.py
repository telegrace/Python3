from sys import argv
# read the WYSS section for how to run this 
script, month , second, third = argv 

print("The script is called:", script)
print("Your first variable is:", month)
print("Your second variable is:", second)
print("Your third variable is:", third)

#modules = libraries, and variables pass data to other 'activities' and arguments pass to other 'workflows'

day = input("What day is today? ")
print(f"I love {day}.")
