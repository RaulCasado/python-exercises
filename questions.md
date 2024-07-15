# Diferencia entre Listas y Tuplas: 
Explica las diferencias entre listas y tuplas en Python. ¿Cuándo usarías una sobre la otra?

La diferencia principal entre listas y duplas es que las tuplas son inmutables estas una vez creadas no se puden
modificar bajo ningún concepto. Esta sería la principal diferencia entre estos dos tipos de estructuras, si queremos ver las similitudes hay varias como por ejemplo ambas son ordenadas pueden contener distintos tipos de datos, al igual que tener datos duplicados y las dos se pueden acceder mediante índices.
Como hemos mencionado las tuplas son inmutables entonces yo las usaría cuando sé que los datos que tenga no van a cambiar ya que si van a cambiar utilizaría la lista.

Listas: cuando quieres hacer una lista de tareas que sabes que vas a tener que modificar, quitar, añadir.

Tuplas: cuando quieres tener una lista de coordenadas x y que no van a cambiar.

# Complejidad Temporal del Algoritmo de Búsqueda Binaria:
¿Cuál es la complejidad temporal del algoritmo de búsqueda binaria y por qué es eficiente para buscar en listas ordenadas?

Si hablamos de la complejidad temporal del algoritmo de búsqueda binaria tendriamos que se trata de O(log n).
Esto hace que sea mucho más eficiente para búsquedas grandes que la lineas ya que la función logarítmica crece más lento que la lineal 0(n).
Hay que anotar que este tipo de algoritmo solo funciona en listas ordenadas debido a como funciona este método, realmente lo que hace es ir dividiendo la lista por la mitad descartando así la otra mitad si el número es mayor o menor que el que estamos buscando esto hace que la eficiencia para buscar un número se divida a la mitad.

Por ejemplo en una lista de un millón de elementos tendriamos que hacer en el peor de los casos todas esas comprobaciones ya que el elemento que estamos buscando se podría encontrar en la última posición. Mientras que con la búsqueda binaria tendríamos que hacer unas 20 comprobaciones log2(1.000.000)

# Concepto de Polimorfismo:
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

# Manejo de Excepciones en Python: ¿Qué es una excepción en Python y cómo manejarías una excepción en tu código?

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

# Ventajas de los Conjuntos (Sets): Describe algunas ventajas de utilizar conjuntos en Python en comparación con otras estructuras de datos como listas o diccionarios.

Los sets son estructuras desordenadas de datos que no permiten elementos duplicados y son mutables.
Las ventajas de estas frente a otras estrucutras de datos son las siguientes

1. No permiten elementos duplicados 
2. Son más rápidos comprobando si un elemento está o no en el set.
3. Pueden llegar a ser más rápidas a la hora de insertar elementos dependiendo del hardware y el tamaño de los datos.
4. Operaciones de conjuntos como unión, intersección, diferencia, diferencia simétrica.
5. Al no ser indexadas no tienes que controlar el OutOfIndexError

# Explica el concepto de herencia en POO y proporciona un ejemplo en Python.

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

# Complejidad Algorítmica:
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

# Optimización de Código:
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

# ¿Qué significa que un lenguaje sea interpretado o compilado?

Un lenguaje compilado es aquel lenguaje que se pasa a lenguaje máquina una vez se va a iniciar y ya una vez compilado se ejecutará normalmente. Por otro lado, un lenguaje interpretado se ejecuta línea por línea, con cada línea traducida y ejecutada en tiempo real.

Las ventajas y desventajas de estos lenguajes empecemos con las ventajas de los compilados:

1. En tiempo de ejecución son más rápidos ya que se han traducido a un lenguaje cercano a la máquina por eso por ejemplo en Python en partes en las que se necesita más velocidad hay un módulo que convierte la parte del código en C++ o C. Otra opción sería escribir las partes donde necesitemos más rapidez en los lenguajes ya mencionados como C o C++.

2. Portabilidad: Una vez que un programa se ha compilado para una plataforma específica, puede ejecutarse en esa plataforma sin necesidad de instalar un entorno de tiempo de ejecución adicional, lo que puede simplificar la distribución y la instalación del software.

