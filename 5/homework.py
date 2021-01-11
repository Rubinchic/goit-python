s = input()
l = len(s)
m = 0
a = 0
count = 0
for i in range(l):
    if s[i] != ' ':
        count += 1
    else:
        if count > m:
            m = count
            a = i - count
        count = 0
 
if count > m:
    m = count
    a = i - count + 1
 
print(s[a:a+m])

#_________________________________

first_max = int(input())
second_max = int(input())
if first_max < second_max:
    first_max, second_max = second_max, first_max
element = int(input())
while element != 0:
    if element > first_max:
        second_max, first_max = first_max, element
    elif element > second_max:
        second_max = element
    element = int(input())
print(second_max)

#___________________________________

