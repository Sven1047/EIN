zahlen = [1,5,6,2,3,8,6,3,2,4]

def sum_rek(summe, liste):
    if len(liste) == 0:
        return summe
    else:
        erstes = liste.pop(0)
        summe = erstes + sum_rek(summe, liste)
        return summe
    
ergebnis = sum_rek(0, zahlen)
print("Die Summe der Zahlen ist:", ergebnis)
