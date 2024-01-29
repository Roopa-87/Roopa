def fun():
    def inner(a,b):
        return a+b
    return inner
out=fun()
print(out(2,3))