3. Detección de errores: lo más común en estos casos sería los errores de sintaxis ya que antes de ejecutarse se compila se puede detectar estos errores con mayor facilidad. Esto puede hacer que podamos ver el fallo antes de siquiera ejecutarlo.

4. Optimización: Los compiladores serán los encargados de hacer que nuestro código sea menos pesado y más rápido. Ya que comprimen todo al máximo para que haya el menor número de caracteres como espacios, tabulaciones, etc.

5. En general, los programas compilados tienden a ser más seguros en términos de protección contra acceso no autorizado al código fuente. Esto se debe a que el código fuente original se compila en código máquina binario, que es más difícil de leer y comprender.

Ahora el lado negativo:

1. El proceso de compilación puede llevar tiempo, especialmente para programas grandes o complejos. Este tiempo adicional de compilación puede ser inconveniente a la hora de probar cambios rápidos. Aunque hay métodos para facilitar al compilador este trabajo como por ejemplo la caché.

2. Una vez que un programa se ha compilado, es difícil realizar cambios en el código sin volver a compilarlo por completo. Esto puede ser problemático si se necesita realizar ajustes o correcciones rápidas en el software en producción, ya que cualquier cambio requiere volver a compilar y volver a implementar el programa.

3. Errores menos precisos: los interpretados al tener que interpretar el código línea por línea pueden llegar a dar mensajes de error más precisos que nos pueden facilitar a la hora de arreglar algún problema en la app.

Algunos ejemplos de lenguajes interpretados son JS y Python y compilados C, C++, Rust, Go.

# Qué son los decoradores en Python

Los decoradores son funciones que toman una función como parámetro y devuelven una función modificada.
Por ejemplo podemos añadir una nueva funcionalidad o lógica a una función sin tener que modificar el código base.

```python
import time

def tiempo_ejecucion(funcion):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = funcion(*args, **kwargs)
        fin = time.time()
        print(f"La función {funcion.__name__} tardó {fin - inicio} segundos en ejecutarse")
        return resultado
    return wrapper

@tiempo_ejecucion
def suma(a, b):
    return a + b

print(suma(3, 5))
```

Tenemos una función suma que suma dos números. Pero como tiene un decorador realmente está añadiendo o cambiando su funcionalidad así que veamos que tiene el decorador.

Este decorador como hemos visto en la definición toma por parámetros una función en este caso suma dentro del decorador vamos a declarar la función con los cambios que queramos en nuestro caso será medir el tiempo que se tarda en sumar estos 2 números con la función time.

También tenemos *args que sirve para cuando no sabes el número de arguementos que va a tomar la función por eso lo ponemos recogiendose en args como una tupla, a parte tenemos **kwargs que tiene la misma funcionalidad pero con parámetros de palabra clave es decir este tipo de argumentos nombre="Juan", edad=30 recogiendose como un diccionario.

Poniendo *args y **kwargs hacemos que el decorador sea más universal ya que podríamos aplicarselo a una función que tomase 3 parámetros en vez de 2. Una vez ejecutada la función va a imprimir el tiempo que tardó y retonar el resultado de la suma. Finalmente se va a retonar esta  función wrapper para ser usada con el decorador.

# Qué es un Arból Binario

Un árbol binario es una estructura de datos jerárquica en la que cada nodo tiene como máximo dos hijos izquierdo y derecho.Estos nodos secundarios, a su vez, pueden ser nodos internos con sus propios hijos o pueden ser nodos terminales, también conocidos como hojas.

Si queremos implementar esta estructura de datos podemos usar librerias como binarytree o podemos implementarlo con código implementado por nosotros esto puede tener varias ventajas como implementar sólo las funcionalidades que sean necesarias y mantener más ligero el proyecto ya que al instalar dependencias de terceros podemos instalar dependencias que se necesiten para hacer funcionar la que hemos instalado aumentando así el tamaño del proyecto. Pero también tiene desventjas la más clara es que se va a tener que gastar tiempo de desarrollo recreando la estructura. Así que vamos a ver un ejemplo de implementación en Python.

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root=None):
        self.root = root
    
    def display_tree(self, node, level=0):
        if node is not None:
            print(' ' * 4 * level + '->', node.value)
            self.display_tree(node.left, level + 1)
            self.display_tree(node.right, level + 1)

# Crearemos algunos nodos para probar que todo funcione correctamente
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

