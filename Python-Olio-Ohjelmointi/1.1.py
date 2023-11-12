"""
1.1
Kirjoita luokka nimeltä ”auto”. Luokasta tulee löytyä muuttujat merkki, väri, paino, vuosimalli, kilometrit,
hinta. Lisää muuttujien merkki, väri, paino, vuosimalli ja kilometrit arvot itse.
Luo listaan vähintään 3kpl auto-olioita. Voit keksiä olioiden muuttujien arvot itse. Auto-oliot tulee lisätä
listaan nimeltään Autot.
Esimerkki listaan lisäämisestä
Auto1 = Auto()
Autot = []
Autot.append(Auto1)
Esimerkki arvoja:
mersu, tummansininen, 1200kg, 1994, 200000
volvo, punainen, 1000kg, 1999, 350000
cadillac, vihreä, 2500kg, 1985, 150000
"""

class Auto:
    def __init__(self,merkki,väri,paino,vuosimalli,kilometrit,hinta):
      self.merkki = "bmw"
      self.väri = "musta"
      self.paino = 1300
      self.vuosimalli = 2006
      self.kilometrit = 180000
      self.hinta = 12000

def main():
  autot = []
  auto1 = Auto("mersu", "tummansininen", 1200, 1994, 200000, 1500)
  auto2 = Auto("volvo", "punainen", 1000, 1999, 350000, 10)
  auto3 = Auto("cadillac", "vihreä", 2500, 1985, 150000, 100000)

  autot.append(auto1)
  autot.append(auto2)
  autot.append(auto3)
  print(autot)


if __name__ == "__main__":
    main()