"""
Kirjoita toistolause, joka kirjoittaa listassa olevien lemmikkien nimiä. Nimet tulee kirjoittaa päin
vastaisessa järjestyksessä, eli viimeinen nimi ensimmäisenä. Nimi listassa tulee olla ainakin neljä nimeä.
Huom. Pythonissa on valmiina funktio reverse() ja sen käyttö on tässä tehtävässä kielletty.
"""
nimet = ["Monty", "Xean", "Wilson", "Andor", "Galant", "Xilo"]

for i in range(len(nimet)-1,0,-1):
    print(nimet[i])
