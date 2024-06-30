import random

class Expert:
    def __init__(self) -> None:
        self.id = "void"
        self.audio = 0
        self.light = 0
        self.stage = 0
        self.general = 0
        self.combined_sustability = 0

    def calculate_combined_sustability(self,prefs):
        self.combined_sustability = (self.audio * prefs[0]) + (self.light * prefs[1]) + (self.stage * prefs[2]) + (self.general * prefs[3])
        

class Selector:
    def __init__(self) -> None:
        self.audiop = 20
        self.lightp = 2
        self.stagep = 5
        self.generalp = 1
        self.experts = []
        self.num_of_experts = 20
        self.guide = 0
        random.seed(self.guide)
        self.perf = (
            self.audiop,
            self.lightp,
            self.stagep,
            self.generalp
        )

    def fillexpers(self):
        for n in range(self.num_of_experts):
            tmpe = Expert()
            tmpe.id = n
            tmpe.audio = random.randint(1,1000)
            tmpe.light = random.randint(1,1000)
            tmpe.stage = random.randint(1,1000)
            tmpe.general = random.randint(1,1000)
            self.experts.append(tmpe)

    
    def sort_using_preference(self):
        for e in self.experts:
            e.calculate_combined_sustability(self.perf)
        
        self.sorted_experts = sorted(self.experts, key= lambda expert: expert.combined_sustability, reverse=True)


selector = Selector()
selector.fillexpers()
selector.sort_using_preference()

print(f"index audio light stage general combined_sustability")
for index, e in enumerate(selector.sorted_experts):
    print(index,":  ",e.audio," ", e.light," ", e.stage," ",e.general,"   ", e.combined_sustability)