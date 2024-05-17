#Creamos clase nodo de la lista

from typing import TypeVar, Generic, List, Optional

T = TypeVar('T')  # Equivalente a template <class T> en c++

class Node(Generic[T]):
    
    
    def __init__(self, data: T):
        self.data = T = data # Dato generico
        self.next: Optional[Node[T]] = None # Dato que existe opcionalmente, tambien generico
        
        