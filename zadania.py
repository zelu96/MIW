import numpy as np
import random

plik = open("australian.dat")
lista = []
for line in plik:
    lista.append(list(map(lambda e:float(e) , line.replace('\n','').split(' '))))


x=[1,1,1,1,1,8,5,6,3,2,1,1,1,1]


def odległość(x, lista):
    tmp = 0
    wyn = []
    for j in range(len(lista)):
        tmp = 0
        for e in range(len(lista[j])-1):
           tmp += (lista[j][e] - x[e])**2
        tmp = tmp**(1/2)
        wyn.append((lista[j][-1], tmp))
    return wyn


listaod = odległość(x, lista)
#print(listaod)


def grupowanie(lista):
    tmp = {}
    for i in range(len(lista)):
        c = lista[i][0]
        if c not in tmp:
            tmp[c]=[]
        tmp[c].append(lista[i][1])
    return tmp


gr = grupowanie(listaod)
#print(gr)


def sum(grupa, k):
    count = 0
    wyn = {}
    for j in range(len(grupa)):
        tmp=sorted(grupa[j])
        sumka = 0
        for i in range(k):
            sumka += tmp[i]
        c = list(grupa)[j]
        if c not in wyn:
            wyn[c] = 0
        if sumka in wyn.values():
            return "Brak odpowiedzi"
        wyn[c]+=sumka

    res = min(wyn,key=wyn.get)
    return (res, wyn[res])


suma = sum(gr, 5)
#print(suma)


d = {0: [3, 3, 3], 1: [3, 3, 3]}
test = sum(d, 3)
#print(test)


def euklidesowa(a, b):
    tmp=0
    for e in range(len(lista[a])):
        tmp+=(lista[a][e] - lista[b][e])**2
    tmp=tmp**(1/2)
    return tmp


def euklidesowa_2(lista1, lista2):
    lista1 = lista1[:-1]
    lista2 = lista2[:-1]
    v1 = np.array(lista1)
    v2 = np.array(lista2)
    c=0
    for i in range(len(v1)):
        c += (v1[i]-v2[i])**2

    return c**(1/2)


#print(euklidesowa_2(lista[0], lista[1]))

#print(euklidesowa(0, 1))

#pd całkowanie numeryczne montecarlo  sumy górne lub dolne//prostokątów/trapezów metoda na wykladzie: 28.02 1:10:00

###################################################################################################
###################################################################################################

def funkcja_do_sprawdzenia_całki(x):
 return x

punkty = 5000

def monteCarlo(poczatek, koniec):
    c = 0. # całka
    dx = koniec - poczatek
    for i in range(punkty):
        c += funkcja_do_sprawdzenia_całki(poczatek + random.uniform(0, dx))
    c *= dx / punkty
    return c

print(monteCarlo(1,2))


def prostokat(poczatejk, koniec):
     x1,x2 = koniec - poczatejk;
     n = 10;
     dx = (x2-x1)/n;
     s = 0 #suma
     for i in range(n):
         x = dx*1+x1
         s = s + dx + funkcja_do_sprawdzenia_całki(x)
     return s

print(prostokat(2, 4))

#####################################################################################################
#####################################################################################################

tabTest = np.array([5, 5, 5, 5])


def srednia(wektor1):
    wektor2 = np.ones(len(wektor1))
    wynik = np.dot(wektor1, wektor2)
    return wynik / len(wektor1)


print("Srednia:", srednia(tabTest))
#sr = srednia(tabTest)


#print(sr)



def wariancja(wektor1):
    sr = srednia(wektor1)
    wektorSr = np.ones(len(wektor1))
    a = wektor1 - sr * wektorSr
    b = np.dot(a, a)
    return b / len(wektor1)

print("Wariancja:", wariancja(tabTest))
#print(wariancja(tabTest))