rows=int(input('enter anumber of rows:-'))
for  i in range(rows):
    for j in range(rows):
        if i==j:
            print(' ',end='')
        else:
            print('*' ,end='')
    print()