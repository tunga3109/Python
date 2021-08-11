#УПР 11.3 стр 235
class Employee():

    def __init__(self,name,surname,salary):
        self.name = name
        self.surname = surname
        self.salary = salary

    
    def give_raise(self,bonus=5000):
        self.salary += bonus


tunga = Employee('chan','tunga',300)
print(tunga.salary)
tunga.give_raise()
print(tunga.salary)
