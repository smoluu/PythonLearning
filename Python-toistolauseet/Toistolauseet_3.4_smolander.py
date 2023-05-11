"""
Kirjoita toistolause, joka käy läpi listaa, jossa on ihmisten ikiä. Listassa tulee olla ainakin kuusi numeroa
väliltä 0-100. Jos luku on pienempi kuin 18, niin tulosta ”alaikäinen”, jos toisin niin tulosta ”täysi-ikäinen”.
"""

ages = [1,2,3,4,5,6,6,8,9,10,20,50,60,43,42,50]

for i in range(len(ages)):
    if ages[i] >= 18:
        print(ages[i],"Täysi-ikäinen")
    else:
        print(ages[i],"Alaikäinen")