"""
3.4 Kirjoita ohjelma, jossa on lista, jossa on kymmenen nimeä. Lisää listaan vanhoista nimistä uusi kappale,
niin että uusi kappale on satunnaisesti valittu nimi listalta, jolloin lista kasvaa samoilla nimillä. Toista tätä
prosessia, kunnes kaikki alkuperäiset nimet on valittu ainakin kerran
"""
import random
def main():
  nimet = [
          "Thorgil Callister",
           "William Hendull",
           "Ysaig Thomasson",
           "Keird Seer",
           "Kerron Heresson",
           "Bertrem Prescote",
           "Nigel Kent",
           "Dooil Shimmin",
           "Rody Gill",
           "Roger Skylycorne"
           ]
  nimet2 = [
          "Thorgil Callister",
           "William Hendull",
           "Ysaig Thomasson",
           "Keird Seer",
           "Kerron Heresson",
           "Bertrem Prescote",
           "Nigel Kent",
           "Dooil Shimmin",
           "Rody Gill",
           "Roger Skylycorne"
           ]
  dupes = 0
  appends = 0
  while dupes < 10:
      nimet.append(nimet[random.randint(0,9)])
      appends = appends + 1
      for i in range(len(nimet2)):
         if nimet.count(nimet[i]) >= 2:
            dupes = dupes + 1
      if dupes < 10:
        dupes = 0

  print(sorted(nimet))
  print(appends)
  
if __name__ == "__main__":
    main()