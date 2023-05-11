# Kirjoita ohjelma, johon käyttäjä syöttää auton värin ja iän.
# Jos auto on nuorempi kuin 5 vuotta tai punainen, niin tulosta ”Ostetaan”, muulloin ”Ei osteta”

color = input("Anna auton väri: ")
age = int(input("Anna auton ikä: "))

if age <= 5 or color == "punainen":
    print("Ostetaan")
else:
    print("Ei osteta")