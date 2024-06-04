from typing import TypeVar, Generic, Optional

T = TypeVar('T')  # Equivalente a template <class T> en c++

class Node(Generic[T]):
    
    def __init__(self, data: T):
        self.data = data  # Dato generico
        self.next: Optional[Node[T]] = None  # Dato que existe opcionalmente, tambien generico
        
    def set_next(self, next_node: Optional['Node[T]']) -> None:  # Setter
        self.next = next_node
        
    def set_info(self, data: T) -> None:  # Setter
        self.data = data
        
    def get_info(self) -> T:  # Getter
        return self.data
    
    def get_next(self) -> Optional['Node[T]']:  # Getter
        return self.next


class ListaLigada(Generic[T]):
    
    def __init__(self):
        self.first_node: Optional[Node[T]] = None
        
    def get_last_node(self) -> Optional[Node[T]]:
        if self.first_node is None:  # Si el primer nodo es nulo, no hay nodos
            return None
        nodo_actual = self.first_node
        while nodo_actual.get_next() is not None:  # Obtener el siguiente nodo hasta que el metodo get_next regrese nulo
            nodo_actual = nodo_actual.get_next()
        return nodo_actual
    
    def get_first_node(self) -> Optional[Node[T]]:  # Obtener el primer nodo
        return self.first_node
    
    def insertar(self, data: T) -> None:
        Nodo_Nuevo = Node(data)
        if self.first_node is None:  # Si el primer nodo es nulo, o sea hay 0 nodos, crear el primer nodo
            self.first_node = Nodo_Nuevo
        else:
            ultimo_nodo = self.get_last_node()  # en caso de que exista ya un nodo, mandamos a buscar cual es el ultimo nodo y a ese le asignamos el nodo que queremos agregar como siguiente nodo
            if ultimo_nodo:
                ultimo_nodo.set_next(Nodo_Nuevo)
    
    def remove(self, data: T) -> bool:  # Vamos a recorrer la lista ligada hasta que podamos encontrar el valor que queremos eliminar
        primer_nodo = self.get_first_node() 
        nodo_anterior = None
        contador = 0
        while primer_nodo is not None:
            if primer_nodo.get_info() == data:
                if nodo_anterior is None:  # Si se quiere eliminar el primer nodo
                    self.first_node = primer_nodo.get_next()
                else:
                    nodo_anterior.set_next(primer_nodo.get_next())
                print(f"El valor se encontró en el índice: {contador}")
                return True
            nodo_anterior = primer_nodo
            primer_nodo = primer_nodo.get_next()
            contador += 1
        return False
    
    def removeAt(self, index: int) -> bool:
        primer_nodo = self.get_first_node() 
        nodo_anterior = None
        contador = 0
        while primer_nodo is not None:
            if contador == index:
                if nodo_anterior is None:  # Si se quiere eliminar el primer nodo
                    self.first_node = primer_nodo.get_next()
                else:
                    nodo_anterior.set_next(primer_nodo.get_next())
                return True
            nodo_anterior = primer_nodo
            primer_nodo = primer_nodo.get_next()
            contador += 1
        return False
    
    def find(self, data: T) -> bool:
        primer_nodo = self.get_first_node()
        while primer_nodo is not None:
            if primer_nodo.get_info() == data:
                return True    
            primer_nodo = primer_nodo.get_next()
        return False
    
    def isEmpty(self, data: T) -> bool:
        return self.first_node == None
        
    def __str__(self) -> str:
        values = []
        current_node = self.get_first_node()
        while current_node is not None:
            values.append(str(current_node.get_info()))
            current_node = current_node.get_next()
        return ' -> '.join(values)
