"""
2.3 Kirjoita ohjelma, joka aloittaa laskemisen numerosta yksi. Ohjelma kasvattaa numero satunnaisluvulla
väliltä 1-6. Lopuksi ohjelma tulostaa, että kuinka monta kertaa lukua kasvatettiin, ennen kuin se saavutti
arvon 100.
"""
import random
def main():
  luku = 0
  count = 0
  while luku <= 100:
     luku = luku + random.randint(1,6)
     if luku > 100:
        print(f"lukua kasvatettiin {count} kertaa")
        break
     count = count + 1

    



if __name__ == "__main__":
    main()