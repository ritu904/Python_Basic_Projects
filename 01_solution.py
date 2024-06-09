class Car:
    total_car =0
    def __init__(self,brand,model):
        self.__brand = brand
        self.__model = model
        Car.total_car +=1

    def get_brand(self):
        return self.__brand + " !"

    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    @staticmethod
    def gen_desc():
        return "I love cars"
    
    @property
    def model(self):
        return self.__model
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
        

my_tesla = ElectricCar("Tesla", "Model S", "85kwh")
print(my_tesla.get_brand())
print(my_tesla.full_name())
#my_tesla.model= "city"
print(my_tesla.model)

my_car= Car("Toyota", "Tata")
print(my_car.full_name())
print(Car.total_car)