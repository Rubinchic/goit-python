'''
def les(LIST,i,n):
    if i == n+1:
        return LIST[-1]
    else:
        for j in range(n, i - 1, -1):
            LIST[j] += LIST[j - i]
        return les(LIST,i+1,n)
n = int(input())
LIST = [0 for i in range(n+1)]
LIST[0] = 1
print(les(LIST,1,n))
'''
'''
add_one = lambda x: x + 1
print(add_one(2))'''
'''
full=lambda first, last: f'f name: {first.title()} {last.title()}'
print(full('dsf', 'asd'))
'''