Diferencia entre Listas y Tuplas: 
Explica las diferencias entre listas y tuplas en Python. ¿Cuándo usarías una sobre la otra?

La diferencia principal entre listas y duplas es que las tuplas son inmutables estas una vez creadas no se puden
modificar bajo ningún concepto. Esta sería la principal diferencia entre estos dos tipos de estructuras, si queremos ver las similitudes hay varias como por ejemplo ambas son ordenadas pueden contener distintos tipos de datos, al igual que tener datos duplicados y las dos se pueden acceder mediante índices.
Como hemos mencionado las tuplas son inmutables entonces yo las usaría cuando sé que los datos que tenga no van a cambiar ya que si van a cambiar utilizaría la lista.

Listas: cuando quieres hacer una lista de tareas que sabes que vas a tener que modificar, quitar, añadir.

Tuplas: cuando quieres tener una lista de coordenadas x y que no van a cambiar.

Complejidad Temporal del Algoritmo de Búsqueda Binaria:
¿Cuál es la complejidad temporal del algoritmo de búsqueda binaria y por qué es eficiente para buscar en listas ordenadas?

Si hablamos de la complejidad temporal del algoritmo de búsqueda binaria tendriamos que se trata de O(log n).
Esto hace que sea mucho más eficiente para búsquedas grandes que la lineas ya que la función logarítmica crece más lento que la lineal 0(n).
Hay que anotar que este tipo de algoritmo solo funciona en listas ordenadas debido a como funciona este método, realmente lo que hace es ir dividiendo la lista por la mitad descartando así la otra mitad si el número es mayor o menor que el que estamos buscando esto hace que la eficiencia para buscar un número se divida a la mitad.

Por ejemplo en una lista de un millón de elementos tendriamos que hacer en el peor de los casos todas esas comprobaciones ya que el elemento que estamos buscando se podría encontrar en la última posición. Mientras que con la búsqueda binaria tendríamos que hacer unas 20 comprobaciones log2(1.000.000)

Concepto de Polimorfismo:
Explica el concepto de polimorfismo en la programación orientada a objetos y proporciona un ejemplo en Python.

El polimorfismo es un principio de la programación orientado a objetos que permite a objetos de distintas clases ser tratados de una manera uniforme.Permitiendo que un mismo método se comporte de manera diferente en diferentes contextos, lo que hace que tu código sea más flexible y fácil de mantener.

Por ejemplo:

```python
class Animal:
    def comunicate(self):
        pass
 
class Dog(Animal):
    def comunicate(self):
        return "Woof!"
 
class Cat(Animal):
    def comunicate(self):
        return "Meow!"
 

animals = [Dog(), Cat()]
 
for animal in animals:
    print(animal.comunicate())

```
Como podemos ver en este código tenemos una clase Animal que simplemente tiene un método comunicate que no va a ser implementado por esta clase por eso ponemos la palabra reservada pass. A continuación tenemos las clases Dog y Cat que heredan de la clase animal estas dos clases implementan el método comunicate. Una vez definidas las dos clases iniciamos dos instancias de las clases definidas hacemos un bucle for para imprimir el resultado de los métodos, como ambos se llaman igual podemos tratarlos de manera uniforme y que funcione sin ningún tipo de problemas. Uno tendrá que imprimir Woof y el otro Meow. Así podemos tratar tanto a los perros como a los gatos como animales genéricos dentro del bucle for, lo que hace que el código sea más flexible y fácil de mantener, ya que no tenemos que preocuparnos por el tipo específico de animal en cada iteración del bucle.

Manejo de Excepciones en Python: ¿Qué es una excepción en Python y cómo manejarías una excepción en tu código?

Las excepciones son un evento anormal que rompe con el flujo previsto del programa. Si no tenemos en cuenta este tipo de excepciones pueden llegar a parar el programa. Por ejemplo si tenemos una calculadora y queremos informarle al usuario que no se puede dividir un número por cero tenemos que hacer uso de estas excepciones en este caso concreto tenemos ZeroDivisionError que en Pyhton ocurre cuando hacemos lo mencionado anteriormente. Esta es una de muchos tipos de excepciones como por ejemplo errores de sintaxis, violaciones de acceso a memoria, intentos de realizar operaciones no admitidas entre otros. Estas excepciones son propias del sistema es decir podemos utilizarla en nuestro programa sin tener que modificar o añadir código. Por ejemplo si queremos crear una excepción propia lo podriamos hacer de la siguiente forma

