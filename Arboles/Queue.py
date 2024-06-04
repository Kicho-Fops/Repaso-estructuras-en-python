#Despues de hacer esto recorde que existe import queue from Queue, pero me sirve para practicar
#Idk, c++ me gusta mas y ahi tienes que escribir todo desde 0

import Listas_Ligadas as ll

from typing import TypeVar, Generic, Optional

T = TypeVar('T')

class Queue(Generic[T]):
    
    def __init__(self):
        self.lista = ll.ListaLigada()
        self.sais = 0 #Size, pero tenia que escribir mis mamadas
        
    def enqueue(self, data: T) -> None:
        self.lista.insertar(data)
        self.sais += 1
        
    def dequeue(self) -> Optional[T]:
        if self.lista.isEmpty:
            return None
        
        valor_actual = self.lista.get_first_node().get_info()
        self.lista.removeAt(0)
        return valor_actual
    
    def isEmpty(self) -> bool:
        return self.lista.isEmpty()
    
    # No se necesita destructor porque el interprete de python se encarga de la eliminacion de datos