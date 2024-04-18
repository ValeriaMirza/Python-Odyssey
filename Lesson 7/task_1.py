# Aceasta este sarcina pentru lecția 7 legată de comentarii, continuarea liniilor și instrucțiuni condiționale.

# Creați o variabilă numită number și atribuiți-i o valoare întreagă.

# CODUL TĂU VINE MAI JOS:
number = 7
# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă numărul este pozitiv și afișați un mesaj corespunzător.

# CODUL TĂU VINE MAI JOS:
if(number > 0):
    print("Numarul este pozitiv.")
    
# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă numărul este par și afișați un mesaj corespunzător.

# CODUL TĂU VINE MAI JOS:
if(number % 2 == 0):
    print("Numarul este par.")
# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă numărul este impar și afișați un mesaj corespunzător.

# CODUL TĂU VINE MAI JOS:
if(number % 2 != 0):
    print("Numarul este impar.")
# CODUL TĂU VINE MAI SUS:

# Creați o variabilă text și atribuiți-i un șir de caractere.

# CODUL TĂU VINE MAI JOS:
text = "un sir de caractere care contine cuvantul Python"
# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă textul conține cuvântul "Python" și afișați un mesaj corespunzător.

# CODUL TĂU VINE MAI JOS:
if ("Python" in text):
    print("Cuvantul Python apartine sirului de caractere.")
# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă textul conține cuvântul "Java" și afișați un mesaj corespunzător.

# CODUL TĂU VINE MAI JOS:
if ("Java" in text):
    print("Cuvantul java apartine sirului de caractere.")
# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă textul conține cuvântul "Python" și afișați un mesaj corespunzător.
# în cazul în care nu conține, verificați dacă conține cuvântul "Java" și afișați un mesaj corespunzător.
# Dacă nu conține niciunul dintre ele, afișați un mesaj corespunzător.

# CODUL TĂU VINE MAI JOS:
if ("Python" in text):
    print("Cuvantul Python apartine sirului de caractere.")
elif("Java" in text):
    print("Cuvantul Java apartine sirului de caractere.")
else:
    print("Sirul de caractere nu contine cuvintele Python si Java.")

# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă textul conține cuvântul "Python" și cuvântul "Java" și afișați un mesaj corespunzător.
# În cazul în care conține doar unul dintre ele, afișați un mesaj corespunzător.
# Dacă nu conține niciunul dintre ele, afișați un mesaj corespunzător.

# CODUL TĂU VINE MAI JOS:
if ("Python" in text and "Java" in text):
    print("Cuvantul Python si Java apartin sirului de caractere.")
elif("Python" in text or "Java" in text):
    print("Unul din cuvintele Java ai Python apartin sirului de caractere")
else:
    print("Sirul de caractere nu contine cuvintele Python si Java.")


# CODUL TĂU VINE MAI SUS:

# Extrageți de la tastatură utilizând funcția input un număr de la 1 la 5 și atribuiți-l variabilei number.
# Folosiți o instrucțiune condițională pentru a printa un mesaj corespunzător în funcție de numărul introdus.
# pentru 1 - printați "Unu"
# pentru 2 - printați "Doi"
# pentru 3 - printați "Trei"
# pentru 4 - printați "Patru"
# pentru 5 - printați "Cinci"

# CODUL TĂU VINE MAI JOS:
user_input = int(input("Introdu un numar intre 1 si 5: "))
if(user_input == 1):
    print("pentru 1 - printați \"Unu\" ")
elif(user_input == 2):
    print("pentru 2 - printați \"Doi\" ")
elif(user_input == 3):
    print("pentru 3 - printați \"Trei\" ")
elif(user_input == 4):
    print("pentru 4 - printați \"Patru\" ")
elif(user_input == 5):
    print("pentru 1 - printați \"Cinci\" ")
# CODUL TĂU VINE MAI SUS:


