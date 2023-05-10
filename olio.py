class Kylä:
    def __init__(self):
        self.talot = []
class Talo:
    def __init__(self):
        self.osoite = "ei oler rakennettu"
        self.koko = 0
        self.hinta = 0

    def rakennetaan(self):
        self.koko = 40
        self.hinta = 50000
    def muutataloon(self):
        self.osoite = ("Taitajankatu 6")

perniö = Kylä()
laskuri = 0
while laskuri < 4:
    temptalo = Talo()
    temptalo.rakennetaan()
    osoite = input("Anna Osoite:")
    temptalo.osoite = osoite
    perniö.talot.append(temptalo)
    laskuri += 1

print (perniö.talot)