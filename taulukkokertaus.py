import random
random.seed(0)
satlu = random.randint(10, 20)
print("satlu", satlu)

taulu = [100, 200, 300]

taulu[2] = satlu

laskuri = 0
t = []

while laskuri < 100:
    satlu = random.randint(0, 100)
    t.append(satlu)
    laskuri += 1

print(t)