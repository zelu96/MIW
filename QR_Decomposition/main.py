from sympy import *
#Tworzenie macierzy A
A = Matrix([2, 0, 1, 1, 0, 1]).reshape(3, 2)
pprint(A)

#pobieramy pierwsza kolumne z macierzy A czyli wektor v1
v1 = A[:, 0]
pprint(v1)

# do u1 przypisujemy v1, poniewaz piewsza kolumna jest taka sama
u1 = v1
#liczymy długość v1, wykorzystałem gotowa funkcje z biblioteki sympy
# ||v1|| = math.sqrt(v11**2 + v12**2 + v13**2)
u1_norm = u1.norm()
pprint(u1_norm)

#liczymy e1
# u1 = v1 / || v1 ||
e1 = u1 / u1_norm
pprint(e1)

v2 = A[:, 1]
pprint(v2)

#liczymy projekcję
proj_u1_v2 = (u1.dot(v2) / (u1.dot(u1))) * u1
pprint(proj_u1_v2)

#liczymy u2
u2 = v2 - proj_u1_v2
pprint(u2)

#liczymy długość u2
u2_norm = u2.norm()
pprint(u2_norm)

#liczymy e2
e2 = u2 / u2_norm
pprint(e2)

#macierz QR
Q = Matrix([e1, e2]).reshape(2, 3).transpose()
pprint(Q)

#odwracamy macierz Q
QT = Q.transpose()
pprint(QT)

#liczymy macierz R
R = QT * A
pprint(R)

#sprawdzamy czy Q*R = A
check = Q * R
pprint(check)
if check == A:
    print(True)
else:print(False)

