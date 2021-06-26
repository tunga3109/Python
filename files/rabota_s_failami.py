# 1 ex

l = []
f = open('text.txt')
for elem in f:
    for elem_2 in elem:
        l.append(elem_2)
print(l)

# 2 ex

def f(x,n1=1,n2=-1):
    f = open('text.txt')
    f_1 = f.read()
    print(f_1[n1:n2:])

f('text.txt')

