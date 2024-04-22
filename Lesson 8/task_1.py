# Aceasta este tema pentru lecția 8 legată de loops

# Creați o listă de numere de la 1 la 10 folosind un for loop și funcția range().

# CODUL TĂU VINE MAI JOS:
lista = []
for i in range(10):
    lista.append(i+1)
# CODUL TĂU VINE MAI SUS:

# Folosind un for loop, parcurgeți lista creată și afișați numai numerele pare.

# CODUL TĂU VINE MAI JOS:
for i in range(len(lista)):
    if(lista[i] % 2 == 0):
        print(lista[i])

# CODUL TĂU VINE MAI SUS:

# Folosind un while loop, creați o variabilă 'i' inițializată cu 1 și incrementați-o până când ajunge la 5. Afișați valoarea 'i' la fiecare pas.

# CODUL TĂU VINE MAI JOS:
i = 1
while(i<5):
    i = i + 1
    print(i)
# CODUL TĂU VINE MAI SUS:

# Creați un dicționar person cu cheile 'name', 'age' și 'city' și iterați prin dicționar afișând perechile de cheie-valoare.

# CODUL TĂU VINE MAI JOS:
dictionar = {"name" : "Valeria", "age" : 21, "city" : "Chisinau"}
for items in dictionar.items():
    print(items)
# CODUL TĂU VINE MAI SUS:

# Utilizați un for loop pentru a itera printr-o listă de liste (matrice) și afișați fiecare element.

# CODUL TĂU VINE MAI JOS:
matrix = [[1,2,3],[4,5,6],[7,8,9]]
for row in matrix:
    for x in row:
        print(x)
# CODUL TĂU VINE MAI SUS:

# Creați o secvență de numere folosind funcția range() și apoi iterați prin această secvență folosind un for loop pentru a afișa numerele.

# CODUL TĂU VINE MAI JOS:
numere = range(10)
for x in numere:
    print(x)
# CODUL TĂU VINE MAI SUS:

# Folosiți funcția enumerate() pentru a itera printr-o listă și a afișa indexul fiecărui element alături de valoarea sa.

# CODUL TĂU VINE MAI JOS:
list=[1,2,3,4,5,6,7,8,9]
for i in enumerate(list):
    print(i)
# CODUL TĂU VINE MAI SUS:

# Folosiți funcția zip() pentru a itera simultan prin două liste și a afișa elementele corespunzătoare.

# CODUL TĂU VINE MAI JOS:
lista_nume = ["Ana", "Irina", "Ion"]
lista_varsta = [12,32,41]

for x in zip(lista_nume,lista_varsta):
    print(x)
# CODUL TĂU VINE MAI SUS:

# Creați o listă de numere de la 1 la 10 folosind un for loop și funcția range().

# CODUL TĂU VINE MAI JOS:
lista = []
for i in range(10):
    lista.append(i+1)
# CODUL TĂU VINE MAI SUS:

# Folosind un buclă while, dublează valorile listei până când primul element va deveni mai mare decât 50.

# CODUL TĂU VINE MAI JOS:
while(lista[0]<50):
    for x in range(len(lista)):
        lista[x] = lista[x] * 2
# CODUL TĂU VINE MAI SUS:

# Generează și printează o listă cu toate numerele pătrat perfect din intervalul [1, 100].

# CODUL TĂU VINE MAI JOS:
lista_patrat_perfect = []
for i in range(10):
    lista_patrat_perfect.append(i*i)
print(lista_patrat_perfect)
# CODUL TĂU VINE MAI SUS:

# Folosind un buclă for , printează tabla înmulțirii pentru numărul 7.

# CODUL TĂU VINE MAI JOS:
for i in range(11):
    print(str(i) + " * 7 = " + str(i*7))
# CODUL TĂU VINE MAI SUS:

# Creează o listă de liste, unde fiecare sub-listă conține perechi (i, j) pentru i și j de la 1 la 5. Printează această listă de perechi.

# CODUL TĂU VINE MAI JOS:
list_of_lists = []
for i in range(1,6):
    for j in range(1,6):
        list_of_lists.append([i,j])
