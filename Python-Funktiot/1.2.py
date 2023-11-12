"""
1.2 Kirjoita ohjelma, jossa on kaksi funktiota. Ensimmäinen funktio kirjoittaa haluamasi lauseen. Toinen
funktio kutsuu ensimmäisen funktion. Kutsu toinen funktio.
"""

def main():
    Tulosta("MORO!")

def Tulosta(message):
    print(message)


if __name__ == "__main__":
    main()