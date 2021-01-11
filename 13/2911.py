def print_nums():
    n = int(input())
    if n > 0: 
        if n % 2:
            print('-',n)
            print_nums()
        else:
            print_nums()
 
print_nums()