"""
Functii/metode importate din module

-   Modulele sunt fisiere care contin instructiuni si definitii Python
    (variabile, functii, clase).
-   Putem importa modul intregi sau anumite parti din module.
-   Pentru a importa un modul intreg se foloseste instructiunea
    import <nume_modul>
    modul
-   Pentru a importa anumite parti dintr-un modul se foloseste instructiunea
    from <nume_modul> import <nume_clasa/functie>
"""
# Importare modul intreg

import random

my_list = [1, 2, 3]
random_number = random.choice(my_list)
print(random_number)

# Importarea anumitor functii dintr-un modul

from datetime import datetime

date_time = datetime(2023, 5, 17, 16)
print(date_time)


"""
Anotatii

-   folosite pentru a specifica tipul de data pe care ne asteptam ca parametrii 
    functiei sa ii aiba sau pentru a specifica tipul de data pe care ne asteptam
    ca functia noastra sa il returneze.
"""


def func(a: int, b: int) -> int:
    return a * b


func(2, 3)
func("a", 4)
"""
Avertisment pentru primul parametru pozitional, deoarece functia se astepta ca 
primul parametru sa fie un int, nu un str
"""


"""
Docstrings
-   Folosite pentru a specifica ce face functia respectiva precum specificarea 
    mai in detaliu a parametrilor pe care ii primim.
"""


def func(a: int, b: int) -> int:
    """
    Aceasta functie returneaza produsul numerelor a si b.
    :param a: primul numar
    :param b: al doilea numar
    :return: produsul celor doua numere
    """
    return a * b


"""
Positional Arguments / Argumente pozitionale
-   Cel mai comun mod de a trimite argumente functiei
-   Acestia sunt trimisi in ordinea in care au fost specificati in apelul 
    functiei
"""


def my_func(a: int, b: int) -> None:
    print(f"a = {a}")
    print(f"b = {b}")


my_func(10, 20)  # a = 10, b = 20
my_func(40, 50)  # a = 40, b = 50


"""
Keyword Arguments / Argumente cheie
-   Sunt argumente care prezinta numele variabilei pe care trebuie sa o populeze
"""


def my_func(a: int, b: int = 100) -> None:
    print(f"a = {a}")
    print(f"b = {b}")


my_func(a=10, b=20)  # a = 10, b = 20
my_func(b=10, a=20)  # a = 10, b = 20
my_func(a=40)        # a = 40, b = 100 -> b preia valoarea default


"""
-   Argumentii pozitionali pot fi specificati (sau nu) folosind numele 
    parametrilor chiar daca acestia au valori default sau nu.
"""


def my_func(a: int, b: int = 200, c: int = 300) -> None:
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"b = {c}")


my_func(10, 20, 30)        # a = 10, b = 20,  c = 30
my_func(a=10, b=20, c=30)  # a = 10, b = 20,  c = 30
my_func(10)                # a = 10, b = 200, c = 300
my_func(a=10)              # a = 10, b = 200, c = 300
my_func(a=10, b=5)         # a = 10, b = 5,   c = 300
my_func(10, 5)             # a = 10, b = 5,   c = 300

# my_func(10, b=5, 10)
# Eroare: nu pot exista parametri pozitionali dupa parametrii cheie


"""
*args

-   Permite trimiterea mai multor parametri POZTIONALI decat functia poate primi
    in mod normal
-   Acestia vor fi pusi intr-un tuplu.
"""


def my_func(a: int, b: int = 200, *args) -> None:
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"args = {args}")


my_func(10, 20, 30, 40, 50)      # a = 10, b = 20,  args = (30, 40, 50)
my_func(10, 20)                  # a = 10, b = 20,  args = ()


"""
**kwargs

-   Permite trimiterea mai multor parametri CHEIE decat functia poate primi
    in mod normal.
-   Acestia vor fi pusi intr-un dictionar.
"""


def my_func(a: int, b: int = 200, **kwargs) -> None:
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"kwargs = {kwargs}")


my_func(10, 20, c=30, d=40, e=50)
# a = 10, b = 20, kwargs = {"c": 30, "d": 40, "e": 50}

my_func(a=10, b=20, c=30, d=40, e=50)
# a = 10, b = 20, kwargs = {"c": 30, "d": 40, "e": 50}

my_func(10, 20)
# a = 10, b = 20,  kwargs = {}

my_func(a=10, b=20)
# a = 10, b = 20,  kwargs = {}


"""
*args - transferul de parametri catre tuplul args.
"""


def my_func(a: int, b: int, *args, c: int) -> None:
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"args = {args}")
    print(f"c = {c}")


my_func(10, 20, 30, 40, c=50)  # a = 10, b = 20,  args = (30, 40), c = 50
my_func(10, 20, c=20)          # a = 10, b = 20,  args = (), c = 20

"""
-   Observam ca args preia valorile care au ramas neatribuite parametrilor 
    functiei.
-   De asemenea, argumentul c trebuie sa fie specificat tot timpul ca si keyword
    argument in momentul in care apelam functia.
"""


"""
**kwargs - transferul de parametri catre dictionarul kwargs
"""


def my_func(a: int = 100, b: int = 200, **kwargs) -> None:
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"kwargs = {kwargs}")


my_func(10, 20, c=30, d=40, e=50)
# a = 10, b = 20, kwargs = {"c": 30, "d": 40, "e": 50}

my_func(a=10, b=20, c=30, d=40, e=50)
# a = 10, b = 20, kwargs = {"c": 30, "d": 40, "e": 50}

my_func(10, 20)
# a = 10, b = 20,  kwargs = {}

my_func(a=10, b=20)
# a = 10, b = 20,  kwargs = {}

"""
-   Observam ca kwargs preia parametrii cheie-valoare care au ramas neatribuiti 
    parametrilor functiei si ii adauga unui dictionar.
"""
