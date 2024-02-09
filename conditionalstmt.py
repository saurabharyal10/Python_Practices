x = 20
if x%2==0:
    print('even number')
else:
    print('odd number')

year=2022
if (year%4==0 and year%100!=0 or year%400==0):
    print('LeapYear')
else:
    print('Not a LeapYear')

#elif
y=5
if y>0:
    print('Positive')
elif y<0:
    print('Negative')
else:
    print('Zero')
