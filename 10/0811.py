
'''slovarik={'masha':0,'petya':0,'olya':0,'others':0}

kol_vo=int(input('vedite kol_vo lydey: '))
afg=[]

for i in range(0, kol_vo):
	afg.append(input('imena: '))

for string in afg:
    if string in slovarik:
        slovarik[string] += 1
    else:
        slovarik['others'] += 1
print(slovarik)'''

'''n=int(input('skiki?: '))
slovarik={}
for i in range(0,n):
	name=input('imya:  ')
	age=int(input('vozrast:  '))
	slovarik[name]=age


for i in slovarik.copy():
    if slovarik[i] <= 17:
        slovarik.pop(i)
print(slovarik)'''



'''slovarichek={}
afg=[input(' ')]
n=int(input('skiki?: '))
for i in range(0,n):
	name=input('imya:  ')
	age=int(input('ciferka:  '))
	slovarichek[name]=age
for string in afg:
    if string in slovarichek:
        slovarichek.pop(string)
print(slovarichek)'''



d = {}
for i in range(int(input())):
    for word in input().split():
        d[word] = d.get(word, 0) + 1
for i in sorted(d.items(), key=lambda x: (x[0])):
    if i[1] == max(d.values()):
        print(i[0])




