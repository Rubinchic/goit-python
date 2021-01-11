'''a=[]
a1=''
while a1 != '!':
	a1 = input('! для завершения: ')
	a.append(a1)
score = 0
for i in range(0, len(a)):
	score1 = 0
	for s in range(0,len(a)):
		if a[i] == a[s]:
			score1 += 1
	if score1 != 1:
		score += 1
print(f'result: {score}')'''

#______________________________________

'''lt = [12,3,54,2,1,23,32,5,8,10,10]
n = len(lt) 

for i in range(n): 
    for j in range(n-i-1): 
        if lt[j] > lt[j+1] : 
            lt[j], lt[j+1] = lt[j+1], lt[j]
for i in range(len(lt)): 
    print(lt[i])'''

#_________________________________________

#a = [1,2,3,4]
#a = a[::-1]
#print(a)

#________________________________

'''s=int(input('live:'))
e=int(input('kuda nado:'))
n=int(input('vsego skolko:'))

choose1 = 0
choose2 = 0
if s > e:
	choose1=s-e-1
else:
	choose1=e-s-1
choose2=n-choose1-2
if choose1-choose2:
	print('result:' choose1)
else:
	print('result:' choose2)'''

#_________________________________