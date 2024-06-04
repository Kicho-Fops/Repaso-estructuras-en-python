Ahora se viene lo chido

Los arboles son estructuras de datos jerarquicos que se usan para repreesntar y organizar data de tal manera que sea ams facil de navegar y buscar-
Sirve como yo lo llamo de una manera "Bidimensional", ya que tenemos mas de un "Plano" en el que buscar informacion, refiriendome en que se puede puede buscar hacia adelante pero tambien hacia abajo
Para ejemplicficar esto, considerese lo siguiente: Un arbol binario de busqueda (BST por sus siglas en ingles) es un arbol donde a partir del elemento raiz, todos los elementos mayores van a ir a la derecha y todos los menores van a ir a la izquierda.

     10
    /  \
   5    15
  / \   / \
 2   7 12 20

Si ordenamos todos los elementos de menor a mayor, se va a ver de esta manera

2
 \
  5
   \
    7
     \
      10
       \
        12
         \
          ...
Si nos damos cuenta, esto perfectamente lo podemos rotar y queda de la siguiente manera:
2-5-7-10-12-15-20, en nodos serparados
Lo que escencialmente es una lista ligada, porque las listas ligadas estan aqui para tormentarnos y hacer que nuestras vidas sean tristes.

el 04/06 voy a cubrir BST y futuramente otro par de arboles

para esto voy a necesitar queues