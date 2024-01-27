rows=int(input('enter number of rows:-'))
temp=rows//2
out=' '
for i in range (rows):
    for j in range(rows):
        if i in[0,rows-1,]or j in [0,rows-1]:
          out+='*'
    else:
          out+=' '
    out+='\n'
print(out)