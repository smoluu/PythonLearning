"""
3.4 Kirjoita ohjelma, jossa on funktio, joka palauttaa argumenttina syötetyn nimen viimeisen kirjaimen.
Aarni -> i
Tuisku -> u
"""

def main(string):
    
    print(string[-1])
    return string[-1]
    
    



if __name__ == "__main__":
    main("abcfg")