class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def full_name(self):
        return f"{self.brand} {self.model}"
obj=Car("Toyota","Fortuner")

class Battery:
    def battery_info(self):
        return "this is battery"

class Engine:
    def engine_info(self):
        return "this is Engine"

class Electric(Battery,Engine,Car):
    pass
obj=Electric("Mahindra","Thar")
print(obj.battery_info())
print(obj.engine_info())