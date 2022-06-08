import numpy as np
import math as m
Ar = np.array([[1., 1., 1., 1., 1., 1., 1., 1.],
               [1.,1.,1.,1.,-1.,-1.,-1.,-1],
               [1.,1.,-1.,-1.,0.,0.,0.,0.],
               [0.,0.,0.,0.,1.,1.,-1.,-1.],
               [1.,-1.,0.,0.,0.,0.,0.,0.],
               [0.,0.,1.,-1.,0.,0.,0.,0.],
               [0.,0.,0.,0.,1.,-1.,0.,0.],
               [0.,0.,0.,0.,0.,0.,1.,-1.]])

b = np.dot(Ar, Ar.T)
c = []
temp = 0
for row in Ar:
    c.append(np.dot(np.array(row),np.array(row).T))
print(b)
print(all(c==np.diag(b)))

d = []
for i in range(len(Ar[0])):
    d.append(Ar[i] * (1 / m.sqrt(c[i])))

#macierz ortonormalna
d = np.array(d)
#transpozycja ortonormalnej
print(d.T)
#odwrotna ortonormalna
print(np.linalg.inv(d))
#d * d^-1
print(np.dot(d,np.linalg.inv(d)))
print(np.diag([1.,1.,1.,1.,1.,1.,1.,1.]).all()==np.dot(d,np.linalg.inv(d)).all())

#zamiana baz
ones = np.diag([1.,1.,1.,1.,1.,1.,1.,1.])
va=np.array([8.,6.,2.,3.,4.,6.,6.,5.])
vb=np.dot(d,va)
print(vb)