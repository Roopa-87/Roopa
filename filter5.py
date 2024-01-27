a=[1,2,[4,5,6],'XYZ',(4,1,2,3)]
def fun(arg):
    if type(arg)in[str,tuple,list,set,dict]:
        return len(arg)
    else:
        return arg
print(list(map(fun,a)))