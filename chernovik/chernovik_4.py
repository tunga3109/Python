per_1 = []
while True:
    name = input('name:')
    age = int(input('age: '))
    per_1.append({'name':name,'age':age})
    if name == '111':
        break

print(per_1)

class Human:

    def __init__(self,name,age,id,sex):
        self.name = name
        self.age = age
        self.id = id
        self.sex = sex

    def eat(self):
        print(self.name, 'я ем')

    def sleep(self):
        print(self.name, 'я сплю')

    def work(self):
        if self.age< 16:
            print(self.name, "я не работаю")
        else:
            print(self.name, "я работаю")      
    
    def __str__(self):
        return f'{self.name}, {self.age}'

h1 = Human('Tunga',21,3,1)
h2 = Human('Igor',15,4,1)

print(h1.age)
h2.work()






