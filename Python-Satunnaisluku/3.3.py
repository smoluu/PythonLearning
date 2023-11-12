"""
3.3 Kirjoita ohjelma, jossa on kaksi listaa. Ensimmäisessä listassa on numerot ykkösestä sataan.
([1,2,3,4…99,100). Toinen lista on tyhjä. Lisää toiseen listaan satunnaisia alkioita ensimmäisestä listasta,
kunnes olet lisännyt numeron 7. Sen jälkeen tulosta siirtojen määrä. Aina kun siirrät numeron, poista se
ensimmäisestä listasta.
"""
import random
def main():
  lista1 = []
  lista2 = []
  found = False
  for i in range(1,101):
     lista1.append(i)
  while found == False:
     randomint = random.randrange(0,len(lista1))
     lista2.append(lista1[randomint])
     if lista1[randomint] == 7:
        found = True
     del lista1[randomint]
  print(lista1)
  print(lista2)
  print(f"{len(lista2)} siirtoa")     
if __name__ == "__main__":
    main()