a=input('enter  a frist number')
b=input('enter a second number')
c=input('enter a operator')
match a,b:
    case "+":
        print(a+b)
    case '-':
        print(a-b) 
    case _:
        print('enter a valid input')     