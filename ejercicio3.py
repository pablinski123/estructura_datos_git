#nuevo ejercicio listas dobles enlazadas
class Nodo:
    def __init__(self, dato):
        self.dato = dato #guarda el dato al nnodo
        self.siguiente = None #apiuntador al siguiente 
        self.anterior = None #apuntador anterior 

class ListaDOble:
    def __init__(self):
        self.inicio = None #marca cual es el primer nodo
        self.final = None #marca cual es el ultimo nodo

    #agregar un nuevo nodo
    def insertar_al_inicio(self, dato):
        nuevo = Nodo(dato) #crear el nuevo nodo en la lista
        if self.inicio is None: #si la lista esta vacia
            self.inicio = nuevo #el primer nodo es el nuevo nodo
            self.final = nuevo   #el ultimo nodo es el nuevo nodo
        else:
            nuevo.siguiente = self.inicio #el nuevo agarra al que era primero
            self.inicio.anterior = nuevo #el viejo primero agarra al nuevo
            self.inicio = nuevo #actualizamos datos
            # actualizamos el final si la lista tenía más de un nodo
            if self.final is None:
                self.final = self.inicio

    def insertar_al_final(self, dato):
        nuevo = Nodo(dato)
        if self.inicio is None:
            self.inicio = nuevo
            self.final = nuevo
        else:
            self.final.siguiente = nuevo #el viejo ultimo agarra al nuevo
            nuevo.anterior = self.final #el nuevo agarra al viejo ultimo
            self.final = nuevo #actualizamos datos

    def imprimir(self):
        actual = self.inicio

        while actual is not None:
            print(actual.dato)
            actual = actual.siguiente

        print("Fin de la lista")

#Imprimir
trend_nodo = ListaDOble()
trend_nodo.insertar_al_final(10)
trend_nodo.insertar_al_final(20)
trend_nodo.insertar_al_inicio(40)
trend_nodo.imprimir()
