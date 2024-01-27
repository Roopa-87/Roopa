a=float(input('enter the percentage'))
if  a<=100 and a>90:
    print('A+')
elif a<=90 and a>80:
    print('A') 
elif a<=80 and a>70:
    print('B+')   
elif a<=70 and a>60:
    print('B')         
elif a<=60 and a>50:
    print('c')
elif a<=50 and a>35:
    print('just pass')     
elif a<35:
    print('fail')
else:  
    print('invalid percentage') 

