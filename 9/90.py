
'''N=int(input(' '))
grib=N//3
petya=grib
vasya=grib
kolya=grib
vasya+=(petya//2)+(kolya//2)
petya=petya//2
kolya=kolya//2
kolya+=(petya//2)+(vasya//2)
vasya//=2
petya//=2
petya+=(kolya//2)+(vasya//2)
kolya//=2
vasya//=2
print(petya)
print(vasya)
print(kolya)'''

'''dict1 = {1: 1, 2: 20, 3: 3, 4: 20}
count = []
for i in dict1:
    if dict1[i] == 20:
        count.append(i)
print(count)'''

ans = {}
names=[]
count = 0
n= int(input(': '))
for i in range(n):
	f=input(' ')
	nm=input('')
	if f in ans:
		ans[f].append(nm)
	if nm in names:
		count += 1
	else:
		ans[f] = [nm]
for i in ans:
	count += len(ans[i])*(len(ans[i])-1)//2
print(count)




