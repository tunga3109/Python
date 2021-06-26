from abc import ABC, abstractclassmethod
import random

class Employee:
    def __init__(self,name='', dept='general'):
        self.name = name
        self.dept = dept
    
class Manager(Employee):
    def __init__(self, reports=[], *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.reports = reports

class Workbee(Employee):
    def __init__(self, project='', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.project = project

class SalesPerson(Workbee):
    def __init__(self,quota=100, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.quota = quota

class Engineer(Workbee):
    def __init__(self, machine='', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.quota = quota
        self.dept = 'engineering'

class Bird(ABC):
    @abstractclassmethod
    def __init__(self):
        self.distance = 0
    @abstractclassmethod
    def move(self):
        pass
    

class Goose(Bird):
    def __init(self):
        super().__init__()
        self.__speed__ = 5
    

    @property
    def speed(self):
        return self.__speed__
    
    def move(self):
        self.distance += self.speed

class Penguin(Bird):
    def __init(self):
        super().__init__()
        self.__speed__ = 10
    
    def move(self):
        self.distance += self.speed
    

    @property
    def speed(self):
        return self.__speed__
    

class Birdcontroller():
    def __init__(self, birds=[]):
        self.birds = birds
    @classmethod
    def generate_random_bidls(cls, count=100):
        birds = [random.choice((Goose,Penguin)() for _ in range(count))]
        return cls(birds)

    def relocate(self, count = None):
        if count in None or type(count) != int:
            count = 10
        
        steps = random.randint(0,count)

        for _ in range(steps):
            for bird in self.birds:
                bird.move()




    

        