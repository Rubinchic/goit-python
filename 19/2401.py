'''
with open('book1.csv', encoding = 'utf-8') as tab:
    total = []
    for line in tab:
        line = line.replace('\n','')
        arr = line.split(';')
        total.append(arr)
print(total)

a = 0
for i in range(1,len(total[1])):
    a += int(total[1][i])
print(a)
'''
'''
with open('book1.csv', encoding = 'utf-8') as tab:
    total = []
    for line in tab:
        line = line.replace('\n','')
        arr = line.split(';')
        total.append(arr)
date = input('Date:\n')
name = input('Name:\n')
error = True
for i in range(1,len(total[0])):
    if total[0][i] == date:
        date = i
        error = False
if error == True:
    print('Error in date')
    '''

with open('Airport.csv', encoding = 'utf-8') as tab:
    total = []
    for line in tab:
        line = line.replace(',',';')
        print(line)
    total.append(line)
with open('Newfile.csv', 'w', encoding='utf-8') as f:
    f.write(total)



