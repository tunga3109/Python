move = ['right','left','up','down']
x = 0
y = 0
count_x = 0
count_y = 0
while True:
    where = input('kuda idem? ')
    if where == move[0]:
        x += 1
        count_x += x
    elif where == move[1]:
        x -= 1
        count_x += x
    elif where == move[2]:
        y += 1
        count_y += y
    elif where == move[3]:
        y -= 1
        count_y += y
    else:
        print(count_x)

        

#move = {'right':0,'left':0,'up':0,'down':0}
#while True:
#    where = input('kuda idem? ')
#    if where == 'right':
#        move['right'] += 1
#        move['left'] -= 1
#    elif where == 'left':
#        move['left'] += 1
#        move['right'] -= 1
#    elif where == 'up':
#        move['up'] += 1
#        move['down'] -= 1
#    elif where == 'down':
#        move['down'] += 1
#        move['up'] -= 1
#    else:
#        print(move)