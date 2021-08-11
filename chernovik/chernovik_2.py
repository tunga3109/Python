def check_int(line):
    while True:
        try:
            a = int(input(line))
        except TypeError:
            print('Введите число')
        else:
            break
    
    return a

print(check_int('Число: '))

       


    
    
        
        
            
        

    
    

    
        
            