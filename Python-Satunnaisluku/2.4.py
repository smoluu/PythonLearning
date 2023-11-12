"""
2.4 Kirjoita ohjelma, jossa luku on nolla. Lukua kasvatetaan ja vähennetään vuorotellen satunnaisluvulla
väliltä 1-6. Jos luku on -10 tai vähemmän, tulosta ”Pelaaja 1 voitti”, jos luku on 10 tai enemmän, tulosta
”Pelaaja 2 voitti”.
"""
import random
def main():
  luku = 0
  vähennys= True

  while luku < 10 or luku <-10:
    if vähennys == True:
      luku = luku - random.randint(1,6)
      vähennys = not vähennys
    else:
      luku = luku + random.randint(1,6)
      vähennys = not vähennys

    if luku <= -10:
      print("Pelaaja 1 voitti")
      break
    if luku >= 10:
      print("Pelaaja 2 voitti")
      break





if __name__ == "__main__":
    main()