a=int(input('enter a number'))
match  a%2:
     case '0':
          print(a**2)
     case '1':
          print(a**3)
     case _:
          print('invalid input')     

