class Tahti:
    def __init__(self):
        self.nuottilista = []
    def transponointi(self,määrä):
        for n in self.nuottilista:
            n.korkeus +=määrä

class Nuotti:
    def __init__(self):
        self.korkeus = 60
        self.alkuaika = 0
        self.kesto = 1
        
a = Tahti()

for x in range(12):
    tempnuotti = Nuotti()
    tempnuotti.korkeus = 60 + x
    tempnuotti.alkuaika = x
    a.nuottilista.append(tempnuotti)


a.transponointi(5)
    
for n in a.nuottilista:
    print(n.alkuaika,n.korkeus)