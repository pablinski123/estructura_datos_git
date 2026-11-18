class Nodo:
    def __init__(self, valor):
        self.valor = valor #Guarda el valor
        self.siguiente = None #el Puntero indica a donde apunta el nodo siguiente

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None #Puntero que indica el primer nodo de la lista

    def insertar (self, valor):
        nuevo_nodo = Nodo(valor)
        if self.cabeza is None: #Si la lista esta vacia
            self.cabeza = nuevo_nodo #El primer nodo es el nuevo nodo
            return
        actual = self.cabeza

        while actual.siguiente is not None: #Recorre la lista hasta el final
              actual = actual.siguiente

        actual.siguiente = nuevo_nodo

    def imprimir(self):
        actual = self.cabeza
        while actual is not None:
            print(actual.valor)
            actual = actual.siguiente
        print("Fin de la lista")

#Se imprimira el programa principal
mi_lista = ListaEnlazada()
mi_lista.insertar(10)
mi_lista.insertar(20)
mi_lista.insertar(30)
mi_lista.imprimir()