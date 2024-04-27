import random
print("""
    1-> Part A (with Number of Machines)
    2-> Part B (with Subnet Number)
""")
secim = int(input("Select Menu: "))
def ustAl(bit):
    us = 8 ; sonuc = 0
    for i in bit:
        for j in range(us):  # us alma
            top = int(i) * (2 ** j)
        sonuc = sonuc + top
        us = us - 1
    return sonuc
def fonk(a, fark):
    topDizi = [];topDizi1 = [];dizi = [];toplam = '';toplam1 = ''
    for x in range(fark):
        dizi.append(0)
    for y in ikilikTabani:
        dizi.append(int(y))
    for s in range(8):
        agDizi[0] = dizi[0]; agDizi[1] = dizi[1] ; broadCast[0] = dizi[0] ; broadCast[1] = dizi[1]
        topDizi.append(dizi[int(s)] * agDizi[int(s)])
        top = dizi[int(s)] + broadCast[int(s)]
        if top == 2:
            top = 1
        topDizi1.append(top)
    for k in topDizi:
        toplam = toplam + str(k)
    for l in topDizi1:
        toplam1 = toplam1 + str(l)
    print("{}.Last Octet of the Network Address: {}".format(a + 1, toplam))
    print("{}.Network Address: 192.158.69.{}".format(a + 1, ustAl(toplam)))
    print("Last Octet of {}.BroadCast Address: {}".format(a + 1, toplam1))
    print("{}.BroadCast Address: 192.158.69.{}".format(a + 1, ustAl(toplam1)))
def farkı(fark):
    if fark == 0:
        fonk(i, fark)
    elif fark1 == 1:
        fonk(i, fark)
    elif fark1 == 2:
        fonk(i, fark)
    elif fark1 == 3:
        fonk(i, fark)
    elif fark1 == 4:
        fonk(i, fark)
    elif fark1 == 5:
        fonk(i, fark)
    elif fark1 == 6:
        fonk(i, fark)
    elif fark1 == 7:
        fonk(i, fark)
if secim == 1:
    makinaSayisi = int(input("Number of Machines Required from the Subnet (For example 32 / 64): "))
    if makinaSayisi > 32 and makinaSayisi < 64:
        makinaSayisi = 64
        print("!!! Since the number of machines entered does not meet the 2 ^ n rule, it is completed to the nearest 2 ^ n rule {} It happenedu".format(makinaSayisi))
    if makinaSayisi > 16 and makinaSayisi < 32:
        makinaSayisi = 32
        print("!!! Since the number of machines entered does not meet the 2 ^ n rule, it is completed to the nearest 2 ^ n rule {} It happenedu".format(makinaSayisi))
    if makinaSayisi > 8 and makinaSayisi < 16:
        makinaSayisi = 16
        print("!!! Since the number of machines entered does not meet the 2 ^ n rule, it is completed to the nearest 2 ^ n rule {} It happenedu".format(makinaSayisi))
    if makinaSayisi > 4 and makinaSayisi < 8:
        makinaSayisi = 8
        print("!!! Since the number of machines entered does not meet the 2 ^ n rule, it is completed to the nearest 2 ^ n rule {} It happenedu".format(makinaSayisi))
    if makinaSayisi > 2 and makinaSayisi < 4:
        makinaSayisi = 4
        print("!!! Since the number of machines entered does not meet the 2 ^ n rule, it is completed to the nearest 2 ^ n rule {} It happenedu".format(makinaSayisi))
    if makinaSayisi > 0 and makinaSayisi < 2:
        makinaSayisi = 2
        print("!!! Since the number of machines entered does not meet the 2 ^ n rule, it is completed to the nearest 2 ^ n rule {} It happenedu".format(makinaSayisi))
    print(" ")
    for i in range(8):
        a = pow(2,i)
        if a == makinaSayisi:
            print("Number of Bits that will not be used from the end: {}".format(i))
            print("Number of Subnet Bits: {}".format(8 - i))
            alAgBiti = 8 - i ; b = pow(2 , alAgBiti)
            print("Number of Subnets to Assign(2 ^ {}) : {}".format(alAgBiti , b))
            print(" ")
            print("Old CIDR Information: {}".format(24))
            print("New CIDR Information: {}".format(24 + alAgBiti))

            dizi = [] ; agDizi = [] ; broadCast = []
            for x in range(alAgBiti):
                agDizi.append(1)
                broadCast.append(1)
            for y in range(8 - alAgBiti):
                agDizi.append(0)
                broadCast.append(1)
            print("network {} broadcast {}".format(agDizi,broadCast))
            print(" ")
            print("!!! IP POOLS and SAMPLE ASSIGNMENTS")
            aralik = 0
            aralik1 = aralik
            aralik1 = makinaSayisi - 1
            for i in range(b):
                print(" ")
                print("{}. IP Pool For 192.158.69.{} - 192.158.69.{}".format(i + 1 , aralik , aralik1))
                uret = random.randint(aralik,aralik1)
                aralik = aralik1 + 1
                aralik1 = aralik + makinaSayisi - 1
                print("{}. Example for IP Pool: 192.158.69.{}".format(i + 1, uret))
                ikilikTabani = "{:b}".format(uret)
                uzunluk = len(ikilikTabani)
                fark1 = 8 - uzunluk
                farkı(fark1)
if secim == 2:
    altAgSayisi = int(input("Number of Subnets: "))
    for i in range(8):
        a = pow(2,i)
        if a == altAgSayisi:
            print("Number of Subnet Bits: {}".format(i))
            print(" ")
            print("Old CIDR Information: {}".format(24))
            print("New CIDR Information: {}".format(24 + i))
            dizi = [] ; agDizi = [] ; broadCast = [] ; toplam = ' ' ; toplam1 = ''
            makinaSayisi = pow(2, 8 - i)
            for x in range(i):
                agDizi.append(1)
                broadCast.append(1)
            for y in range(8 - i):
                agDizi.append(0)
                broadCast.append(1)
            print(" ")
            print("!!! IP POOLS and SAMPLE ASSIGNMENTS")
            aralik = 0
            aralik1 = aralik
            aralik1 = makinaSayisi - 1
            for i in range(altAgSayisi):
                print(" ")
                print("{}. IP Pool For 192.158.69.{} - 192.158.69.{}".format(i + 1 , aralik , aralik1))
                uret = random.randint(aralik,aralik1)
                aralik = aralik1 + 1
                aralik1 = aralik + makinaSayisi - 1
                print("{}. Example for IP Pool: 192.158.69.{}".format(i + 1, uret))
                ikilikTabani = "{:b}".format(uret)
                uzunluk = len(ikilikTabani)
                fark1 = 8 - uzunluk
                farkı(fark1)
