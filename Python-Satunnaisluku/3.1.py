"""
Listat
3.1 Kirjoita ohjelma, jossa tulostetaan sattumanvaraisesti listasta valittu alkio.
"""
import random
def main():
  lista = [1,2,3,4,45,5,56,66,77,8,8,45,45,34,5]

  print(lista[random.randrange(0,len(lista))])



if __name__ == "__main__":
    main()