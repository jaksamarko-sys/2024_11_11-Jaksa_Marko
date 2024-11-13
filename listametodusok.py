nyelvek = ['Python', 'C', 'C++', 'Java']
#vátozóhoz mentve megtartja az eredeti listát is
nyelvek2 = sorted (nyelvek)
print(nyelvek2)
print(nyelvek)

#sorbarendezni a listát
nyelvek.sort()
print(nyelvek)

#fordított sorrendbe rendezi a listát
nyelvek.reverse()
print(nyelvek)

#az adott elem előfordulásának indexe
print(nyelvek.index('C'))

#az adott elem hányszor fordul elő
print(nyelvek.count('Python'))

print('C++' in nyelvek)
print('C+++' in nyelvek)

nev="Hello"
print(nev.index("1"))