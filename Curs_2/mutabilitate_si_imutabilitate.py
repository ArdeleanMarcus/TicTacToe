# Mutabilitate si imutabilitate
# Daca un obiect nu isi modifica adresa de memorie atunci cand valoarea interna
# a acestuia se schimba, spunem ca acest obiect este mutabil.

# Tipuri de date mutabile:
#   1. Lista
#   2. Dictionar
#   3. Set

# Tipuri de date imutabile:
#   1. Numere(int, float, boolean)
#   2. Strings
#   3. Tupluri
#   4. Frozen Set
#
#
#
#
# Exemplu obiect mutabil

print("Exemplu obiect mutabil.\n")
telefoane = ["iPhone", "Samsung"]

print(f"telefoane = {telefoane}")
print(f"Adresa de memorie initiala lista        -> {id(telefoane)}\n")

telefoane.append("Huawei")
print(f"telefoane = {telefoane}")

print(f"Adresa de memorie lista dupa modificare -> {id(telefoane)}\n")
print("Se poate observa ca adresa de memorie nu s-a modificat dupa ce s-a "
      "mai adaugat un element in lista.\n\n\n")
#
#
#
#
#
#
# Exemplu obiect imutabil
print("Exemplu obiect imutabil.\n")

numar = 5
print(f"numar = {numar}")
print(f"Adresa de memorie initiala numar        -> {id(numar)}\n")

numar = 10
print(f"numar = {numar}")
print(f"Adresa de memorie numar dupa modificare -> {id(numar)}")

print("Se poate observa ca adresa de memorie s-a modificat dupa ce s-a "
      "modificat valoarea variabilei numar.\n\n\n")
