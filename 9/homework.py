
#nomer 1
'''slovarik={'pirog': 200, 'tort': 600, 'zhaba': 500, 'pirozhok': 499}
for i in slovarik.copy():
    if slovarik[i] <= 499:
        slovarik.pop(i)
print(slovarik)'''

#nomer 2
'''slvrk={1: 5, 5: 2}
asd=0
for i in slvrk.copy():
	if slvrk[i] == 5:
		asd+=1
{v:k for k, v in slvrk.items()}
for i in slvrk.copy():
	if slvrk[i] == 5:
		asd+=1
print(asd)'''

#nomer 3
'''a={'e': 3, 'd': 'rtr', 'erwef': 2}
b={'r': 23, 'sdfgsedfg': 32}
a.update(b)
print(a)'''

#nomer 4
'''slovari={'c1': 'Red', 'c2': 'Green', 'c3':None}
for i in slovari.copy():
    if slovari[i] == None:
        slovari.pop(i)
print(slovari)'''

#nomer 5


#nomer 6
'''aa={'wer':23, 'er':'ew'}
print({v:k for k, v in aa.items()})'''

#nomer 7
'''N = int (input(''))
b = [1]*N
c=0
#b = list(map(int,input().split()))

 
for i in range (N):
    b[i] = int (input (''))
 
for i in range (N):
    if b[i] <= 437:
        print ("Crash " + str(i+1))
        c=1
        break
if c == 0:
    print ('No crash')'''