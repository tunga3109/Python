with open('text_files/pi_digits.txt','w') as file_object:
    for i in range(3):
        name = input('name: ')
        file_object.write(f'Hello,{name}\n')