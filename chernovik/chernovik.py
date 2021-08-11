file = open('chernovik/input.txt','w')
n = int(input(''))
n_1 = int(input(''))
file.write(f'{int(input(''))} {n_1}')
file.close()


file_2 = open('chernovik/output.txt','w')
minus = n - n_1
file_2.write(str(minus))
file_2.close()