print(list_of_lists)
# CODUL TĂU VINE MAI SUS:

# Parcurge lista de la punctul anterior și printează doar perechile unde i < j .

# CODUL TĂU VINE MAI JOS:
for i in list_of_lists:
    if(i[0]<i[1]):
        print(i)  
# CODUL TĂU VINE MAI SUS:

# Folosind un buclă while , caută și printează prima valoare care este mai mare decât 10 dintr-o listă cu numere random creată de tine. Dacă nu există, printează "Nu există valori mai mari decât 10".

# CODUL TĂU VINE MAI JOS:
lista = [1,17,34,2,5,19,22,1]
i=0
numar = 0
while(i < len(lista)):
    if lista[i]>10:
        numar = lista[i]
        print(str(numar) + " este mai mare decat 10.")
        break
    i = i+1
if(numar == 0):
    print("Nu există valori mai mari decât 10.")
# CODUL TĂU VINE MAI SUS:
# Folosind loop-uri Creează un pătrat de stele ( * ) folosind bucle încadrate. Dimensiunea pătratului va fi citită de la utilizator.
# Exemplu pentru un pătrat de dimensiune 5:
# *****
# *****
# *****
# *****
# *****

# CODUL TĂU VINE MAI JOS:
dimensiune_patrat = int(input("Introdu dimensiunea patratului: "))
for i in range(dimensiune_patrat):
    for i in range(dimensiune_patrat):
        print("*", end ="")
    print("\n",end ="")
# CODUL TĂU VINE MAI SUS:

# Folosind for sau while loops realizați afișările de mai jos

# Afișarea 1:
# 1
# 12
# 123
# 1234
# 12345
# 123456

# CODUL TĂU VINE MAI JOS:
numar = int(input("Introdu un numar: "))
i=""
iter=1
while(iter<numar + 1):
    i = i + str(iter)
    print(i)
    iter=iter+1
# CODUL TĂU VINE MAI SUS:

# Afișarea 2:

# 54321
# 5432
# 543
# 54
# 5

# CODUL TĂU VINE MAI JOS:
numar = int(input("Introdu un numar: "))
sir = ""
for i in range(numar,0,-1):
    sir = sir + str(i)

for i in range(numar):
    print(sir)
    sir = sir[:-1]
    i = i+1
# CODUL TĂU VINE MAI SUS:

# Afișarea 3:

# abcdefg
# bcdefg
# cdefg
# defg
# efg
# fg
# g

# CODUL TĂU VINE MAI JOS:
sir1 = ""
sir3 = "a"
numar_litere = 7

for i in range(numar_litere,0,-1):
    sir1 = sir1 + sir3
    sir3 = chr(ord(sir3) + 1)

for i in range(numar_litere):
    print(sir1)
    sir1 = sir1[1:]
    i = i+1
# CODUL TĂU VINE MAI SUS:

# Afișarea 4:

# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+
# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+
# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+
# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+

# CODUL TĂU VINE MAI JOS:
plus = "+"
minus = "-"
for i in range(8):
    for j in range(16):
        if(j % 2 == 0):
            print(plus,end="")
        else:
            print(minus,end="")
    if(i % 2 == 0):
        plus ="-"
        minus = "+"
    else:
        plus = "+"
        minus = "-"
    print("\n",end="")
# CODUL TĂU VINE MAI SUS:

# Afișarea 5:

# 3
# 3 9
# 3 9 27
# 3 9 27 81
# 3 9 27 81 243
# 9 27 81 243
# 27 81 243
# 81 243
# 243

# CODUL TĂU VINE MAI JOS:
sir4 = input("Introdu un numar:")
nr = int(sir4)
lenght = nr + 1
for i in range(lenght):
    nr = nr * 3
    sir4 = sir4+" "+str(nr)
    print(sir4)
    
for i in range(lenght):
    index = sir4.find(" ")
    index = index + 1
    sir4 = sir4[index:]
    print(sir4)
    i = i+1
# CODUL TĂU VINE MAI SUS:

# Completați sarcinile de mai sus pentru a exersa lucrul cu buclele în Python.
