# Ejercicio 1:
# Una de las principales críticas es que pueden generar una complejidad innecesaria. 
# En proyectos pequeños, implementar un patrón puede significar crear más clases y 
# estructuras de las realmente necesarias. Por ejemplo, utilizar el patrón Singleton
# para controlar una única instancia de un objeto puede resultar excesivo cuando 
# simplemente se podría crear el objeto normalmente.

# Otra crítica frecuente es la sobreingeniería. Algunos desarrolladores intentan aplicar
# patrones a cualquier situación, incluso cuando el problema puede resolverse 
# con una solución mucho más simple. Esto provoca que el código sea más difícil de 
# entender para otros integrantes del equipo.

# También se cuestiona que ciertos patrones agregan muchas clases o niveles de
# abstracción. Un caso típico es Factory Method, donde para crear distintos tipos
# de objetos pueden terminar apareciendo varias subclases que complican la estructura
# del proyecto cuando un constructor convencional sería suficiente.

# Además, algunos patrones pueden dificultar el mantenimiento del código. 
# Patrones como Decorator o Strategy aportan flexibilidad, pero si se utilizan en
# exceso la lógica de la aplicación queda distribuida entre muchos objetos, haciendo
# más difícil seguir el flujo de ejecución.

# Como ejemplo concreto, el patrón Singleton suele ser criticado cuando se utiliza 
# como reemplazo de variables globales. Esto puede generar dependencias ocultas y 
# problemas durante las pruebas del sistema. De manera similar, emplear Decorator 
# para agregar una funcionalidad muy simple puede resultar innecesario cuando una 
# función adicional resolvería el problema con menor complejidad.

# Por último, en lenguajes como Python algunos patrones clásicos pierden relevancia
# porque el propio lenguaje ofrece mecanismos más flexibles y dinámicos. 
# Características como funciones de primera clase, decoradores y otras herramientas
# integradas permiten resolver ciertos problemas sin necesidad de implementar patrones completos.

# Ejercicio 2:
# Selección de patrones implementados en el archivo "patrones_diseno.py":
#   - Creacional: Factory Method (ConcreteCreatorA / ConcreteCreatorB)
#   - Estructural: Adapter (PrinterAdapter)
#   - Comportamiento: Strategy (Context, AddStrategy, SubtractStrategy)
#
# Ejercicio 2 - Ejemplos de uso concreto:
#   Factory Method: permite crear objetos sin acoplar el código cliente a las
#   clases concretas, ideal para crear distintos tipos de productos según el
#   contexto.
#   Adapter: permite usar una interfaz antigua con una nueva, por ejemplo para
#   adaptar una impresora vieja a una API moderna.
#   Strategy: permite cambiar el algoritmo en tiempo de ejecución, por ejemplo
#   para seleccionar distintas formas de calcular precios, enviar notificaciones
#   o procesar pagos.
#
# Ejercicio 3: Problemas diarios donde aplicar patrones de diseño:
# 1. Organización de tareas personales: elegir entre diferentes formas de
#    ordenar una agenda, lista de compras y recordatorios según prioridades,
#    similar a usar Strategy para cambiar la forma de decidir qué hacer primero.
# 2. Manejo de recursos domésticos compartidos: coordinar el uso de la lavadora,
#    la cocina o el automóvil en una familia, donde una sola “instancia” de cada
#    recurso debe ser usada de manera ordenada, como en un Singleton.
# 3. Selección de rutas para ir al trabajo o a una reunión: decidir si tomar
#    transporte público, coche o bicicleta según condiciones de tráfico,
#    clima y tiempo disponible, comparable a usar Factory Method para elegir
#    la mejor alternativa en cada caso.
#
# Ejercicio 4: Nombres alternativos de patrones comunes:
#   - Singleton: Monostate, Instancia única, Single Instance
#   - Factory Method: Método de fábrica, Fábrica, Constructor virtual
#   - Adapter: Adaptador, Wrapper, Translador
#   - Decorator: Decorador, Envoltorio, Extensor dinámico
#   - Observer: Observador, Publicar-Suscribir, Listener, Suscriptor de eventos
#   - Strategy: Estrategia, Política, Algoritmo intercambiable
#   - Facade: Fachada, Interfaz simplificada, Envoltorio de subsistema
#
# Ejercicio 5: ¿Qué son los antipatrones?
# - Los antipatrones son soluciones recurrentes pero ineficaces o problemáticas.
#   Parecen resolver un problema, pero generan malas prácticas, rigidez y errores.
# - Ejemplos:
#   * God Object: un objeto que concentra demasiadas responsabilidades y datos.
#   * Spaghetti Code: código desordenado y enredado sin estructura clara.
#   * Golden Hammer: usar siempre la misma herramienta o patrón para todo.
#   * Lava Flow: código antiguo que permanece porque da miedo cambiarlo.
#   * Singleton abusivo: usar singleton como variable global, lo que dificulta
#     pruebas y control de estado.
#
# Ejercicio 6 (opcional): Otras buenas prácticas como SOLID:
# - S: Single Responsibility Principle (una clase debe tener una sola razón de cambio).
# - O: Open/Closed Principle (abierto para extensión, cerrado para modificación).
# - L: Liskov Substitution Principle (las subclases deben ser intercambiables con
#      sus superclases).
# - I: Interface Segregation Principle (interfaces pequeñas y específicas).
# - D: Dependency Inversion Principle (depender de abstracciones en vez de
#      detalles concretos).
#
# Estos principios ayudan a mantener código más limpio, flexible y fácil de
# mantener.
