'''n=int(input('igroki: '))
m=int(input('maksimalniy uroven: '))
k=int(input('uroven: '))

if k>m:
	print('k ne mozhet bit bolshe m!!!')
else:
	print(n*(m/k + min(m, k-1))) '''

'''spisok=[1, 3, 5, 7, 9]
del spisok[2:4]
print(spisok)'''

#print('hello'[::-1])

'''a = {'Hello','Lose',"Leader",'Lich'}
b = {'Lose','bed','Lich','Dream'}
for i in a & b:
    if i[0] == 'L':
        print(i)'''

'''a={1, 5, 11, 13}
b={1, 2, 3, 4, 5, 6, 7, 8, 9}
#set2=a.intersection(b)
#print(set2)

for i in b:
    if i > 10:
        a.discard(i)
print(a)'''


'''a = [5, 5, 6, 8, 4, 8]
for i in a:
   if a.count(i) == 1:
       print(i)
'''