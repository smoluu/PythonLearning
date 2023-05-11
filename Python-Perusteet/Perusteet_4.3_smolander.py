# Kirjoita ohjelma, joka kysyy pin-koodia. Pin-koodin arvo on 1234.
#Käyttäjälle tulostetaan, että onko vastaus oikein.

code = "1234"
input = input("Anna koodi: ")
if input == code:
    print("Oikein")
else: print("Väärin")