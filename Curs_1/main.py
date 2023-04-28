# În Python, o linie este comentată folosind simbolul diez, această linie
# fiind ignorată în momentul rulării codului


# Pentru a afișa un text în consolă, în Python folosim funcția print()
print("Text afișat cu ajutorul funcției print")


# Pentru a prelua date din consolă, în Python folosim funcția input()
input("Aici poți scrie text: ")


# O variabilă este un container/un loc în memoria calculatorului unde se va
# stoca/memora o anumită valoare(numere, text etc.). Te poți gândi la acea
# variabilă ca fiind o cutie în care pui anumite lucruri, în cazul nostru
# numere, liste de obiecte etc

# Pentru a atribui o valoare(un numar, un text, o listă de obiecte) unei
# variabile, se folosește operatorul de atribuire și anume semnul egal

# Putem atribui valoarea pe care o scriem în consolă cu ajutorul funcției
# input() unei variabile și pe urmă să afișăm textul stocat în variabila nume
# cu ajutorul funcției print()
nume = input("Cum te numești ? ")
print(nume)


# Mai jos sunt prezentate mai multe moduri în care putem prelua și
# afișa exact aceleași informații


# Varianta 1
print("Varianta 1")
print("Scrie numele tău: ")
nume_1 = input()
print("Numele tău este " + nume_1)

# Varianta 2
print("Varianta 2")
print("Scrie numele tău: ")
nume_2 = input()
print("Numele tău este {}".format(nume_2))

# Varianta 3
print("Varianta 3")
print("Scrie numele tău: ")
nume_3 = input()
print(f"Numele tău este {nume_3}")

# Varianta 4
print("Varianta 4")
print("Scrie numele tău: ", end="")
nume_4 = input()
print(f"Numele tău este {nume_4}")

# Varianta 5
print("Varianta 5")
nume_5 = input("Scrie numele tău: ")
print(f"Numele tău este {nume_5}")


# Diferența dintre varianta 1, 2 și 3 este următoarea:
# În prima variantă folosim concatenare prin folosirea semnului plus
# A doua varianta foloseste o funcție format() care înlocuieste acoladele din
# interiorul textului cu valoarea variabilei care este pusă în interiorul
# functiei
# A treia varianta este foarte similară cu a doua, doar că în loc să folosim
# functia format() scriem direct variabila între acolade


# Diferența dintre varianta 3, 4 și 5 este următoarea:
# În varianta 3, când ne scriem numele în consolă, numele este scris sub textul
# afișat în consolă
# În varianta 4 și 5, când ne scriem numele în consolă, numele este scris pe
# același rând cu textul afișat în consolă


# Varianta 3
# Scrie numele tău:
# Marcus

# Varianta 4 si 5
# Scrie numele tău: Marcus


# Această diferență dintre varianta 3 și 4 apare deoarece implicit, funcția
# print() se termină prin trecerea la rând nou, adica parametrul end este
# end="\n". \n este "o secvență de evadare" care este convertită și tradusă ca
# linie nouă
# Acest comportament al funcției print() poate fi modificat folosind acest
# parametru end, și putem să îi spunem funcției ca la sfârșitul executări să
# rămână pe aceeași linie prin ai transmite un text gol, adică end="".
# La fel putem să îi spunem ca la sfârșit să pună semnul exclamării end="!"
# sau semnul întrebări end="?" sau orice altă combinație de caractere


# Exemple de modificare a comportamentului funcției print()
# Pune semnul exclamarii la sfarsitul textului
print("Imi place programarea", end="!")

# Pune cuvantul programare la sfarsitul textului
print("Imi place ", end="programarea")

# Pune cuvantul programare la sfarsitul textului si in acelasi timp muta
# cursorul pe rand nou datorita secventei de evadare \n
print("Imi place ", end="programarea\n")
