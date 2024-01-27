def fun(n):
    a=b=1
    for i in range(n):
        a=b
        yield a
        b=a+b
out=fun(20)
print(list(out))        