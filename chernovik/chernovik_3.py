question = input('Кушать хочешь? ')
if question == 'да':
    question_2 = int(input('Выбери блюдо:\nкартошка с мясом - 1\nпаста - 2\nпельмени - 3\n'))
    if question_2 == 1:
        print('Очень долго готовить!')
    elif question_2 == 2:
        print('Ок,сейчас подогрею')
    elif question_2 == 3:
        print('Закончилась сметана')
else:
    print('Пока!')


    



        
    
