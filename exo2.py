
from math import sqrt

xa = int(input('Entrer coordonnees xA = '))
ya = int(input('Entrer coordonnees yA = '))

xb = int(input('Entrer coordonnees xB = '))
yb = int(input('Entrer coordonnees yB = '))


distAB = sqrt((xb-xa)**2 + (yb-ya)**2)

print('Distance = ', distAB)

x_milieu = (xb + xa)/2
y_milieu = (yb + ya)/2

print('Milieu = ', x_milieu, ',' , y_milieu)