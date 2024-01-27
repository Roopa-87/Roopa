a="Hello my name is bhanu"
i=0
out=" "
while i<len(a):
    if a[i]==' ':
        out+='_'
    else:
        out+=a[i]
        i+=1
        print(out)
