
lukuA = 10
lukuB = 5

liukulukuA = 0.4

lista = [23,19,25,10]

laskuri = 0
määrä = 5

# while laskuri < määrä:
#     lista.append(10)
#     laskuri = laskuri + 1
# print(lista)
# 
# laskuri = 0
# ###
# while  laskuri < len(lista):
#     templuku = lista[laskuri]
#     templuku += laskuri
#     lista[laskuri] = templuku
#     laskuri = laskuri + 1
# print(lista)
# ###
# laskuri = 0
# tulos = []
# while laskuri < len(lista):
#     templuku = lista[laskuri]
#     tulos.append(templuku)
#     laskuri = laskuri + 2
# print(tulos)
# 
# ###
# for i in range(10,100,10):
#     print(i, end=" ")
#     if i > 30:
#         print("k on isompi kuin 30")
#     if i < 30:
#         print("k on pienempi kuin 30")
###
def summa(*luvut):
    tulos = 0
    for i in luvut:
        tulos += i
    return tulos
    
###

def tulo(kertoja,kerrottava):
    tulos = kerrottava * kertoja
    return tulos

k = tulo(3,2)
for kertoja in range (1,11):
    print("\n")
    for kerrottava in range (1,11):
        
        tulos = tulo(kertoja,kerrottava)
        print(tulos,end="\t")







    