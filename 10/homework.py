#nomer 1
'''lIst'''
'''asdfg=int(input('skiki?: '))
old_list=[]
new_list=[]
ciferka=0
while ciferka < asdfg:
	old_list.append(input('chto hochesh dobavit?: '))
	ciferka+=1

for i in old_list:
     if i not in new_list:
       new_list.append(i)
print(new_list)'''

'''KoRtEzH'''
'''tupl=(1,1,2,3)
new_tupl=[]
for i in tupl:
	if i not in new_tupl:
		new_tupl.append(i)
print(new_tupl)'''

'''StR'''
'''s=input('udar po klaviature: ')
result = []
for i in s:
    if i not in result:
        result.append(i)
print(''.join(result)) ''' 




'''DicT'''

#some problems!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
'''slovarik={1:2, 2:5, 3:5, 4:6, 5:5}
resultat={}
for i, v in slovarik:
	print(i, v)
	if slovarik.get(i) not in resultat:
		print(slovarik.items(i))
		print(slovarik[i])
		resultat.update({slovarik.get(i):slovarik[i]})
print(resultat)'''
#_________________________________




#nomer 2
'''spisok=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
for i in range(len(spisok)-1):
    for j in range(len(spisok)-i-1):
        if spisok[j][-1] > spisok[j+1][-1]:
            spisok[j], spisok[j+1] = spisok[j+1], spisok[j]
print(spisok)'''

#nomer 3
'''n=int(input('chislo: '))
pq=['p', 'q']
new_listochek=[]
for i in range(1,n+1):
	i=f'{i}'
	print(i)
	for x in pq:
		new_listochek.append(x+i)
print(new_listochek)'''

#nomer 4

#nomer 5
'''n,m = list(map(int,input().split()))

if n == 0 and m!=0:
	print('Impossible')
elif m==0:
	print(n, n)
elif n==0 and m==0:
	print(0, 0)
elif n==1:
	print(n+m-1,n+m-1)
elif n < m :
	print(m, m+n-1)
elif n==m:
	print(n,m+n-1)
else:
	print(n, m+n-1)'''