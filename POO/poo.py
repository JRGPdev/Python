class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def greet(self):
        print(f"Hola mi nombre es {self.name} y tengo {self.age} años")
        
persona1 = Person("Maria", 25)
persona2 = Person("Juan", 30)
persona3 = Person("Pedro", 35)

persona1.greet()
persona2.greet()