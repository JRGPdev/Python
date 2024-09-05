class Vehicle:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.is_available = True
        
    def sell(self):
        if self.is_available:
            self.is_available = False
            print(f"El vehiculo {self.brand} ha sido vendido")
        else:
            print(f"El vehiculo {self.brand} no esta disponible")
            
    def check_available(self):
        return self.is_available
    
    def get_price(self):
        return self.price
    
    def star_engine(self):
        raise NotImplementedError("Este metodo no esta implementado por la subclase hija") 
    
    def stop_engine(self):
        raise NotImplementedError("Este metodo no esta implementado por la subclase hija") 
    
class Car(Vehicle):
    def star_engine(self):
        if not self.is_available:
            print(f"El motor del coche {self.brand} ha sido encendido")
        else:
            return f"El coche {self.brand} no esta disponible"
        
    def stop_engine(self):
        if self.available:
            print(f"El motor del coche {self.brand} ha sido apagado")  
        else:
            return f"El coche {self.brand} no esta disponible"  
        
class Bike(Vehicle):
    def star_engine(self):
        if not self.is_available:
            print(f"La bicicleta {self.brand} esta en marcha")
        else:
            return f"La bicicleta {self.brand} no esta disponible"
        
    def stop_engine(self):
        if self.available:
            print(f"La bicicleta {self.brand} esta detenida")  
        else:
            return f"La bicicleta {self.brand} no esta disponible" 
    
class Truck(Vehicle):
    def star_engine(self):
        if not self.is_available:
            print(f"El motor del camion {self.brand} ha sido encendido")
        else:
            return f"El camion {self.brand} no esta disponible"
        
    def stop_engine(self):
        if self.available:
            print(f"El motor del camion {self.brand} ha sido apagado")  
        else:
            return f"El camion {self.brand} no esta disponible" 
        
class Customer:
    def __init__(self, name,):
        self.name = name
        self.purchased_vehicles = []
    
    def buy_vehicle(self, vehicle):
        if vehicle.check_available():
            vehicle.sell()
            self.purchased_vehicles.append(vehicle)
        else:
            print(f"El vehiculo {vehicle.brand} no esta disponible")
            
    def inquire_vehicle(self, vehicle):
        if vehicle.check_available():
            available = "disponible"
        else:
            available = "no disponible"
        print(f"El vehiculo {vehicle.brand} esta {available} y su precio es {vehicle.get_price()}")
        
class Dealership:
    def __init__(self):
        self.inventory = []
        self.customers = []
        
    def add_vehicle(self, vehicle: Vehicle):
        self.inventory.append(vehicle)
        print(f"Vehiculo {vehicle.brand} agregado al inventario")
        
    def register_custormers(self, customer: Customer):
        self.customers.append(customer)
        print(f"Cliente {customer.name} registrado")
        
    def show_available_vehicles(self):
        print("Vehiculos disponibles:")
        for vehicle in self.inventory:
            if vehicle.check_available():
                print(f"{vehicle.brand} por {vehicle.price}")

car1 = Car("Toyota", "Corolla", 20000)
bike1 = Bike("Yamaha", "MT-07", 7000)
truck1 = Truck("Volvo", "VNL 860", 80000)

customer1 = Customer("Carlos")

dealership = Dealership()
dealership.add_vehicle(car1)
dealership.add_vehicle(bike1)
dealership.add_vehicle(truck1)

#mostrar vehiculos disponibles
dealership.show_available_vehicles()

#Cliente comprar un vehiculo
customer1.inquire_vehicle(car1)

#cliente compra un vehiculo
customer1.buy_vehicle(car1)
                
#mostrar vehiculos disponibles
dealership.show_available_vehicles()