import Queue as q

from typing import TypeVar, Generic, Optional

T = TypeVar('T')

class NodoArbol(Generic[T]):
    
    # No puedes tener multiples constructiores, si es necesario utilizamos valores por defecto para cada una de las opciones
    def __init__(self, data: Optional[T] = None, nodoDerecha: Optional['NodoArbol'] = None, nodoIzquierda: Optional['NodoArbol'] = None):
        self.valor = data
        self.derecha = nodoDerecha
        self.izquierda = nodoIzquierda
        
    def get_nodo_derecha(self) -> Optional['NodoArbol']:
        return self.derecha
    
    def get_nodo_izquierda(self) -> Optional['NodoArbol']:
        return self.izquierda
    
    def set_nodo_derecha(self, nodo: Optional['NodoArbol']) -> None:
        self.derecha = nodo
        
    def set_nodo_izquierda(self, nodo: Optional['NodoArbol']) -> None:
        self.izquierda = nodo
    
    def get_valor(self) -> Optional['NodoArbol']:
        return self.valor
    
    def set_valor(self, data: T) -> None:
        self.valor = data
        
        
class BST(Generic[T]):
    #Necesitamos
    #Agregar, obtener y definir valores
    #Compara nodos para saber cual es mayor y cual es menor
    #Imprimir el arbol
    #Un buen de metodos para reocrrer el arbol, asi como en mi repo de gitgub, aunq me de hueva
    
    def __init__(self):
        self.nodoRaiz = None
        self.nodoVisitado = None
        self.fila = None
    
    def insertar(self, data: T) -> None:
        if self.nodoRaiz is None:
            self.nodoRaiz = NodoArbol(data)
        else:
            self._insertar(data, self.nodoRaiz) #Sugerencia de Copilot y el prefjo _ significa que es un metodo privado, se considera buena practica en funciones recursivas
    
    def comparar_valor_nodos(self, nodo1: NodoArbol, nodo2: NodoArbol) -> int:
        if nodo1.get_valor() == nodo2.get_valor():
            return 0
        elif nodo1.get_valor() > nodo2.get_valor():
            return 1
        else:
            return -1
    
     
    def _insertar(self, data: T, nodo: NodoArbol) -> None:
        nodo_actal = nodo
        nodo_anterior = None
        
        while(nodo_actal is not None):
            if self.comparar_valor_nodos(data, nodo_actal) == 0: #Caso base
                return False #El valor ya existe en el arbol
            nodo_anterior = nodo_actal
            nodo_actal = nodo_actal.get_nodo_derecha() if self.comparar_valor_nodos(data, nodo_actal) == 1 else nodo_actal.get_nodo_izquierda()
            #Si llega aqui se inserta
        
        if nodo_anterior is None:
            self.nodoRaiz =  NodoArbol(data) #Caso base
        else:
            if self.comparar_valor_nodos(data, nodo_anterior) == 1: #Caso derecha
                nodo_anterior.set_nodo_derecha(NodoArbol(data))
            else:
                nodo_anterior.set_nodo_izquierda(NodoArbol(data)) #Caso izquierda
        return True
    
    
                