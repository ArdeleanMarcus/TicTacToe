# Python este case-sensitive / sensibil la majuscula
a = 10
A = 15

# a nu este acelasi lucru cu A
# sunt doua variabile diferite, cu 2 valori diferite
print(f"a = {a}, A = {A}")
print(f"{   a } == {   A } -> {a == A}")  # Output: False
print(f"{id(a)} is {id(A)} -> {a is A}")  # Output: False
print("\n\n")


# Folosire typecasting pentru a schimba tipul de data
a = "5"  # tip: string/text
print(f"a = {a} -> {type(a)}")

a = int(a)  # tip: integer/numar
print(f"a = {a} -> {type(a)}")  # Se poate observa ca tipul de data s-a schimbat
print("\n\n")


# Atribuire de mai multe valori la mai multe variabile
# Varianta standard
x_1 = "Banana"
y_1 = "Orange"
z_1 = "Apple"

# Sau varianta simplificata
print(f'x_2, y_2, z_2 = ["Banana", "Orange", "Apple"]')
x_2, y_2, z_2 = ["Banana", "Orange", "Apple"]

print(f"x_1 = {x_1}, y_1 = {y_1}, z_1 = {z_1}")
print(f"x_2 = {x_2}, y_2 = {y_2}, z_2 = {z_2}")
print("\n\n")


# Atribuirea aceleiasi valori la mai multe variabile
print("Atribuirea aceleiasi valori la mai multe variabile")
a = b = c = "Banana"
print(f'a = b = c = "Banana"')
print(f"a = {a}, b = {b}, c = {c}\n\n")

# Preluarea elementelor specifice dintr-un obiect tip secventa
masini = ["Ford", "Audi", "BMW"]
ford = masini[0]
audi = masini[1]
bmw = masini[2]


# Preluarea mai multor elemente dintr-un obiect tip secventa
alimente = ["Lapte", "Oua", "Carne"]
lapte = alimente[0:1]
oua = alimente[1:2]
carne = alimente[2:3]
lapte_si_oua = alimente[0:2]
oua_si_carne = alimente[1:3]

# Se preiau toate elementele daca nu sunt specificate inceputul si sfarsitul
toate_alimentele_1 = alimente[:]

toate_alimentele_2 = alimente[0:3]

# Se preiau toate elementele daca nu sunt specificate inceputul,
# sfarsitul sau pasul
toate_alimentele_3 = alimente[::]

lapte_si_carne = alimente[0:3:2]  # Parcurgem lista din 2 in 2
alimente_inversate_1 = alimente[0:3:-1]
alimente_inversate_2 = alimente[::-1]


# O variabila este formata din 3 lucruri:
#   1. identitate - adresa din memoria calculatorului
#   2. tip - tipul de data (string, integer, lista, tuplu)
#   3. valoare - 100, "albastru"

# Pentru a verifica aceste 3 lucruri folosim urmatoarele functii:
culoare = "albastru"
print(id(culoare))    # identitatea
print(type(culoare))  # tipul
print(culoare)        # valoarea
