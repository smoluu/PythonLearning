# Kirjoita ohjelma, jossa lasketaan kolmen muuttujan keskiarvo. Tulosta lopputulos

luvut = [0,10,20,30,40,50,60,70,80,90,100]

summa = 0
for i in range(len(luvut)):
    summa += luvut[i]

keskiarvo = summa / len(luvut)
print(keskiarvo)