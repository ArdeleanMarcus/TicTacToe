# Instructiunea conditionala if ... elif ... else

"""
Un conditional, este o structura care permite ramificarea codului pe baza
conditilor indeplinite (sau nu).
Se pot folosi operatori aritmetici, logici, de comparatie, de identitate, de
apartenenta pentru a crea conditii complexe.
"""

a = 2

if a < 3:  # Daca aceasta conditie este adevarata, se executa codul de mai jos
    print("a < 3")
else:  # Daca conditia de sus este falsa se executa codul de mai jos
    print("a >= 3")


# Putem avea instrucituni imbricate
a = 2

if a < 3:
    print("a < 3")
else:
    if a == 3:
        print("a == 3")
    else:
        print("a > 3")

# Dar elif ofera o lizibilitate mult mai buna
a = 2

if a < 3:
    print("a < 3")
elif a == 3:
    print("a == 3")
else:
    print("a > 3")


# Operatorul ternar - reprezinta o varianta mai scurta si mai rapida de a
#                     efectua instructiuni conditionale.
a = 5
b = 10
print("a < b") if a < b else print("a >= b")


# Bucla while - ofera un mod de a parcurge o portiune de cod atata timp cat este
#               indeplinita o conditie

i = 0

while i < 5:
    print(i)
    i += 1

"""
Retineti ca nu exista nici o garantie ca bucla while se va executa, deoarece 
conditia este testata inainte de executare.
- Unele limbaje ofera sintaxa do while, dar in python acest lucru nu exista.
- DAR putem crea o bucla infinita si sa testam conditia in interiorul buclei, 
  iar apoi sa folosim break pentru a iesi din bucla daca conditia este falsa.
"""

i = 5

while True:
    print(i)

    if i >= 5:
        break

"""
-	Dupa cum se poate observa, bucla a fost executata cel putin odata
-	Acesta este un model standard si poate fi util intr-o varietate de scenarii
-	Un exemplu ar fi obtinerea numelui unei persoane
"""
min_length = 4  # Lungime minima a numelui

name = input('Please enter your name:')  # Preluare nume

while not(len(name) >= min_length and name.isalpha()):
    # Daca numele nu indeplineste conditia de lungime si de a avea doar
    # caractere alpha, preia din nou numele.
    print("Name must contain at least 4 characters and only alpha characters")
    name = input('Please enter your name:')

print(f'Hello, {name}')


"""
Modul acesta de verificare functioneaza correct, nu are erori, este cod Python 
scris corect, inteligibil, dar are o problema. Observati ca trebuie sa scriem 
codul pentru preluarea numelui de doua ori, este cod duplicat. Pentru a evita 
acest lucru putem folosi "do while"
"""
min_length = 4

while True:
    name = input('Please enter your name:')
    if len(name) >= min_length and name.isalpha():
        # Daca numele este corect, atunci iesim din bucla
        break
    else:
        print(
            "Name must contain at least 4 characters and only alpha characters"
        )

print(f'Hello, {name}')


"""
-	Am vazut cum instructiunea break iese din bucla while si executia se 
    continua pe liniile urmatoare buclei.
-	Uneori vrem doar sa scurtam iteratia curenta dar sa continuam bucla, fara a 
    iesi din bucla in sine.
-   Pentru acest lucru putem folosi cuvantul cheie "continue"
"""
a = 0

while a < 10:
    a += 1

    if a % 2:
        continue

    print(a)


"""
-	Bucla While poate fi folosita si cu o clauza else.
-	Else este executat daca bucla while s-a incheiat in mod normal, adica nu am 
    folosit instructiunea break
-	Sa presupunem ca vrem sa testam daca o valoare este prezenta intr-o lista si 
    daca nu, sa o anexam/sa o adaugam in lista respectiva.
-	Cum facem acest lucru fara instructiunea else ?
"""
my_list = [1, 2, 3]
value = 10
found = False
index = 0

while index < len(my_list):
    if my_list[index] == value:
        found = True
        break
    index += 1

if not found:
    my_list.append(value)

print(my_list)


# -	Si folosind instructiunea else:
my_list = [1, 2, 3]
value = 10
idx = 0

while idx < len(my_list):
    if my_list[idx] == value:
        break
    idx += 1
else:
    my_list.append(value)

print(my_list)


"""
Bucla For

-	In python, un iterabil este un obiect capabil sa returneze valori pe rand.
-	Obiecte iterabile: liste, siruri, obiecte, fisier, etc.
-	Cuvantul cheie for poate fi folosit pentru a parcurge un obiect iterabil.
-	Sintaxa C++ for (int i=0; i<5; i++) {bloc de cod}
-	Aceasta forma a buclei for este pur si simplu o repetitie, care seamana cu 
    bucla while – de fapt este echivalenta.
-	Pentru a folosi bucla for avem nevoie de un obiect iterabil cu care sa lucram
-	Un obiect iterabil simplu este generat prin intermediul functiei range()
"""
for i in range(5):
    print(i)

for x in [1, 2, 3]:
    print(x)

for x in 'hello':
    print(x)

for x in ('a', 'b', 'c'):
    print(x)


"""
-	Cand iteram peste un iterabil, fiecare iteratie returneaza valoarea SAU 
    obiectul urmator din iteratie.
"""
for x in [(1, 2), (3, 4), (5, 6)]:
    print(x)


"""
-	Putem chiar atribui valori individuale ale tuplului unor variabile numite 
    specific
"""
for i, j in [(1, 2), (3, 4), (5, 6)]:
    print(i, j)


"""
-	Break and Continue functioneaza la fel ca in bucla while.
"""
for i in range(5):
    if i == 3:
        continue
    print(i)


for i in range(5):
    if i == 3:
        break
    print(i)


"""
-	Bucla for precum bucla while accepta si o clauza else care este executata 
    daca si numai daca bucla se termina normal (adica nu a iesit din cauza unei 
    instructiuni break)
"""
for i in range(1, 5):
    print(i)
    if i % 7 == 0:
        print('multiple of 7 found')
        continue
else:
    print('No multiples of 7 encountered')


for i in range(1, 8):
    print(i)
    if i % 7 == 0:
        print('multiple of 7 found')
        break
else:
    print('No multiples of 7 encountered')

"""
-	Similar buclei while, clauzele try except finally functioneaza la fel.
"""
for i in range(5):
    print('--------------------')

    try:
        10 / (i - 3)
    except ZeroDivisionError:
        print('divided by 0')
        continue
    finally:
        print('always runs')

    print(i)


"""
-	Exista mai multe moduri prin care putem itera peste iterabile:
"""
s = 'hello'
for c in s:
    print(c)


"""
-	Dar uneori, pentru tipurile indexabile (de exemplu secvente/liste), vrem sa 
    cunoastem si indexul elementului din bucla.
"""
s = 'hello'
i = 0

for c in s:
    print(i, c)
    i += 1

# O abordare putin mai buna ar fi:
s = 'hello'

for i in range(len(s)):
    print(i, s[i])

# Sau si mai bine:
for i, c in enumerate(s):
    print(i, c)

"""
-	Ultima varianta este un standard in Python, cand ne uitam la functia 
    enumerate stim exact ce face. Folosirea celorlalte 2 variante este corect, 
    dar este putin mai greu de citit codul in acest fel
"""
