"""
2.2 Kirjoita ohjelma, joka simuloi noppaa. Jos ohjelma saa silmäluvun kuusi, niin ohjelma tulostaa ”Voitit”,
muulloin ”Hävisit”
"""
import random
def main():
  luku = random.randint(1,6)
  print(luku)
  if luku == 6:
      print("voitit")

    



if __name__ == "__main__":
    main()