"""
1.3
Tulosta autojen tiedot seuraavan laisesti: Merkki, väri, vuosimalli, kilometrit, hinta.
Esimerkki tulostuksesta
mersu, tummansininen, , 1994, 10571
volvo, punainen, 1000kg, 1999, 8083
cadillac, vihreä, 2500kg, 1985, 10794
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
  auto1 = Auto("mersu", "tummansininen", 1200, 1994, 200000)
  auto2 = Auto("volvo", "punainen", 1000, 1999, 350000)
  auto3 = Auto("cadillac", "vihreä", 2500, 1985, 150000)
  auto1.LaskeHinta()
  auto2.LaskeHinta()
  auto3.LaskeHinta()

  print(f"{auto1.merkki}, {auto1.väri}, {auto1.väri}, {auto1.kilometrit}, {auto1.hinta}")
  print(f"{auto2.merkki}, {auto2.väri}, {auto2.väri}, {auto2.kilometrit}, {auto2.hinta}")
  print(f"{auto3.merkki}, {auto3.väri}, {auto3.väri}, {auto3.kilometrit}, {auto3.hinta}")
  print("")
  print(vars(auto1))
  print(vars(auto2))
  print(vars(auto3))
  print("")
  print(auto1.__dict__)
  print(auto2.__dict__)
  print(auto3.__dict__)
if __name__ == "__main__":
    main()