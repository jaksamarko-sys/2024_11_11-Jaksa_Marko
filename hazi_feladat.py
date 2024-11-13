"""2.1 Feladat
Készíts egy programot, amely a felhasználótól kis "a" betűvel kezdődő szavakat kér be és ezeket tárolja. Ha a felhasználó nem "a" betűvel kezdődő szót ad meg, akkor azt hagyja figyelmen kívül és ne tárolja. A bekérés egészen addig folytatódjon, amíg a felhasználó ENTER-t nem üt (nem ad meg újabb nevet a bekérésnél)! A program a bekért neveket írja ki a képernyőre!

A program tájékoztatássa a felhasználót a működéséről, és az elvárt adatokról!"""


lista = [] 

valtozo = str("Béla")

while True:
    szo = input("Kérlek adj meg egy szót: ")
    if szo == "":
        break

    if szo.startswith("a") or szo.startswith("A"):
        lista.append(szo)

print("\nA bekért, 'a' betűvel kezdődő szavak:")
for w in lista:
        print(w)