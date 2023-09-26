
unit = int(input('enter the units:'))
amount=0
if unit<100:
    print('No Charge',amount)
elif 100< unit <=200:
    amount+=(unit-100)*5
    print('bill is' , amount)
elif  unit>200:
    amount = 500+ (unit-200)*10
    print('bill amount is' , amount)











