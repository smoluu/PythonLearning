# Kirjoita ohjelma, joka kysyy käyttäjän ikää.
#Täysi-ikäiselle tulostetaan ”Tervetuloa” ja alaikäiselle ”Poistukaa”.

age = int(input("Anna ikä:"))

if age >= 18:
    print("Tervetuloa")
else:
    print("Poistukaa")