a=[2,8,6,4,3,2,3,1,2,8,9]
out=list(map(lambda k:k**3,filter(lambda i:i%2==0,a)))
print(out)
