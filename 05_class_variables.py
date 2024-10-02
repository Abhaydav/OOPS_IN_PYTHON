class Car:
    total_car=0   # VARIABLE
    def __init__(self,brand,model):
        self.__brand=brand  # __ This is how we make private attributes cant be accessed outside class
        self.model=model
        Car.total_car+=1
    def get_brand(self):
        return self.__brand
obj=Car("Toyota","Fortuner")
# print(obj.__brand)
print(obj.get_brand())
print(Car.total_car) # this is how we access Class Variable

