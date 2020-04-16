types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}." #this formats the binary variable into the strign

print(x) #this prints the whole of x including what is formatted
print(y)

print(f"I said: {x}") #This prints the whole of x as well as including I said 
print(f"I also said: '{y}'")

hilarious = False #boolean?
joke_evaluation = "Isn't that joke so funny?! {}" # the variable is left empty

print(joke_evaluation.format(hilarious)) # .format adds the variable into the blank space

w = "This is the left side of..."
e = "a string with a right side."

print(w + e) # this prints both and w and e together on the same line.
