class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def full_name(self):
        return f"{self.brand} {self.model}"
obj=Car("Toyota","Fortuner")

class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)  #this is what we use to get superclss's attributes
        self.battery_size=battery_size

my_electric=ElectricCar("Tesla","s1","85kwh")
print(my_electric.full_name())