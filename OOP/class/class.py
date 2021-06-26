from abc import ABC , abstractclassmethod

class Animal(ABC):

    @abstractclassmethod
    def says(self):
        print("KEKS")
    
    def move(self):
        raise NotImplementedError

class Cat(Animal):
    
    def __init__(self,name):
        self.name = name
    
    def __str__(self):
        return str(self.name)
    
    def says(self):
        print("Meow")

cat1 = Cat("Murka")
cat1.says()


try:
    cat1.move()
except NotImplementedError:
    print('NotImplementedError')

print(cat1)


        
    









    









    











        

        
    






    










