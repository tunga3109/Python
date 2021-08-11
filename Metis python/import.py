# 9.13 стр 914
import random

class Die:

    def __init__(self,sides=6):
        self.sides = sides
    
    def roll_die(self):
        print(f'У вас выпала {random.randint(1,self.sides)}')
    

die = Die(10)
for i in range(10):
    die.roll_die()



#упражнение 9.14 стр 194
try_1 = []
while True:  
    random_num = [1,2,3,4,5,6,7,8,9]  
    ticket = '' 
    win_ticket = '488'

    for i in range(3):
        ran = random.choice(random_num)
        ticket += str(ran)

    if ticket == win_ticket:
        print(f'Вы выиграли, ваш счастливый билет {ticket}')
        break
    else:
        print(f'Вы проиграли, ваш билет {ticket}')
    
    
    try_1.append(ticket)

print(f'Кол-во попыток:{len(try_1)}')
