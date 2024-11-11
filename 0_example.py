honapok = ['Január', 'Február', 'Március', 'Április', 'Május']

print(honapok)

#lista hossza: len()
print(len(honapok))

#0. indexű elem
print(honapok[0])

#1. indexű elem
print(honapok[1])

#üres lista létrehozása
szamok = []
#elem hozzáadása
for i in range(1, 11):
    szamok.append(i)            #append-del hozzáadunk elemeket
print(szamok)

print(szamok[2])
print(szamok[9])
#túlindexelés - IndexError: list index out of range
#print(szamok[10])


#utolsó elem megadása hátulról az első elem
print(szamok[-1])
print(szamok[-2])