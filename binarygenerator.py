def binary(a):
  while a>0:
    yield a%2
    a=a//2
out=''  
for i  in binary(100):
    out=str(i)+out
print(out)

                                                                                                                                                                                                                                                                           