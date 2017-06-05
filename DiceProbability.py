# Marvin Diaz
# programing assignment 6
# This program will be able to give frequency, relative frequency, and experimental
# probability for each sum of any amount of dice with any amount of sides

import random

rng = random.Random(237) # Create a random number generator

def throwDice(m,k):
   """
   throws m independent dice and returns the result in a m-tuple
   """
   L =[]
   for i in range(m):
      die = rng.randrange(1,k+1)
      L.append(die)

   return tuple(L)
# end ThrowTwoDice()


#-- main ----------------------------------------------------------------------   

print()
# Asks the user for the number of dice and will continue to prompt if
# the number of dice is less than 1
dice = int(input("Enter the number of dice: "))
while dice < 1:
	print("The number of dice must be at least 1")
	dice = int(input("Please enter the number of dice: "))
# print(dice)


# Asks the user for the number of sides on each die and will continue
# to prompt if input is less than 2
print()
sides = int(input("Enter the number of sides on each die: "))
while sides < 2:
	print("The number of sides on each die must be at least 2")
	sides = int(input("Please enter the number of sides on each die: "))
# print(sides)


# Asks the user for the number of trials to perform and will continue to
# prompt if input is less than 1
print()
numberOfTrials = int(input("Enter the number of trials to perform: "))
while numberOfTrials < 1:
	print("The number of trials must be at least 1")
	numberOfTrials = int(input("Please enter the number of trials to perform: "))
# print(numberOfTrials)


# perform simulation, record and print frequencies
frequency = ((dice*sides)+1)*[0]  # makes a m*k+1 list
for i in range(numberOfTrials): # Performs throwDice for said trials
   t = throwDice(dice,sides)
   sum = 0 # The total will be stored in sum
   for j in range(0,dice): 
      sum += t[j] # The values of each dice are summed together
   frequency[sum] += 1;
# end for


# calculate frequencies, relative frequencies, and experimental probability
relativeFrequency = [0, 0]
exprob = [0,0]
for i in range(2, len(frequency)):
   relativeFrequency.append(frequency[i]/numberOfTrials)
   exprob.append(frequency[i]/100)
# end for


#print(relativeFrequency)
#print(exprob)
print()


# print results
f1 = "{0:>4}     {1:<9}     {2:<18}     {3:<22}"
f2 = 70*"-"
f3 = "{0:>4}     {1:>6.0f}      {2:^18.5f}         {3:>6.2f} % "
print(f1.format("Sum","Frequency","Relative Frequency","Experimental Probability"))
print(f2)
for i in range(dice, len(frequency)):
   print(f3.format(i, frequency[i], relativeFrequency[i], exprob[i]))
#end for
print()
