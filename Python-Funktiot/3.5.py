"""
3.5 Kirjoita ohjelma, joka palauttaa listan pienimmän alkion. Huom. pythonissa on valmiina funktio min(),
jonka käyttö on kiellettyä harjoittelun takia.
"""

def main(string):
    lista = [1223123,2322,223,45555,5,63123,7,12312,766,87,8]
    minimi = lista[0]
    for i in range(len(lista)):
        luku = lista[i]
        if luku < minimi:
            minimi = luku
    print(minimi)
    return minimi
    



if __name__ == "__main__":
    main("abcfg")