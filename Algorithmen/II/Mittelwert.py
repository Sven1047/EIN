from random import *

sum = 0
numbers = []
for i in range(0,100):
    numbers.append(randint(0,1000))

for i in range(0,len(numbers)):
    sum += numbers[i]

resultat = sum/len(numbers)

print(resultat)