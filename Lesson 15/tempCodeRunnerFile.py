class DataAnalysis:
    def __init__(self,lista_obiecte):
        self.lista_obiecte = lista_obiecte
    def add_container(self,new_container):
        self.lista_obiecte += new_container
    def __call__(self):
        return [max(obiect.lista) for obiect in self.lista_obiecte]
