class Person: # Класс

    def __init__(self, name): #Методы в классах
        self.name = name
    
    def info(self):
        print(self.name)


name1 = Person('Igor') # Название_объекта = название_класса([параметры])
name1.info()

class Student(Person):

    def details(self, course):
        print(self.name,"учиться на", course, "курсе")

name2 = Student('Антон')
name2.details(2)