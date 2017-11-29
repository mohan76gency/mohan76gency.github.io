#NumberOne

Number=(input('Please enter a number: '))
New=2*int(Number)
print('Your number multiplied by two is '+str(New)+'.')

#NumberTwo

Yip=input('Please enter another number: ')
if int(Yip)%2==0:
    print('Your number is even!')
else:
    print('Your number is odd!')

#NumberThree

import turtle
egg=turtle.Turtle()
newnumber=(input('Please enter the last number: '))
for i in range(4):
    egg.forward(int(newnumber))
    egg.right(90)
print('The square I drew had the side length of the number you just entered!')
