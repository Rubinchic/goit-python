#код для того чтобы узнать слово которое чаще всего повторяеться в строке
'''STR = input().split()
unique = dict().fromkeys(set(STR),0)
result = []
for p in range(2):
    for i in range(len(STR)):
        if STR[i] in unique:
            unique[STR[i]] += 1
            leader = STR[i]
    for i in unique:
        if unique[i] > unique[leader]:
            leader = i
    result.append(leader)
    unique.pop(leader)
    unique.fromkeys(unique,0)
for i in range(len(result)):
    print(result[i],end=' ')'''




#2
'''stroka=input(': ')
bukvi =list(''.join(stroka))
new_str=''
for i in bukvi:
	new_str += i.swapcase()
print(new_str)'''

#3
'''strochka=" 'sdfg', 'sdfgsdfgsdfg', 'gh', 'dsfgdsfgsdf', 'kju' "
n=int(input(': '))
print(*(x for x in strochka.split(',') if len(x.strip().split("'")[1]) > n), sep='\n')
'''

#or

'''a = list(map(str, input().split()))
n = int(input())
for i in a.copy():
    print(len(i))
    if len(i) <= n:
        a.remove(i)
print(a)'''

#4
# for all
'''max=0
min =0
for i in a:
   if a[i]>max:
     max=a[i]
   if a[i]<min:
     min=a[i]
'''
#or
'''max=0
min =100000
for i in a:
   if i>max:
     max=i
   if i<min:
     min=i'''



#list
'''listok=[1,5,2,67,3]
for i in range(len(listok)-1):
    for j in range(len(listok)-i-1):
        if listok[j] > listok[j+1]:
            listok[j], listok[j+1] = listok[j+1], listok[j]
print(listok[-1], listok[0])'''

#tuple
'''tupl=(1,5,2,7,43,4567)
sed=list(tupl)
print(sed)
for i in range(len(sed)-1):
    for j in range(len(sed)-i-1):
        if sed[j] > sed[j+1]:
            sed[j], sed[j+1] = sed[j+1], sed[j]
print(sed[-1], sed[0])'''

#set
'''nabor={1,2,4,234,65}
nabor=list(nabor)
for i in range(len(nabor)-1):
    for j in range(len(nabor)-i-1):
        if nabor[j] > nabor[j+1]:
            nabor[j], nabor[j+1] = nabor[j+1], nabor[j]
print(nabor[-1], nabor[0])'''

#5
#tuple
'''tupl=(1,5,2,7,43,4567)
sed=list(tupl)
print(sed)
for i in range(len(sed)-1):
    for j in range(len(sed)-i-1):
        if sed[j] > sed[j+1]:
            sed[j], sed[j+1] = sed[j+1], sed[j]
print(sed)'''

#set
'''nabor={1,2,4,234,65}
nabor=list(nabor)
for i in range(len(nabor)-1):
    for j in range(len(nabor)-i-1):
        if nabor[j] > nabor[j+1]:
            nabor[j], nabor[j+1] = nabor[j+1], nabor[j]
print(nabor)'''

#dict
'''a = {876: 5, 23: 6, 90: 128}
b = a.values()
c = a.keys()
c = list(c)
b = list(b)
for i in range(len(b)):
    for x in range(len(b) - i - 1):
        if b[x] > b[x + 1]:
            b[x], b[x + 1] = b[x + 1], b[x]
print(b)
for i in range(len(c)):
    for x in range(len(c) - i - 1):
        if c[x] > c[x + 1]:
            c[x], c[x + 1] = c[x + 1], c[x]
print(c)'''

def calc(a, b, c):
    if c =='+':
        return(a+b)
    elif c == '-':
        return(a-b)
    elif c == '*':
        return(a*b)
    elif c == '/':
        return(a/b)
f = input('+, -, /, or *')
d = int(input('d: '))
e = int(input('e: '))
print(calc(d, e, f))