"""
1.4 Kirjoita ohjelma, jossa käyttäjä arvaa joko nolla tai yksi. Luo oikea vastaus satunnaisluvulla väliltä 0.0 ja
1.0, ja tulosta ”voitit”, jos satunnaisluku on lähempänä arvattua kuin toista vaihto ehtoa. Muulloin tulosta
”Hävisit!”.
"""
import random
def main():
    arvaus = int(input("valitse 1 tai 0   "))
    random_Float = random.uniform(0.0,1.0)
    print(random_Float)
    if arvaus == 0:
      vastapää = 1
    else: vastapää = 0

    if abs(random_Float - arvaus) < abs(random_Float -vastapää):
       print("voitit")
    else: print("hävisit")

            
    
    print(f"")
    



if __name__ == "__main__":
    main()