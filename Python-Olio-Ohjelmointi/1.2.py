"""
1.2
Kirjoita auto luokkaan funktio, joka laskee auton hinnan. Hinta rakentuu kahdesta osasta, ikäkerroin ja
kilometrikerroin.
Ikäkerroin lasketaan seuraavasti: 1 + (1 / ikä) * 100.
Kilometrikerroin rakentuu: 1 + (1 / kilometrit) * 10000 * 100)
Lopuksi hinta lasketaan (Ikäkerroin + Kilometrikerroin) * 1000
Pyöristä hinta niin, että hinta on kokonaisluku
"""
from datetime import datetime

class Auto:
    def __init__(self,merkki,väri,paino,vuosimalli,kilometrit):
      self.merkki = "bmw"
      self.väri = "musta"
      self.paino = 1300
      self.vuosimalli = 2006
      self.kilometrit = 180000
    def LaskeHinta(self):
        ikäkerroin = 1+(1/(datetime.now().year - self.vuosimalli) *100)
        kilometrikerroin = 1+(1/self.kilometrit) *1000 *100
        self.hinta = int((ikäkerroin + kilometrikerroin) *100)
      

def main():
  auto1 = Auto("bmw","musta",1200,2006,180000)
  auto1.LaskeHinta()
  print(auto1.hinta)


if __name__ == "__main__":
    main()