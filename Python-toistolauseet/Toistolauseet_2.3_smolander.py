""" Kirjoita ohjelma, jossa on muuttujat Bensa ja Moottoriöljy, anna niille arvot 50 ja 5. Kirjoita while-
toistolause, joka toistuu niin kauan, kun bensaa ja moottoriöljyä on jäljellä. Jokaisella toistolla kasvatetaan
muuttujaa kilometrit yhdellä ja vähennetään bensaa 0.5: llä ja moottoriöljyä 0.05: llä. Lopuksi tulosta ajetut
kilometrit seuraavan laisesti: ”Ajettu xxx kilometriä”.
"""

bensa = 50
öljy = 5
km = 0

while bensa > 0 and öljy > 0:
    km += 1
    bensa -= 0.5
    öljy -= 0.05

print("Ajettu",km,"kilometriä")