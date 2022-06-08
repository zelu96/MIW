# pierwsze zajęcia
print("Hello world")
strings = ['ala', 'ma', 'kota', 'i', 'psa']
x = "_".join(strings)
print(x)
x_split = x.split("_")
print(x_split)
print(type(x_split))
zdanie = "Metody Inżynierii Wiedzy są najlepsze"
print(zdanie)
print(zdanie.lower())
print(zdanie.upper())
zdanie_bez_pl = zdanie.replace("ż", "z").replace("ą", "a")
print(zdanie_bez_pl, len(zdanie_bez_pl))
set = set(zdanie_bez_pl)
print(set, len(set))
tupka = ("pierwszy", 1)
print(tupka)
print(type(tupka))
slownik = {"pierwszy": 1}
print(slownik)
print(type(slownik))

literki = ['b', 'a', 'c']
cyferki = [2, 1, 3]
print(literki + cyferki)
literki.append(cyferki)
print(literki.index("c"))

cyferki2 = [0, 1, 2, 3, 4]
cyferki3 = [6, 7, 8, 9]
cyferki2.append(5)
cyferki2.extend(cyferki3)
print(cyferki2)

dict = {'a': 2, 'b': 1, 'c': 4, 'd': 3}
print(dict)
dict_sort = {k: v for k, v in sorted(dict.items(), key=lambda item: item[1])}
print(dict_sort)

tf = [' ', '', 0, 1, '0', '1', [], [',']]
for x in tf:
    print(bool(x))

for x in range(0, 21, 1):
    print(x, end=" ")
print("")

to_split = " ".join(strings)
print(to_split)


def my_split(to_split):
    split = []
    start = 0
    for x in range(0, len(to_split), 1):
        if (to_split[x] == " "):
            split.append(to_split[start:x])
            start = x + 1
    split.append(to_split[start:x + 1])
    return split


print(my_split(to_split))

numbers = [1, 2, 3, 4, 5, 99, 6, 7, 8, 9]


def index_99(numbers):
    x = 0
    while (x >= len(numbers)):
        if (numbers[x] == 99):
            return x
        x += 1
    return -1


print(index_99(numbers))
