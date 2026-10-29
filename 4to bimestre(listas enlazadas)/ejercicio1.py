class nodo:
    def __init__(self, dato):
        self.dato = dato
        self.apuntador = None


class lista_enlazada:
    def __init__(self):
        self.cabeza = None

    def insertar(self, dato):
        nuevo = nodo(dato)

        if self.cabeza is None:
            self.cabeza = nuevo
            return

        actual = self.cabeza

        while actual.apuntador is not None:
            actual = actual.apuntador

        actual.apuntador = nuevo

    def imprimir(self):
        actual = self.cabeza

        while actual is not None:
            print(actual.dato)
            actual = actual.apuntador

        print("fin del nodo")


# Se probará la impresión del programa
mi_lista = lista_enlazada()

# Creamos la lista
mi_lista.insertar(10)
mi_lista.insertar(20)
mi_lista.insertar(30)

mi_lista.imprimir()


