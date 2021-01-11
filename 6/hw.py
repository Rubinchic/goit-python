'''lt = [12,3,'v',54,2,32,'d',5,8,10]
x=0

while x < len(lt):
	if type(lt[x]) is str:
		del lt[x]
		print(lt)
	else:
		x += 1

n = len(lt)

for i in range(n): 
    for j in range(n-i-1):
        if lt[j] > lt[j+1]:
            lt[j], lt[j+1] = lt[j+1], lt[j]
print(lt)'''
#________________________

'''a=[1,4,65,3,5,2]
n=len(a)
for i in range(n): 
    for j in range(n-i-1): 
        if a[j] > a[j+1] : 
            a[j], a[j+1] = a[j+1], a[j]
print(a[2])'''
