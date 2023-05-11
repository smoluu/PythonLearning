# Kirjoita while-toistolause, jossa laskuri aloittaa laskemisen luvusta yksi ja tuplaantuu joka toistolla,
# kunnes laskuri ylittää sadan. Tulosta luku jokaisella toistolla. (1,2,4,8,16,32,64,128)

luku = 0
kerrottava = 1
while luku < 100 and kerrottava < 100:
    print(kerrottava)
    luku += 1
    kerrottava *= 2