# Build the tree
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5

# Create the binary tree
tree = BinaryTree(node1)

# Display the tree
tree.display_tree(tree.root)
```

Esta sería el código base de como implementar un árbol binario en Python hay que tener en cuenta que depende de las necesidades del programa podemos añadir más o menos métodos. Por ejemplo podemos tener métodos para añadir un nodo, para recorrer el arbol como inorder, preorder y postorder. Aquí tenemos un ejemplo en código.

```python
    def traverse_preorder(node, visit):
        if node:
            visit(node.value)
            self.traverse_preorder(node.left, visit)
            self.traverse_preorder(node.right, visit)

    def traverse_inorder(node, visit):
        if node:
            self.traverse_inorder(node.left, visit)
            visit(node.value)
            self.traverse_inorder(node.right, visit)

    def traverse_postorder(node, visit):
        if node:
            self.traverse_postorder(node.left, visit)
            self.traverse_postorder(node.right, visit)
            visit(node.value)

    
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        queue = [node]
        while queue:
            current = queue.pop(0)
            if not current.left:
                current.left = Node(value)
                break
            else:
                queue.append(current.left)
            if not current.right:
                current.right = Node(value)
                break
            else:
                queue.append(current.right)

```

# Qué es un generador en Python y como se crea

Un generador en Python es una función especial que crea iteradores. Estos iteradores son eficientes ya que almacenan todos los valores en la memoria de una vez.

Yield: En lugar de utilizar return para devolver un valor, los generadores usan yield. Cada vez que yield se encuentra, la función produce un valor y mantiene su estado.

Iteradores: Los generadores son una forma de crear iteradores. Implementan los métodos __iter__() y __next__() automáticamente.

Para crear un generador podemos usar la palabra reservada yield.

```python
def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

counter = count_up_to(5)
for num in counter:
    print(num)
```

### Ventajas de los Generadores

- Eficiencia de Memoria: Generan valores sobre la marcha y no almacenan toda la secuencia en la memoria.
- Simplicidad: Son más simples y fáciles de escribir en comparación con las clases de iteradores.
- Mantienen Estado: Mantienen su estado automáticamente entre llamadas a `yield`.

### Qué es un método estático

Un método estático pertenece a una clase y puede ser llamado directamente desde la clase, es decir, no se necesita crear una instancia de la clase para poder llamar a un método estático. Estos métodos suelen tener en común la temática con la clase. Por ejemplo, si tenemos una clase `TaskController`, un método estático dentro de esta clase podría ser uno que gestione tareas.

En Python, para definir que un método es estático se utiliza el decorador `@staticmethod`.

```python
class TaskController:
    @staticmethod
    def get_tasks():
        # método que llame al modelo y acceda a las tareas de una base de datos
        print("Llamando a las tareas desde la base de datos")
    
# Una vez hecho esto, podemos llamar al método get_tasks sin tener que crear una instancia 
TaskController.get_tasks()
```

# Explica el concepto de __init__ y __new__.

Los métodos init y new son dos métodos utilizados a la hora de crear un objeto, las diferencias entre ellos son:

Empezemos por new este método es llamado antes que init ya que new se encarga de crear la instancia del objeto, una vez creada la instancia se llama a init que inicializará el objeto con los atributos. Otra diferencia es que new es un método estático mientras que init es un método de instancia. Al ser new llamado antes que init este método no tendrá como parámetro self ya que este todavía no ha sido creado.

Normalmente no tendremos que sobrecargar el método new a no ser que estemos trabajando con clases como int, tuples o str.

```python
class MyClass:
    def __new__(cls, *args, **kwargs):
        print("Calling __new__")
        instance = super().__new__(cls)
        return instance

    def __init__(self, value):
        print("Calling __init__")
        self.value = value

# Creando una instancia de MyClass
obj = MyClass(10)

#Como hemos explicado new se ejecuta antes que init por lo que primero tendría que salir el print de new y después el de init.
```

# ¿Qué es la diferencia entre deepcopy y copy en Python?

Copy es un módulo utilizado en Python para hacer copias de objetos, este tiene 2 tipos de copias las copias superficiales o (shallow copies) y las copias profundas o (deep copies). La diferencia entre ambas es como se maneja los objetos anidados del objeto que copiamos en caso de las copias superficiales no copiará los objetos anidados, en lugar de eso ambos objetos el copiado y original compartirán las referencias a los objetos contenidos.

```python
import copy

