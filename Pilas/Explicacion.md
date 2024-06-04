Stacks, en español pilas

Una pila es el unico tipo de dato que se estructura de manera LIFO (Last In, First Out)
En una pila se meten elementos como en una "Bateria" (o pila xd, por eso se llama pila) y se va revisando "el tope", osea siempre se empieza  por el ultimo elemento

Acccesar o editar elementos en una pila es de tiempo O(N), lo mismo con buscar pero opreaciones de agregación o eliminación es de O(1)


Hay otro tipo de dato que es muy similar en teoria que es una fila (Queue), ese tipo de dato es FIFO (First In, First Out). La implementación de una fila en la siguiente (se manera simple)

from queue import Queue
q = Queue(maxsize = 3)
print(q.qsize()) 
q.put('a')
q.put('b')
q.put('c')
print("\nFull: ", q.full()) 
print("\nElements dequeued from the queue")
print(q.get())
print(q.get())
print(q.get())
print("\nEmpty: ", q.empty())
q.put(1)
print("\nEmpty: ", q.empty()) 
print("Full: ", q.full())


Una implementacion con Type Hints seria algo asi (https://stackoverflow.com/questions/48956422/what-is-the-correct-way-to-type-hint-a-homogenous-queue-in-python3-6-especially)


from typing import NamedTuple, Any, Generic, TypeVar, Tuple
from multiprocessing import Process, Queue

T = TypeVar("T")


class Message(NamedTuple):
    method: str
    id: str
    data: Any = None


class TypedQueue(Generic[T]):
    def get(self) -> T:
        ...
    def put(self, m: T) -> None:
        ...


MessageQ = TypedQueue[Message]


class FractalWorker(Process):
    def __init__(self, work: MessageQ, results: MessageQ)
        super().__init__()
        self.work = work
        self.results = results

    @staticmethod
    def make_queues() -> Tuple[MessageQ, MessageQ]:
        work = cast(MessageQ, Queue())
        results = cast(MessageQ, Queue())
        return work, results