```python 
class UnderageError(Exception):
    def __init__(self, age):
        self.age = age
        self.message = f"The person is {age} years old and is underage"

def check_legal_age(age):
    if age < 18:
        raise UnderageError(age)
    else:
        print("The person is of legal age")

# Example of usage
try:
    person_age = int(input("Enter the person's age: "))
    check_legal_age(person_age)
except ValueError:
    print("Error: Please enter a valid age (integer)")
except UnderageError as error:
    print("Error:", error.message)
finally:
    print("Thank you for using this program.")
```

Con este ejemplo podemos ver perfectamente como hacer nuestra propia excepción y como gestionarla en nuestro programa.
Para crear una excepción tenemos que heredar de la clase Exception. Cambiamos el mensaje al que queremos que mande, una vez definido ya podemos usarla en la función de check_legal_age si la persona tiene menos de 18 años saltará nuestra excepción personalizada. Ahora vamos los 3 bloques fundamentales try,except,finally dentro del try tendremos que poner el código que puede llegar a soltar una excepción en nuestro caos verificar si la persona es mayor de edad. Si le ponemos 17 entrará por except UnderageError as error e imprimirá el mensaje. Nota importante podemos tener varios except para controlar distintas excepciones en mi caso el valueError es para cuando el usuario te mete un valor que no es un número si por ejemplo escribe "abc" entraría por except ValueError y por último tenemos finally que siempre se ejecutará haya o no haya entrado por la excepción.

Ventajas de los Conjuntos (Sets): Describe algunas ventajas de utilizar conjuntos en Python en comparación con otras estructuras de datos como listas o diccionarios.

Los sets son estructuras desordenadas de datos que no permiten elementos duplicados y son mutables.
Las ventajas de estas frente a otras estrucutras de datos son las siguientes

1. No permiten elementos duplicados 
2. Son más rápidos comprobando si un elemento está o no en el set.
3. Pueden llegar a ser más rápidas a la hora de insertar elementos dependiendo del hardware y el tamaño de los datos.
4. Operaciones de conjuntos como unión, intersección, diferencia, diferencia simétrica.
5. Al no ser indexadas no tienes que controlar el OutOfIndexError

Explica el concepto de herencia en POO y proporciona un ejemplo en Python.

La herencia en Python es un concepto que tiene sus bases en las clases. La herencia permite ordenar las clases de forma jerárquica es decir una clase va a ser la clase padre de la cual van a heredar las demás clases hijas. Estas clases tendrán los métodos y propiedades de la clase padre. Vamos a ver un ejemplo y ponerlo en contexto.

```python
class Animal:
    def __init__(self, species):
        self.__species = species

    def get_species(self):
        return self.__species

    def speak(self):
        return "GRRR"

class Dog(Animal):
    def __init__(self, species, breed):
        super().__init__(species)
        self.__breed = breed

    def get_breed(self):
        return self.__breed

    def speak(self):
        return "Woof!"

class Cat(Animal):
    def __init__(self, species, color):
        super().__init__(species)
        self.__color = color

    def get_color(self):
        return self.__color

    def speak(self):
        return "Meow!"


dog = Dog("Dog", "Labrador")
print(dog.get_species())
print(dog.get_breed())
print(dog.speak())

cat = Cat("Cat", "Black")
print(cat.get_species())
print(cat.get_color())
print(cat.speak())
```
Como podemos ver en este código tenemos la clase padre Animal que tiene como atributo species, un get de este atributo y un método genérico de speak. A continuación tenemos dos clases que heredan de la padre Dog y Cat estas tendrán un nuevo atributo breed y color respectivamente. Ambas tendrán un constructor, para llamar al constructor o cualquier método de la clase padre se pone como super(). Tmbién vamos a hacer overwrite del método speak para que se parezca al sonido que hace el animal. Si quisieramos también podriamos tener herencia múltiple es decir en nuestro ejemplo podriamos tener una clase mammal que conteniese atributos conjuntos a Dog y Cat.

Complejidad Algorítmica:
¿Qué es la notación Big O (O(n)) en términos de complejidad algorítmica y qué representa?

