class Nikola:
    __slots__ = ['name','age']
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        if self.name == 'Николай':
            print(self.name)
        else:
            print(f'Я не {self.name}, а Николай')

igor = Nikola('Николай',22)
        
    


        



    