original_list = [1, 2, [3, 4]]
shallow_copy = copy.copy(original_list)

shallow_copy[0] = 10
print(original_list) 
print(shallow_copy)   

# Aquí sí que hará bien el print ya que no hemos modificado el objeto contenido.

shallow_copy[2][0] = 30
print(original_list) 
print(shallow_copy)
# En estos prints tanto el primero como el segundo van a imprimir lo mismo [1,2[30,4]] ya que como hemos visto comparten referencia al objeto contenido en este caso [3,4]
```

Mientras que las copias profundas si que copia los objetos anidados de forma recursiva haciendo que el objeto que hemos copiado y la copia sean dos objetos diferentes.

```python
import copy

original_list = [1, 2, [3, 4]]
deep_copy = copy.deepcopy(original_list)

deep_copy[0] = 10
print(original_list)  # [1, 2, [3, 4]]
print(deep_copy)      # [10, 2, [3, 4]]

deep_copy[2][0] = 30
print(original_list)  # [1, 2, [3, 4]]
print(deep_copy)      # [10, 2, [30, 4]]

```

# Explica qué es el "scope" de una variable y cómo se maneja en Python.

Primero definamos que es el scope o ámbito de una variable esto se refiere a la región de código donde la variable es reconocida y puede ser usada. Python maneja el scope de las variables utilizando unas reglas específicas, conocidas como LEGB.

L: Local Scope (ámbito local): Está definido dentro de una función esta variable solo puede ser usada dentro de la función por ejemplo:

```python
def my_function():
    local_var = 10 
    print(local_var)

my_function()
print(local_var) # si hacemos este print dará un error ya que no reconocerá la variable ya que está definida dentro de la función.  

```

E : Enclosing Scope (Ámbito Envolvente): Se refiere a las variables en funciones anidadas. Una función interna puede acceder a las variables de su función externa.

```python
def outer_function():
    outer_var = 20 

    def inner_function():
        print(outer_var)  # Este print sí funcionará

    inner_function()

outer_function()
```

G: Global Scope (Ámbito Global): Las variables definidas fuera de todas las funciones tienen un scope global y pueden ser accesibles desde cualquier lugar.

```python
global_var = 30 

def my_function():
    print(global_var)  # Accediendo a la variable global

my_function()
print(global_var)  # También accesible
```

B: Built-in Scope: Este es el scope que contiene nombres predefinidos por Python funciones como len() o print()

```python
print(len("Hello, World!"))
```

Y ¿para qué queremos saber esta regla? La idea es que Python a la hora de buscar una variable lo hará en el orden que lo hemos explicado, como se puede ver en este ejemplo.

```python
x = "global"

def outer_function():
    x = "enclosing"

    def inner_function():
        x = "local"
        print(x)  # Imprime "local"

    inner_function()
    print(x)  # Imprime "enclosing"

outer_function()
print(x)  # Imprime "global"
```

El primer print imprime local ya que imprime la variable que está definida en inner_function, el segundo imprime enclosing ya que está en mayor orden de prioridad que global que también se llama x y finalmente el último print imprimirá global ya que las demás no son accesibles en este ámbito.

También tenemos 2 palabras exclusivas para trabajar con el ámbito de las variables estas son global y nonlocal global sirve para inficarle a Python que queremos trabajar con la variable global, mientras que nonlocal sirve para el ámbito envolvente.

# ¿Qué es el "Garbage Collection" en Python y cómo funciona?

El Garbage Collection (recolección de basura) en Python es el proceso de gestión automática de la memoria este se encarga de liberar espacio de memoria ocupado por objetos que ya no son necesarios en el programa.

Python usa una combinación de conteo de referencia y colector de basura generacional.

Conteo de referencia: Basicamente Python tiene un contador de referencias. Cuando este contador llega a cero este objeto va a ser eliminado de memoria veamos un ejemplo.

```python
a = [1, 2, 3]  # El contador de referencias del objeto [1, 2, 3] es 1 ya que se acaba de crear 
b = a          # El contador de referencias del objeto [1, 2, 3] será 2 
del a          # El contador de referencias del objeto [1, 2, 3] es 1 ya que hemos borrado a
b = None       # El contador de referencias del objeto [1, 2, 3] es 0, por lo que puede ser eliminado
```

También tenemos el colector de basuras generacional, veamos un ejemplo y lo explicaremos.

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Creamos dos objetos node y hacemos que se refieran entre ellos
a = Node(1)
b = Node(2)

a.next = b
b.next = a

# Eliminamos las referencias originales.
a = None
b = None

# En este punto, los objetos Node están referenciados entre sí pero si no son accesibles desde ninguna otra parte del programa Python detectará este ciclo y lo podrá llegar a eliminar 
```
Si queremos trabajar manualmente tenemos que importar gc con este módulo podemos habilitar, desabilitar, forzar una recolección y tener unas estadísticas de la recolección.

