import random
import time

LIST_SIZE = 10000
TRIALS_PER_LISTSIZE = 10

def bubble_sort(liste):
    n = len(liste)
    for i in range(n):
        for j in range(0, n-1):
            # Tausche, wenn grösser als das nächste
            if liste[j] > liste[j+1]:
                temp = liste[j]
                liste[j] = liste[j+1]
                liste[j+1] = temp
    return liste

# Generiere eine Liste von Zufallszahlen
numbers = []
for num in range(LIST_SIZE):
    numbers.append(num)

time_needed_per_trial = []
for i in range(TRIALS_PER_LISTSIZE):
    
    # Randomisieren der Zahlen
    random.shuffle(numbers)

    # Starte die Zeitmessung
    start_time = time.time()

    # Aufruf des Algorithmus
    sorted_numbers = bubble_sort(numbers)

    # Beende die Zeitmessung
    end_time = time.time()

    # Berechne die benötigte Zeit: end_time - start_time
    time_needed = end_time - start_time

    # Millisekunden
    milliseconds = time_needed * 1000
    time_needed_per_trial.append(milliseconds)
    print("Lauf Nr.",i, ":", milliseconds, "(Millisekunden)")


average = sum(time_needed_per_trial)/len(time_needed_per_trial)

print("Durchschnitt: Benötigte Zeit für die Sortierung von: ", LIST_SIZE, " Zahlen (in Millisekunden): ", average )



