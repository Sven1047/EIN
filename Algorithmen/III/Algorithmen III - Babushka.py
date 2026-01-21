
babushka = ["Olga", ["Tatjana", ["Svetlana", ["Natalya", ["Katerina", ["Alina", ["Nadia"]]]]]]]
# iterativ
while(len(babushka) > 1):
    name = babushka[0]
    babushka = babushka[1]
    print("im Bauch von", name, "ist", babushka[0])
    
    
# rekursiv
def openBabushka(babushka):
    if (len(babushka) > 1):
        name = babushka[0]
        babushka = babushka[1]
        print("im Bauch von", name, "ist", babushka[0])
        openBabushka(babushka)

babushka = ["Olga", ["Tatjana", ["Svetlana", ["Natalya", ["Katerina", ["Alina", ["Nadia"]]]]]]]
openBabushka(babushka)