# ¿Qué es el principio de responsabilidad única (SRP) y por qué es importante?

Empecemos con la definición: Una clase debe tener solo una responsibilidad o propósito, esto también se puede extender a otros conceptos como las funciones. Esto hace que el código sea más mantenible ya que si por ejemplo tenemos una clase que trabaja con los strings de nuestra app por ejemplo para quitarle carácteres especiales, ponerlo todo minúsculas etc. Sabemos que si modificamos esta clase no cambiará en como los datos se añaden a la base de datos. Más legibilidad y entendimientos ya que nos es más fácil entender una función o clase que todo el código haga conceptos parecidos a tener todo el código mezclado y que haga de todo. Mayor reusabilidad en el ejemplo de los strings que he mencionado anteriormente se ve claramente este punto si no mezclamos lógica en esta clase tendremos una clase que podremos usar en otros proyectos. También se hará más fácil el tema de los tests, ya que al tener se pueden hacer pruebas únicas esperando que la función sólo hace lo que dice y no más funcionalidades. Ahora veremos un ejemplo en Python sobre este principio.

```python
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def save_to_database(self):
        # Código para guardar el libro en la base de datos
        # Verificar si el ISBN es un número con una cantidad de 10-13 dígitos
        pass

    # Con SRP
    class Book:
        def __init__(self, title, author, isbn):
            self.title = title
            self.author = author
            self.isbn = isbn

    class BookRepository:
        def save_to_database(self, book):
            # Código para guardar el libro en la base de datos
            # Manejar la lógica de si es correcto el isbn
            pass
    
    class DataTest:
        def is_isbn_correct(self,isbn):
            # Verificar si es correcto
            pass

```

Como vemos en el ejemplo hemos modificado la clase book para que tenga una responsabilidad. La tarea de guardar en base de datos el libro tendría que ser de otra clase. También tenemos que la función de guardar en la base de datos revisa si el ISBN es correcto esto lo deberiamos de cambiar a otra función o en casos en los que tengamos varios datos a ver si están correctos o no podemos crearnos una clase para verificar si los datos se corresponden con lo que nosotros queremos.

# ¿Qué es un entorno virtual en Python y por qué deberías usarlo?

Un entorno virtual es un espacio en el que puedes tener instaladas dependencias en un proyecto sin tener que interferir en las de otros proyectos o globales esto es especialmente útil ya que puede haber proyectos que tengan que usar una dependencia pero en distintas versiones. Otros beneficios son que nos permite tener una mayor facilidad a la hora de mantener las versiones ya que para cada proyecto tendremos versiones específicas, seguridad a lo mejor instalamos un paquete que interfiere con otro de nuestros proyectos, también podemos reproducir el código en otros sistemas asegurandanos que la configuración del nuevo sistema no interfiera.

Para crear un entorno en Python, si desarrollamos con Visual Studio te preguntará si quieres crear un entorno podemos simplemente darle que sí o podemos hacerlo manualmente con consola.

```bash
python -m venv mi_entorno
source mi_entorno/bin/activate
pip install paquete
pip freeze > requirements.txt
deactivate
```

Creamos el entorno, lo activamos, instalamos las dependencias que necesitemos por ejemplo requests, pasamos las dependencias a un archivo requirements.txt y si queremos salirnos del entorno podemos hacerlo con deactivate.

# Qué son los principios SOLID.

