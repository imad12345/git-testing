
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

delta = b**2 - 4 *a *c

if delta >0:
    x1 = (-b + delta**0.5)/(2*a)
    x2 = (-b - delta**0.5)/(2*a)
    print('Les racines sont :')
    print('x1 = ', x1)
    print('x2 = ', x2)
elif delta == 0:
    x1 = -b/(2*a)
    print('Une seule racine :')
    print('x1 = ', x1)
else:
    print('Pas de solution réelle')

    
