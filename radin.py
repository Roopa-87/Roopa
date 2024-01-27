import random
number=random.randint(100,1000)
while True:
     a=int(input('enter a number'))
     if a==number:
        print('congrats! youn successfully guesed the number')
        break
     elif a< number:
        print('enter  some greater number')
     else:
        print('enter some lesser number')     