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
        
        #Primero comparar si el valor ya existe en el arbol
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
    
    def buscar(self, data: T) -> bool:
        return self._buscar(data, self.nodoRaiz)
    
    def _buscar(self, data: T, nodo: NodoArbol) -> bool:
        
        while(nodo is not None):
            if self.comparar_valor_nodos(data, nodo) == 0:
                return True
            nodo = nodo.get_nodo_derecha() if self.comparar_valor_nodos(data, nodo) == 1 else nodo.get_nodo_izquierda()
        return False
    
    def printTree(self):
        
        self.InOrder(self.nodoRaiz)
        
    
    
    def InOrder(self, nodo: NodoArbol): #Necesitamos el nodo para saber cual es el nodo raiz
        
        #Suponemos que el nodo proporcionado es el nodo raiz
        #Primero recorremos el arbol por la derecha y luego por la izquierda, haciendo asi que se impriman los datos en orden
        
        if nodo == None:
            return
        self.InOrder(nodo.get_nodo_derecha)
        print(nodo.get_valor)
        self.InOrder(nodo.get_nodo_izquierda)
    
    
    #A partir de aqui son los metodos que de verdad me da miedo
        

    #Para remover un valor, vamos a necesitar de 3 casos:
    # 1. Caso de nodo hoja
    # 2. Caso de nodo con un hijo
    # 3. Caso de nodo con 2 hijos
    
    def removerValor(self, data: T) -> bool:
        
        nodoActual = self.nodoRaiz
        
            #IK
        if self.comparar_valor_nodos(data, nodoActual.get_valor) == 0:
    
    
                