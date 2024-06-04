Una lista ligada es una estructura de datos que consiste de 2 (o algunas veces 3) partes, una seccion donde se guarda información y otra sección donde se guarda la dirección en memoria del siguiente elemento en la lista. 
Dependiendo si es una lista ligada o circular, el ultimo nodo puede terminar en null o en la dirección del primer nodo

la complejidad de obtener un elemento de una lista ligda siempre va a ser O(n), porque no sabes la direccion en la cual esta el elemento que quieres, no puedes acceder directamente a el, solo puuedes acceder y saber donde esta esa memoria a traves del nodo anterior que tiene esa informacion

las listas ligadas se pueden crear con la libreria deque

from collections import deque

Para objetivos de estudio vamos a realizar los nodos de manera manual y vamos a hacer una practica con deque


Tambien aprovechando esto, voy a aprendere a como hacer clases en Python.

# Clases

Según la misma documentación de Python.org (https://docs.python.org/3/tutorial/classes.html) escencialmente las clases en Pyhon se comportan casi igual que en c++, se crean en runtime y se pueden modificart despues de creación. Todas las variables y metodos son publicos por defecto y todas las funciones miembras son virtuales por defecto. e igual que en c++ los operadores se pueden sobrecargar.

El syntax en python es un poco diferente a la hora de construir un objeto de la clase. Mientras que en c++ tenmemos un objeto que recibe parametros y luego los pasa al constructur, aqui usamos una funcion __init__(self)

ejemplo en c++:

//Asumiendo que estamos importando todo lo necesario
class Persona {

    private: //usamos en este ejemplo para no exponer datos

    string nombre;
    int edad;

    public:
    
    //estos 2 constructores sin tomar en cuenta que podemos asignar valores default

    //Constructor
    Persona() {} // <- Constructor vacio

    /* un tipo de constructor
    
    Persona(string nombre, int age){
        this->nombre = nombre;
        edad = age;
    }

    */

    //Otro tipo de constructor

    Persona(string nombre, int age)
        : nombre(nombre), edad(age) {}

    /*
    Incluya todos los demas métodos necesarios para leer y escribir datos
    */

    friend std::ostream& operator<<(std::ostream& os, const Persona& p);

}

    ostream& operator<<(ostream& os, Persona& p) { //Metodo de sobrecarga para poder imprimir persona con cout << Persona
        os << "Nombre: " p.getNombre() << "Edad: " << p.getEdad() << endl;
        return os
    }



Lo mismo en python seria:

class Persona:

    #Constructor vacio
    def __init__(self):
        pass


    #Constructor
    def __init__(self, nombre, edad): #donde el "__" significa variable privada
        self.__nombre = nombre
        self.__edad = edad

    # Overloading the str() function to print object details
    def __str__(self):
        return f"Nombre: {self.s}, Edad: {self.__edad}"


persona = Persona("Juan", 30)
print(persona)  # This will use the __str__ method



#LISTAS LIGADAS

habiendo tenido una explicacion sobre clases en Python y en general sobre listas ligada, vamos a empezar con la practica