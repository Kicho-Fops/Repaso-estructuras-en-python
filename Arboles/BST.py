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
        self.nodoRaiz = NodoArbol
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
        nodoAnterior = None
        while nodoActual is not None:
        
            #Encontramos el valor que buscamos
            if self.comparar_valor_nodos(data, nodoActual.get_valor()) == 0:
                #Ya lo encontramos
                
                # Caso 1: Nodo hoja
                
                if nodoActual.get_nodo_derecha() ==  None and nodoActual.get_nodo_izquierda() == None:
                    #No tiene hijo, por lo tanto es un nodo hoja
                    
                    #Revisar si no es nodo raiz
                    if nodoAnterior != None:
                        if nodoActual == nodoAnterior.get_nodo_derecha():
                            nodoAnterior.set_nodo_derecha(None)
                            
                        if nodoActual == nodoAnterior.get_nodo_izquierda():
                            nodoAnterior.set_nodo_izquierda(None)
                    else:
                        self.nodoRaiz = None
                    
                    return True
                
                # Caso 2: Nodo con 2 hijos
                
                if nodoActual.get_nodo_derecha() != None and nodoActual.get_nodo_izquierda() != None:
                #Hijole mano, te toca un buen de chamba
                
                    #Este es el nodo que va a reemplazar el nodo que vamos a elimiar del arbol
                    nodoPadreDelPredecesor = nodoActual
                    nodoPredecesor = nodoActual.get_nodo_izquierda()
        
                
                    
                    #Obtenemos el valor maximo del lado izquierdo del arbol, en otras palabras, el valor mas cercano pero menor al valor original
                    while nodoPredecesor.get_nodo_derecha() != None:
                        nodoPadreDelPredecesor = nodoPredecesor
                        nodoPredecesor = nodoPredecesor.get_nodo_derecha()
                        
                    nodoActual.set_valor(nodoPredecesor.get_valor()) # En este punto tenemos 2 nodos con el mismo valor
                    
                    
                    # Desconecamos el predecesor y conectamos el nodo padre del predecesor con los posibles hijos del llamado nodoPredecesor (Que acutalmente no es el predecesor)
                    
                    # A la hora de estudiar me estoy atorando mucho aqui, asi que me voy a tomar el tiempo para explicar  todo paso a paso para que  en el futuro entienda
                    #
                    # Sabemos que el nodo que encontramos tiene 2 nodos hijos, vamos a "crear" un subarbol donde nuestro nodo que vamos a borrar se convierte en el nodoRaiz
                    # El nodoPredecesor es como un buscador, que encuentra el nodo con el valor con el que vamos a reemplazar al nodo que estamos borrando 
                    # El nodoPadreDelPredecesor es el nodo anterior al nodo buscador 
                    #
                    # Cuando encontramos (Para esta solucion) el nodo con el valor mas cercano pero menor al nodo que estamos eliminando, vamos a duplicar el nodo "Buscador" (Osea nodoPredecesor) en el nodo original
                    # despues vamos a conectar los nodos hijos del nodo buscador (nodoPredecesor) al nodoPadreDelPredecesor, tambien efectivamente eliminando el nodo buscador (nodoPredecesor)
                    # 
                    #
                    if nodoPredecesor.get_nodo_izquierda() != None:
                        # El nodo llamado nodo predecesor tieje un hijo a la izquierda, vamos a reemplazar el valor del hijo de la izquierda con el del nodoPredecesor, 
                        # pero no solo reemplazamos el  valor, reemplazamos el nodo y hacemos que la direccion en memoria del nodo predecesor sea reemplazada con al del hijo de la izquierda
                        if nodoPadreDelPredecesor != None:
                            
                            if nodoPredecesor == nodoPadreDelPredecesor.get_nodo_izquierda():
                                nodoPadreDelPredecesor.set_nodo_izquierda(nodoPredecesor.get_nodo_izquierda()) #Solo para el futuro, beto se equivoco en este set y en el; siguiente, PUES A HUEVO CON RAZON NO ENTENDIA NI MADRES
                            else:
                                nodoPadreDelPredecesor.set_nodo_derecha(nodoPredecesor.get_nodo_derecha())
                                
                               # Y es cierto que hay que estar
                               # Alerta y preparado
                               # Para enfrentar peligros
                               # Que nos puedan lastiamr
                               
                               # Pero siempre puede haber
                               # En vilo y asechando
                               # Tiburones en el bosque
                               # Y zorros en el mar ( Como Kicho :3 )

                        else:
                            # El nodo predecesor no tiene un hijo a la izquierda, tiene un hijo a la derecha
                            if nodoPadreDelPredecesor != None:
                                if nodoPredecesor == nodoPadreDelPredecesor.get_nodo_izquierda():
                                    nodoPadreDelPredecesor.set_nodo_izquierda(nodoPredecesor.get_nodo_derecha()) 
                                else:
                                    nodoPadreDelPredecesor.set_nodo_derecha(nodoPredecesor.get_nodo_derecha())
                    else:
                        #El nodoPredecesor no tiene hijos
                        if nodoPadreDelPredecesor.get_nodo_derecha != None:
                            self.nodoRaiz = nodoPadreDelPredecesor.get_nodo_izquierda()
                        else:
                            self.nodoRaiz = nodoPadreDelPredecesor.get_nodo_derecha()
                        
                    return True
                            
                        # Caso 3: Nodo con un solo hijo (no cubierto en tu código original)
                if nodoActual.get_nodo_derecha() != None or nodoActual.get_nodo_izquierda() != None:
                    # Solo tiene un hijo, ya sea izquierdo o derecho
                    
                    if nodoActual.get_nodo_izquierda() != None:
                        hijo = nodoActual.get_nodo_izquierda()
                    else:
                        hijo = nodoActual.get_nodo_derecha()
                    
                    if nodoAnterior != None:
                        if nodoActual == nodoAnterior.get_nodo_derecha():
                            nodoAnterior.set_nodo_derecha(hijo)
                        else:
                            nodoAnterior.set_nodo_izquierda(hijo)
                    else:
                        self.nodoRaiz = hijo
                    
                    return True
            
            # Si no encontramos el valor, seguimos buscando
            nodoAnterior = nodoActual
            if self.comparar_valor_nodos(data, nodoActual.get_valor()) < 0:
                nodoActual = nodoActual.get_nodo_izquierda()
            else:
                nodoActual = nodoActual.get_nodo_derecha()
        
            return False
                    
                    
                    
                 
                    
                    
                    
       
            
    
                