La notación Big O es una forma de medir la complejidad de los logaritmos en base al tiempo y a la cantidad de memoria que utilizan algunos algoritmos pueden ser muy eficientes en tiempo pero usar mucha cantidad de memoria. Principalmente se suele tener en cuenta el tiempo que tarde el algoritmo en ejecutarse este puede ir desde el más sencillo siendo O(1) hasta los más complejos como O(n!). Por ejemplo si tenemos un algoritmo O(1) nos da igual el tamaño de la entrada ya que siempre se va a mantener constante pero si tenemos O(n) cuanto más grande sea n vamos a tener que invertir mucho más tiempo en ejecutarlo. Ahora vamos a ver unos ejemplos:

```python
def return_constant():
    return 42

def copy_list(lst):
    new_list = []
    for num in lst:
        new_list.append(num)
    return new_list

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)
```
La primera función sería O(1) tanto en tiempo como en espacio ya que simplemente está retornando una variable y no depende de la entrada que le pongamos. Sin embargo copy list si que tiene una complejidad mayor siendo de o(n) tanto en tiempo como en espacio ya que tenemos que recorrer toda la lista incrementando proporcionalmente tanto el tiempo como en espacio en memoria que se tiene que reservar para copiar los elementos de lst a new_list. Ahora vamos a ver dos algoritmos que tienen la misma función pero distintos usos y notaciones, para empezar el bubble sort tiene una complejidad O(n2) ya que tenemos un bucle anidado esto a cambio de tener una eficiencia en memoria de O(1) porque no requiere espacio adicional que dependa del tamaño de la entrada ya que todo se hace en la misma lista. Pero si nos fijamos en quicksort es todo lo contrario este no tiene bucles anidados por lo que si comparamos en cuestión de tiempo va a ser más eficiente que su contraparte más concretamente O(n log n) pero espacialmente es peor también O(n log n).
Como hemos visto son dos algoritmos que tienen la misma función pero distinta complejidad entonces ¿cuando usaremos uno u otro? En caso donde la memoria es limitada usaremos BubbleSort ya que tiene la menor complejidad espacial siendo O(1) en casos como software para equipamiento médico,vehículos y demás donde los rescursos sean muy limitados. Y si lo que queremos es velocidad de ejecución usaremos quicksort ya que es más rápido en la mayoría de casos siendo el mejor de los casos O(nlogn) y en el peor de los casos O(n2).

Optimización de Código:
Describe algunas técnicas comunes de optimización de código en Python y cuándo sería apropiado usarlas.

1. **Uso de estructuras de datos eficientes:** Utilizar las estructuras de datos adecuadas para el problema en cuestión puede mejorar significativamente el rendimiento del código. Por ejemplo, elegir entre listas, conjuntos o diccionarios según las operaciones que se realicen con los datos puede marcar la diferencia en términos de tiempo de ejecución y consumo de memoria.

2. **Optimización de bucles y operaciones repetitivas:** Evitar bucles innecesarios y reducir la complejidad de las operaciones dentro de los bucles puede mejorar el rendimiento del código. Utilizar operaciones vectorizadas en lugar de bucles explícitos cuando sea posible puede ser una estrategia eficaz para optimizar el código.

```python
import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

result = a + b

print(result)  # Saldría [6,8,10,12]
```

3. **Memorización y caché:** Almacenar resultados intermedios de cálculos costosos puede evitar recálculos innecesarios y mejorar el tiempo de ejecución. La memorización es útil en algoritmos recursivos y funciones costosas que se llaman repetidamente con los mismos argumentos.

4. **Perfilado de código y análisis de rendimiento:** Identificar cuellos de botella y áreas críticas de un programa mediante herramientas de perfilado y análisis de rendimiento puede ayudar a priorizar las áreas que requieren optimización. Perfiladores como cProfile y herramientas de análisis de rendimiento como timeit son útiles para este propósito.

5. **Paralelización y concurrencia:** Utilizar técnicas de paralelización y concurrencia puede mejorar el rendimiento del código al aprovechar múltiples núcleos de CPU o realizar operaciones de manera simultánea. Módulos como multiprocessing y threading proporcionan funcionalidades para implementar estas técnicas en Python.

