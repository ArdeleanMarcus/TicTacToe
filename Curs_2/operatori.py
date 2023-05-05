# Operatori aritmetici ->  + - * / // % **
print("Operatori aritmetici")

num_1 = 4
num_2 = 3

print(f"{num_1} +  {num_2} = {num_1 +  num_2}")   # Adunare
print(f"{num_1} -  {num_2} = {num_1 -  num_2}")   # Scadere
print(f"{num_1} *  {num_2} = {num_1 *  num_2}")   # Inmultire
print(f"{num_1} /  {num_2} = {num_1 /  num_2}")   # Impartire
print(f"{num_1} // {num_2} = {num_1 // num_2}")   # Floor division
print(f"{num_1} %  {num_2} = {num_1 %  num_2}")   # Modulo
print(f"{num_1} ** {num_2} = {num_1 ** num_2}")   # Ridicare la putere
print("\n\n")
#
#
#
#
#
#
#
# Operatori de atribuire ->  = += -= *= /= **=
print("Operatori de atribuire")

var = 5  # Semnul egal este operatorul de atribuire
print(f"var = {var}")

var += 5
print(f"var = var +  5    sau    var +=  5 ---> var = {var} ")

var -= 5
print(f"var = var -  5    sau    var -=  5 ---> var = {var} ")

var *= 2
print(f"var = var *  2    sau    var *=  2 ---> var = {var} ")

var /= 2
print(f"var = var /  2    sau    var /=  2 ---> var = {var} ")

var **= 2
print(f"var = var ** 2    sau    var **= 2 ---> var = {var} ")

print("\n\n")
#
#
#
#
#
#
#
# Operatori de comparatie ->  == != > >= < <=
# Acestia compara valoarea variabilelor

print("Operatori de comparatie")

numar_1 = 10
numar_2 = 5

print(f"{numar_1} == {numar_2} -> {numar_1 == numar_2}")  # Output: False
print(f"{numar_1} != {numar_2} -> {numar_1 != numar_2}")  # Output: True
print(f"{numar_1} >  {numar_2} -> {numar_1 >  numar_2}")  # Output: True
print(f"{numar_1} >= {numar_2} -> {numar_1 >= numar_2}")  # Output: True
print(f"{numar_1} <  {numar_2} -> {numar_1 <  numar_2}")  # Output: False
print(f"{numar_1} <= {numar_2} -> {numar_1 <= numar_2}")  # Output: False
print("\n\n")
#
#
#
#
#
#
#
# Operatori logici -> and, or, not
print("Operatori logici")

val_1 = True
val_2 = False

print(f"    {val_1} and {val_2}  -> {    val_1 and val_2}")   # Output: False
print(f"    {val_1} or  {val_2}  -> {    val_1 or  val_2}")   # Output: True
print(f"not({val_1} and {val_2}) -> {not(val_1 and val_2)}")  # Output: True
print("\n\n")
#
#
#
#
#
#
# Operatori de identitate -> is, is not
# Acestia compara adresa de memorie a variabilelor, daca sunt egale, returneaza
# True, altfel returneaza False
print("Operatori de identitate")

numar_3 = 5
numar_4 = 5

print(f"{id(numar_3)} is     {id(numar_4)}  -> {numar_3 is     numar_4}")
# Output: True
print(f"{id(numar_3)} is not {id(numar_4)}  -> {numar_3 is not numar_4}")
# Output: False
print("\n\n")
#
#
#
#
#
#
#
# Operatori de apartenenta -> in, not in
print("Operatori de apartenenta")

masini = ["Ford", "Audi", "BMW"]
ford = "Ford"

print(f"{ford} in     {masini}  -> {ford in     masini}")  # Output: True
print(f"{ford} not in {masini}  -> {ford not in masini}")  # Output: False
