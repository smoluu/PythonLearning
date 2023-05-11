# Kirjoita ohjelma, johon käyttäjä syöttää iän. Määrittele itse ala- ja ylärajat.
#Jos ikä on rajojen sisällä, niin ohjelma tulostaa ”Rajojen sisällä”.
# Jos ikä on liian nuori, niin tulostaa ”Liian nuori” ja jos liian vanha, niin ”Liian vanha”.

age = int(input("Anna ikä: "))

if age >= 18:
    if age <= 25:
      print("Rajojen sisällä")
    else: print("Liian vanha")
else:
    print("Liian nuori")