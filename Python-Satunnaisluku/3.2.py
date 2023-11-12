"""
3.2 Kirjoita ohjelma, jossa listasta poistetaan sattumanvaraisesti valittuja alkioita, kunnes jäljellä on vain
yksi alkio. Tulosta jäljelle jäänyt alkio.
"""
import random
def main():
  lista = [1,2,3,4,45,5,56,66,77,8,8,45,45,34,5]
  while len(lista) > 1:
     
    del lista[random.randrange(0,len(lista))]

  print(lista)

if __name__ == "__main__":
    main()