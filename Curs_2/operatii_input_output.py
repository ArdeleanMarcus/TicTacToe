# Operatii input/output

# Pentru a prelua date din consola folosim functia input()
# Pentru a afisa in consola folosim print()
nume = input("Scrie numele tau: ")

# Formatare output
# Avem 3 moduri de a printa text impreuna cu valorile unor variabile, cea mai
# folosita varianta este f-string
print("Numele tau este: " + nume)  # Concatenare
print("Numele tau este: {}".format(nume))  # Functia format()
print(f"Numele tau este: {nume}")  # f-string


# Caractere de evadare
print("\n")  # Linie noua
print("Prima linie\nUrmatoarea linie")
print("Inainte de tab\tDupa tab")  # Tab
print("Text care nu o sa fie afisat\rText care o sa fie afisat")  # Mutare
# cursor la inceputul randului
