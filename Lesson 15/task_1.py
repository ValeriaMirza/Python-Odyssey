# Aceasta este sarcina pentru lecția despre polimorfism, metode speciale și compoziție a claselor în Python.

from sigmoid_check.python_odyssey.lesson_15.lesson_15 import Lesson15

# Această temă pentru acasă necesită instalarea librăriei `sigmoid_check` cu versiunea cel puțin 0.0.8
# Pentru a instala această librărie, rulați următorul cod în terminal:
# pip install sigmoid_check==0.0.8

# VERIFICATION PROCESS
session = Lesson15()
# VERIFICATION PROCESS

"""
ISTORIA DIN SPATE
După toată munca depusă pentru proiectul de la DARWIN și TechSolutions, ai primit o ofertă de la cei de la Microsoft, 
aceștia lucrează la crearea unui algoritm care le va permite procesarea a unor cantități mari de date.
"""

"""
Primul pas în crearea algoritmului este implementarea unor containere de date care va permite stocarea și manipularea datelor într-un mod mai simplu
și eficient. Trebuie să creezi o clasă nouă `DataContainer`. Pentru a manipula datele vom folosi metodele speciale ale clasei.

Clasa va primi ca parametru o listă de numere integer.
- __init__ initializează clasa cu lista de numere.
- __str__ va returna lista de numere sub formă de string.
- __len__ va returna numărul de elemente din listă.
- __getitem__ va permite accesarea elementelor din listă folosind indexul (e.g., container[0]).
- __setitem__ va permite modificarea elementelor din listă folosind indexul (e.g., container[0] = 5).
- __add__ va permite combinarea a două instanțe de `DataContainer` într-o singură instanță.
"""

# CODUL TĂU VINE MAI JOS:
class DataContainer:
    def __init__(self,lista):
        self.lista = lista
    def __str__(self):
        return str(self.lista)
    def __len__(self):
        return len(self.lista)
    def __getitem__(self,index):
        return self.lista[index]
    def __setitem__(self,index,value):
        self.lista[index] = value
    def __add__(self,obj):
        return DataContainer(self.lista + obj.lista)

# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_1(DataContainer))
# VERIFICATION PROCESS

"""
Acum avem nevoie de o modalitate de a calcula suma și produsul containerului de date. Pentru aceasta creează două clase noi care vor moșteni clasa `DataContainer`.
- `SumaContainer` va calcula suma elementelor din listă.
- `ProdusContainer` va calcula produsul elementelor din listă.
Ambele clase vor avea metoda `calculate` care va returna suma sau produsul elementelor.
"""

# CODUL TĂU VINE MAI JOS:
class SumaContainer(DataContainer):
    def __init__(self,lista):
        super().__init__(lista)
        
    def calculate(self):
        suma = 0
        for x in self.lista:
            suma += x
        return suma

    
class ProdusContainer(DataContainer):
    def __init__(self,lista):
        super().__init__(lista)
        
    def calculate(self):
        produs = 1
        for x in self.lista:
            produs *= x
        return produs
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_2(SumaContainer, ProdusContainer, DataContainer))
# VERIFICATION PROCESS

"""
Pentru ca instrumentul pe care îl folosim să fie complet vom mai avea nevoie de careva adiții.
Creează o clasă `DataAnalysis` care va primi ca input o listă de obiecte de tipul `DataContainer`.
- __init__ va inițializa clasa cu lista de obiecte.
- `add_container` va permite adăugarea unui nou container în listă.
- `__call__` va returna o listă cu valorile maxime ale fiecărui container.
"""

# CODUL TĂU VINE MAI JOS:
class DataAnalysis:
    def __init__(self,lista_obiecte):
        self.lista_obiecte = lista_obiecte
    def add_container(self,new_container):
        self.lista_obiecte.append(new_container)
    def __call__(self):
        return [max(obiect) for obiect in self.lista_obiecte]
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_3(DataAnalysis, DataContainer))
# VERIFICATION PROCESS

"""
Pe lângă elementul de analiză a datelor, Microsoft a mai cerut și un element de statistică.
Creează o clasă `DataStatistics` care va primi ca input o listă de obiecte de tipul `DataContainer`.
- __init__ va inițializa clasa cu lista de obiecte.
- `add_container` va permite adăugarea unui nou container în listă.
- `mean` va returna media aritmetică a elementelor din toate containerele.
- `median` va returna mediana elementelor din toate containerele.
- `min` va returna valoarea minimă din toate containerele.
- `sum` va returna suma elementelor din toate containerele.
"""

# CODUL TĂU VINE MAI JOS:
class DataStatistics:
    def __init__(self,list_of_objects):
        self.list_of_objects = list_of_objects
    def __add__(self,new_container):
        self.list_of_objects.append(new_container)
    def mean(self):
        sum = 0
        count=0
        for obiect in self.list_of_objects:
            for x in obiect.lista:
                sum += x
                count += 1
        return sum/count
    def median(self):
        all_numbers = []
        for obiect in self.list_of_objects:
            all_numbers.extend(obiect.lista)     
        sorted_numbers = sorted(all_numbers)
        lungime_lista = len(sorted_numbers)
        if lungime_lista % 2 ==0:
            median = (sorted_numbers[lungime_lista // 2 - 1] + sorted_numbers[lungime_lista // 2]) / 2
        else:
            median = sorted_numbers[lungime_lista // 2]
        return median
    def min(self):
        all_numbers = []
        for obiect in self.list_of_objects:
            all_numbers.extend(obiect.lista)
        sorted_numbers = sorted(all_numbers)
        return sorted_numbers[0]
    def sum(self):
        sum = 0
        for obiect in self.list_of_objects:
            for x in obiect.lista:
                sum += x           
        return sum
    
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_4(DataStatistics, DataContainer))
# VERIFICATION PROCESS

"""
Iar pe ultima sută de metri, Microsoft a cerut și un element de filtrare a datelor.

Creează o clasă `DataFilter` care va primi ca input o listă de obiecte de tipul `DataContainer`.
- __init__ va inițializa clasa cu lista de obiecte.
- `add_container` va permite adăugarea unui nou container în listă.
- `filter_zeros` va returna o listă cu toate elementele care sunt diferite de 0.
- `filter_negatives` va returna o listă cu toate elementele care sunt mai mari sau egale cu 0.
- `filter_positives` va returna o listă cu toate elementele care sunt mai mici sau egale cu 0.
- `filter_under_mean` va returna o listă cu toate elementele care sunt mai mari decât media aritmetică a tuturor elementelor 
calculate cu metoda `mean` din clasa `DataStatistics`.
"""

# CODUL TĂU VINE MAI JOS:
class DataFilter:
    def __init__(self,list_of_objects):
        self.list_of_objects = list_of_objects
    def add_container(self,new_container):
        self.list_of_objects.append(new_container)
    def filter_zeros(self):
        return [x for obiect in self.list_of_objects for x in obiect.lista if x!= 0]
    def filter_negatives(self):
        return [x for obiect in self.list_of_objects for x in obiect.lista if x>= 0]
    def filter_positives(self):
        return [x for obiect in self.list_of_objects for x in obiect.lista if x<= 0]
    def filter_under_mean(self):
        obj = DataStatistics(self.list_of_objects)
        media = obj.mean()
        print(media)
        return [x for obiect in self.list_of_objects for x in obiect.lista if x > media ]

# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_5(DataFilter, DataStatistics, DataContainer))
print(session.get_completion_percentage())
# VERIFICATION PROCESS