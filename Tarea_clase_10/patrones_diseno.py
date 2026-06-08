"""
Patrones de Diseño en Python: Definiciones y Ejemplos
Autor: ChatGPT (OpenAI)
"""

# ================================
# 1. PATRONES CREACIONALES
# ================================

# Singleton
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
            print("Instancia creada")
        return cls._instance

# Ejemplo de uso:
s1 = Singleton()
s2 = Singleton()
print(s1 is s2)  # True - ambas son la misma instancia


# Factory Method
class Product:
    def operation(self):
        pass

class ConcreteProductA(Product):
    def operation(self):
        return "Resultado del Producto A"

class ConcreteProductB(Product):
    def operation(self):
        return "Resultado del Producto B"

class Creator:
    def factory_method(self):
        pass

    def some_operation(self):
        product = self.factory_method()
        return product.operation()

class ConcreteCreatorA(Creator):
    def factory_method(self):
        return ConcreteProductA()

class ConcreteCreatorB(Creator):
    def factory_method(self):
        return ConcreteProductB()

# Ejemplo de uso:
creator = ConcreteCreatorA()
print(creator.some_operation())


# ================================
# 2. PATRONES ESTRUCTURALES
# ================================

# Adapter
class OldPrinter:
    def old_print(self):
        return "Impresión vieja"

class NewPrinter:
    def print(self):
        return "Nueva impresión"

class PrinterAdapter:
    def __init__(self, old_printer):
        self.old_printer = old_printer

    def print(self):
        return self.old_printer.old_print()

# Ejemplo de uso:
old = OldPrinter()
adapter = PrinterAdapter(old)
print(adapter.print())


# Decorator
class Notifier:
    def send(self):
        return "Enviando notificación"

class BaseDecorator(Notifier):
    def __init__(self, notifier):
        self._notifier = notifier

    def send(self):
        return self._notifier.send()

class SMSDecorator(BaseDecorator):
    def send(self):
        return f"{super().send()} vía SMS"

# Ejemplo de uso:
notifier = Notifier()
decorated = SMSDecorator(notifier)
print(decorated.send())


# ================================
# 3. PATRONES DE COMPORTAMIENTO
# ================================

# Observer
class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)

class Observer:
    def update(self, message):
        pass

class ConcreteObserver(Observer):
    def update(self, message):
        print(f"Notificado con mensaje: {message}")

# Ejemplo de uso:
subject = Subject()
observer = ConcreteObserver()
subject.attach(observer)
subject.notify("Actualización importante")


# Strategy
class Strategy:
    def execute(self, a, b):
        pass

class AddStrategy(Strategy):
    def execute(self, a, b):
        return a + b

class SubtractStrategy(Strategy):
    def execute(self, a, b):
        return a - b

class Context:
    def __init__(self, strategy):
        self.strategy = strategy

    def execute_strategy(self, a, b):
        return self.strategy.execute(a, b)

# Ejemplo de uso:
context = Context(AddStrategy())
print(context.execute_strategy(5, 3))  # 8
context.strategy = SubtractStrategy()
print(context.execute_strategy(5, 3))  # 2


