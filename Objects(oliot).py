class Koti:
    def __init__(self):
        self.kori = []

class Kissa:
    def __init__(self):
        self.nimi = "eioleannettu"
        self.paino = 1000
        self.poikaset = []
    def ääntely(self):
        print("miau")

munkissa = Kissa()
munkissa.nimi = "Pöhnä"
nimet = ["jesse","tiikeri","soma","ville","santeri"]

for i in range(5):
    poikanen = Kissa()
    poikanen.nimi = nimet[i]
    munkissa.poikaset.append(poikanen)
    
print(munkissa.poikaset)

for i in munkissa.poikaset:
    print(i,i.nimi,i.paino)