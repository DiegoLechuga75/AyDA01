class Nodo:
    def __init__(self, datos, hijos=None):
        self.datos = datos
        self.hijos = hijos
        self.padre = None

    def set_hijos(self, hijos):
        self.hijos = hijos
        if self.hijos != None:
            for hij in self.hijos:
                hij.padre = self

    def get_hijos(self):
        return self.hijos

    def get_padre(self):
        return self.padre

    def set_padre(self, padre):
        self.padre = padre

    def set_datos(self, datos):
        self.datos = datos

    def get_datos(self):
        return self.datos

    def igual(self, nodo):
        if self.get_datos() == nodo.get_datos():
            return True
        else:
            return False

    def en_lista(self, lista_nodos):
        esta_en_lista = False
        for n in lista_nodos:
            if self.igual(n):
                esta_en_lista = True
        return esta_en_lista

    def __str__(self):
        return str(self.get_datos())
def busqueda_amplitud(estado_inicial, solucion):

    solucionado = False
    nodos_visitados = []
    nodos_pendientes = []
    nodoInicial = Nodo(estado_inicial)
    nodos_pendientes.append(nodoInicial)

    while (not solucionado) and (len(nodos_pendientes) != 0):
        nodo = nodos_pendientes.pop(0)
        nodos_visitados.append(nodo)
        if nodo.get_datos() == solucion:
            solucionado = True
            return nodo
        else:
            dato_nodo = nodo.get_datos()
            #Cambio izquierdo
            hijo = [dato_nodo[1], dato_nodo[0], dato_nodo[2], dato_nodo[3], dato_nodo[4], dato_nodo[5]]
            hijo_izq = Nodo(hijo)
            if (not hijo_izq.en_lista(nodos_pendientes)) and (not hijo_izq.en_lista(nodos_visitados)):
                nodos_pendientes.append(hijo_izq)
            #Cambio enmedio izquierda
            hijo = [dato_nodo[0], dato_nodo[2], dato_nodo[1], dato_nodo[3], dato_nodo[4], dato_nodo[5]]
            hijo_med_izq = Nodo(hijo)
            if (not hijo_med_izq.en_lista(nodos_pendientes)) and (not hijo_med_izq.en_lista(nodos_visitados)):
                nodos_pendientes.append(hijo_med_izq)
            #Cambio enmedio
            hijo = [dato_nodo[0], dato_nodo[1], dato_nodo[3], dato_nodo[2], dato_nodo[4], dato_nodo[5]]
            hijo_med = Nodo(hijo)
            if (not hijo_med.en_lista(nodos_pendientes)) and (not hijo_med.en_lista(nodos_visitados)):
                nodos_pendientes.append(hijo_med)
            #Cambio enmedio derecha
            hijo = [dato_nodo[0], dato_nodo[1], dato_nodo[2], dato_nodo[4], dato_nodo[3], dato_nodo[5]]
            hijo_med_der = Nodo(hijo)
            if (not hijo_med_der.en_lista(nodos_pendientes)) and (not hijo_med_der.en_lista(nodos_visitados)):
                nodos_pendientes.append(hijo_med_der)
            # Cambio enmedio derecha
            hijo = [dato_nodo[0], dato_nodo[1], dato_nodo[2], dato_nodo[3], dato_nodo[5], dato_nodo[4]]
            hijo_der = Nodo(hijo)
            if (not hijo_der.en_lista(nodos_pendientes)) and (not hijo_der.en_lista(nodos_visitados)):
                nodos_pendientes.append(hijo_der)
            nodo.set_hijos([hijo_izq, hijo_med_izq, hijo_med, hijo_med_der, hijo_der])

if __name__ == "__main__":

    estado_inical = [3, 2, 1, 4, 5, 6]
    solucion = [1, 2, 3, 4, 5, 6]
    nodo_solucion = busqueda_amplitud(estado_inical, solucion)
    resultado = []
    nodo = nodo_solucion
    while nodo.get_padre() is not None:
        resultado.append(nodo.get_datos())
        nodo = nodo.get_padre()
    resultado.append(estado_inical)
    resultado.reverse()
    print(resultado)
    profundidad = len(resultado)
    print("La profundidad es de: " + str(profundidad))
