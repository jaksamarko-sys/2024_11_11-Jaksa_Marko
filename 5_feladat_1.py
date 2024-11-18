"""A program tároljon egy listában színeket. Kérjen be a felhasználótól egy színt, és állapítsa meg, hogy a megadott szín már szerepel-e az adott listában. A vizsgálat eredményéről tájékoztassa a program a felhasználót, és írja ki egymás mellé vesszővel elválasztva a lista által tartalmazott színeket!
"""


# Ha a szín nem szerepel a listában egészítsd ki a listát a színnel majd print-eld is ki a lsitát a színnel
színek = ['kék', 'piros', 'fehér', 'fekete', 'zöld', 'sárga', 'barna', 'piros', 'fehér', 'szürke']

szín = input('Adj meg egy színt!\t')
if szín in színek:
	print('A megadott szín szerepel a listában.')
else:
    print('A megadott szín nem szerepel a listában.')
    színek.append(szín)
    print(f'Az új lista kiegészítve: {színek}')

if szín in színek:
    színek.remove(szín)
else:
    print(f'Nincs a listában ilyen elem: (szín)') 
print(színek)