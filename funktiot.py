def summa(a,b):
    tulos = a+b
    return tulos

#print(summa(1,2))

def teelista():
    tuloslista = []
    tuloslista.append(100)
    tuloslista.append(200)
    tuloslista.append(300)
    return tuloslista

def yhdistalista(alista,blista):
    tuloslista = []
    laskuri = 0
    while laskuri < len(alista):
        tuloslista.append(alista[laskuri])
        tuloslista.append(blista[laskuri])
        laskuri += 1
    return tuloslista

muntulos = yhdistalista([0,1,2,3,4],["a","b","c","d","e"])
print(muntulos)

#jakojäännös % modulus
laskuri = 0
while laskuri < 20:
    print ("laskuri: ",laskuri, end=" ")
    if laskuri % 2 == 0:
        print("parillinen")
    if laskuri % 2 >= 1:
        print("pariton")
    laskuri += 1
