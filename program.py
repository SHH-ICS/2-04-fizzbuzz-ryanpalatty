# My Python Program
# Task:  use if statements to output the result of the game fizzbuzz.  
# Start at 1
# For multiples of 3, output   Fizz
# For multiples of 5, output   Buzz
# For multiples of 15, output   FizzBuzz
# End at 32


#this is what i came up with

 for myNumber in range(1, 32):
    if(myNumber % 3 == 0 and myNumber % 5 == 0):
        print("FizzBuzz") 
    elif(myNumber % 3 == 0):
        print("Fizz")
    elif(myNumber % 5 == 0):
        print("Buzz")
    else:
        print(myNumber)




# This is was what came in the page

for X in range(1, 32):


result = ""
for myNumber in range(32):
  result = str(result) + str(myNumber) + "\n"

print(result)
