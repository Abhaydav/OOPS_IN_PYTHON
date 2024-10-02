class Car:   
    def __init__(self,brand,model):
        self.brand=brand  # 
        self.__model=model  #__ This is how we make private attributes cant be accessed outside class
    @property  #by this decorator the the variable will be immutable and can only access through its method .model
    def model(self):
        return self.__model
obj=Car("Toyota","Fortuner")
print(obj.model)

