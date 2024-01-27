print('welcome to my bus...')
dest = input('''
select destination by enterin
             1 for delhi
             2 for mumbai
             3 for chennai
             4 for hydrabad
:-''')             
adult_seats = int(input('Number of adults :- '))
child_seats = int(input ('Number of childrens :- '))
category = input('enter \n 1 for ac \n 2 for non ac \n:-')
distance = {'1':2000,'2':800,'3':350,'4':500}
if category =='1':
   adult_price = 10
   child_price = 5
elif category == '2':
   adult_price=5
   child_price=3
total_price=distance[dest]*(adult_price*adult_seats+child_price*)
print('The total amount is:_','total_price,rupees') 
confirm=input('enter "yes" for confirm or press any other key to cancel:-')
if confirm=='yes':
   print('your transactions successfully')
   print('Thank you.....\n.visit again...')
else:
   print('your transaction cancelled')
   print('Thank you..visit again...')
                                       
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
