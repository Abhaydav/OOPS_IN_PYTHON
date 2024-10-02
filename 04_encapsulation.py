class Car:
    def __init__(self,brand,model):
        self.__brand=brand  # __ This is how we make private attributes cant be accessed outside class
        self.model=model

    def get_brand(self):
        return self.__brand
obj=Car("Toyota","Fortuner")
# print(obj.__brand)
print(obj.get_brand())
