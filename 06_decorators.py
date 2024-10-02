

# if we want to access class functions without the use of its object we use decorators
#And Remember staticmethod can not be accessed by its object

class Car:   
    def __init__(self,brand,model):
        self.brand=brand  # __ This is how we make private attributes cant be accessed outside class
        self.model=model
    @staticmethod
    def general_description():
        return "cars are means of transport"
obj=Car("Toyota","Fortuner")
print(Car.general_description())
