a=[1,'1',2,2.4,[4,5,6],9,16,'abcd']
for i in a:
    if isinstance(i,int):
        if i%2==0:
          out+=i
        else:
           out-=i
        print(out)
        

