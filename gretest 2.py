a=int(input('enter a number'))
b=int(input('enter a  number'))
c=int(input('enter a number'))
if a>b and a>c:
    if b>c:
       print(b,'is the greatest number')
    else:
        print(c,'is the greatest number')   
elif b>c:
    if a>c:
        print(a,'is the greatest number')
    else:
        print(c,'is the greatest number')
else:
    if a>b:
        print(a,'is the greatest number')
            

