"""
2.4 Kirjoita ohjelma, joka tulostaa ”Hello world”, niin monta kertaa kuin on argumentin arvo.
2 -> Hello world
Hello world
"""

def main(print_Count):
    for i in range(print_Count):
      print(f"hello world")
    



if __name__ == "__main__":
    main(50)