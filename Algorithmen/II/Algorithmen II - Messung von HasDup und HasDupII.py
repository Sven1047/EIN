import random
import time


LIST_SIZE = 10000
TRIALS_PER_LISTSIZE = 10

def hasDup(numbers):
    for x in range(0,len(numbers)):
        for y in range(0,len(numbers)):
            if numbers[x] == numbers[y] and x!=y:
                return True
    return False


def hasDupII(numbers):
    already_seen_list = []
    for i in range(max(numbers)+1):
        already_seen_list.append(False)
    
    for x in range(0,len(numbers)):
        num = numbers[x]
        if already_seen_list[num] == True:
            return True
        else:
            already_seen_list[num] = True
    
    return False

# Generiere eine Liste von Zufallszahlen
numbers = []
for num in range(LIST_SIZE):
    numbers.append(num)

time_needed_per_trial_I = []
time_needed_per_trial_II = []

for i in range(TRIALS_PER_LISTSIZE):
    print("Lauf Nr.",i, " berechne beide Methoden")
    # We make a copy of the list
    numbers_trial = numbers.copy()
    # We add a 50% chance of a duplicate 0 in the list
    if random.randint(0,1)==0:
        index = random.randint(LIST_SIZE//2, LIST_SIZE-1)
        numbers_trial[index] = 0
    
    # Randomisieren der Zahlen
    random.shuffle(numbers_trial)
    
    # Starte die Zeitmessung
    start_time_I = time.time()
    hasOrNot_I = hasDup(numbers_trial)
    # Beende die Zeitmessung
    end_time_I = time.time()
    # Berechne die benötigte Zeit
    time_needed_I = end_time_I - start_time_I
    
    
    # Starte die Zeitmessung II
    start_time_II = time.time()
    hasOrNot_II = hasDupII(numbers_trial)
    # Beende die Zeitmessung
    end_time_II = time.time()
    # Berechne die benötigte Zeit
    time_needed_II = end_time_II - start_time_II


    # Millisekunden
    milliseconds_I = time_needed_I * 1000
    time_needed_per_trial_I.append(milliseconds_I)
    
    # Millisekunden
    milliseconds_II = time_needed_II * 1000
    time_needed_per_trial_II.append(milliseconds_II)

for i in range(len(time_needed_per_trial_I)):
    print("Lauf Nr.",i, ":", time_needed_per_trial_I[i], "(Millisekunden)")


average_I = sum(time_needed_per_trial_I)/len(time_needed_per_trial_I)
print("Durchschnitt: Benötigte Zeit für Die Duplikaterkennung von: ", LIST_SIZE, " Zahlen (in Millisekunden): ", average_I )

print("\n")

for i in range(len(time_needed_per_trial_II)):
    print("Lauf Nr.",i, ":", time_needed_per_trial_II[i], "(Millisekunden)")

average_II = sum(time_needed_per_trial_II)/len(time_needed_per_trial_II)
print("Durchschnitt: Benötigte Zeit für Die Duplikaterkennung von: ", LIST_SIZE, " Zahlen (in Millisekunden): ", average_II )

print("\n")





