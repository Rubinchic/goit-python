
'''sl = 'abcdefghijklmnopqrstuvwxyz'
cl = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
answer = input('Введите строку для сортировки: ')
s = []
c = []
ch = []
num = []

for i in range(0,len(answer)):
    if answer[i] in sl:
        s.append(answer[i])
    elif answer[i] in cl:
        c.append(answer[i])
    else:
        ch.append(answer[i])
        num.append(i)
print(s)
print(c)
print(ch)
print(num)'''
#______________________________________

'''squares = [i * i for i in range(10)] 
print(squares)
cubes = [i * i * i for i in range(1,11,1) if i % 2 != 0]
print(cubes)
chetnie = [i for i in range(15) if i%2==0 and (i<=6 or i>=10)]
print(chetnie)'''

#_____________________________________

'''a = input() 
s = [l for l in a if l in 'aeyuio'] 
print(s) '''
